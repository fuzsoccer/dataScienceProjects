"""Randomized reasons-count interaction and logistic sensitivity checks."""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.proportion import proportion_confint
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from extend_analysis import SPECS

ROOT = Path(__file__).resolve().parents[1]
RAW, OUT = ROOT/'data/raw', ROOT/'reports'

def fit_reasons(data, outcome='vaccinated', adjust_risk=False):
    d=data[data.algo_condition.isin(['medrec','algorithm'])].copy()
    assert d.num_reasons.isin(['1reason','3reasons']).all()
    assert d[outcome].isin([0,1]).all() and d.s_ID.is_unique
    x=pd.DataFrame({'const':1.,'algorithm':(d.algo_condition=='algorithm').astype(float),
                    'three_reasons':(d.num_reasons=='3reasons').astype(float)},index=d.index)
    x['interaction']=x.algorithm*x.three_reasons
    if adjust_risk:
        x['top3']=(d.risk_condition=='top3').astype(float)
        x['algorithm_top3']=x.algorithm*x.top3
    model=sm.OLS(d[outcome].astype(float),x).fit()
    robust=model.get_robustcov_results(cov_type='HC1',use_t=True)
    contrasts={'Three vs one: medical records':[0,0,1,0],
               'Three vs one: algorithm':[0,0,1,1],
               'Interaction: algorithm minus medical records':[0,0,0,1],
               'Three vs one: equal-arm average':[0,0,1,.5]}
    rows=[]
    for label,vector in contrasts.items():
        vector=vector+[0]*(x.shape[1]-4)
        row={'contrast':label,'n':len(d)}
        for name,m in [('ols',model),('hc1',robust)]:
            test=m.t_test(vector)
            lo,hi=np.asarray(test.conf_int()).ravel()
            row.update({f'{name}_difference_pp':100*test.effect.item(),
                        f'{name}_se_pp':100*test.sd.item(),
                        f'{name}_ci_low_pp':100*lo,f'{name}_ci_high_pp':100*hi,
                        f'{name}_p':test.pvalue.item()})
        rows.append(row)
    result=pd.DataFrame(rows)
    result['hc1_p_holm_within_family']=multipletests(result.hc1_p,method='holm')[1]
    if not adjust_risk:
        means=d.groupby(['algo_condition','num_reasons'])[outcome].mean()
        med=means['medrec','3reasons']-means['medrec','1reason']
        alg=means['algorithm','3reasons']-means['algorithm','1reason']
        assert np.allclose(result.ols_difference_pp,[100*med,100*alg,100*(alg-med),50*(med+alg)],atol=1e-10)
    return result,model

def main():
    OUT.mkdir(exist_ok=True)
    a=pd.read_csv(RAW/'study_2_analysis_data_deid.csv')
    f=pd.read_csv(RAW/'study_2_fulldata_deid.csv')
    d=a[a.algo_condition.isin(['medrec','algorithm'])]
    cells=d.groupby(['algo_condition','num_reasons']).vaccinated.agg(n='size',vaccinated='sum',rate='mean')
    cells['ci_low'],cells['ci_high']=proportion_confint(cells.vaccinated,cells.n,method='wilson')
    cells.to_csv(OUT/'reasons_cell_rates.csv')
    fd=f[f.algo_condition.isin(['medrec','algorithm'])].copy()
    fd['status']=fd.exclude_reason.fillna('included')
    pd.crosstab([fd.algo_condition,fd.num_reasons,fd.risk_condition],fd.status).to_csv(OUT/'reasons_exclusion_audit.csv')
    results=[]
    for pop, data, outcome,adjust in [
        ('analysis',a,'vaccinated',False),
        ('analysis_risk_adjusted',a,'vaccinated',True),
        ('analysis_no_shared_address',a[a.dup_address==0],'vaccinated',False),
        ('enrolled_excluding_contra',f[f.exclude_reason.fillna('included')!='contra'],'vaccinated',False),
        ('all_enrolled',f,'vaccinated',False),
        ('analysis',a,'vaccinated_4weeks',False)]:
        r,_=fit_reasons(data,outcome,adjust)
        r.insert(0,'outcome',outcome)
        r.insert(0,'population',pop)
        results.append(r)
    res=pd.concat(results,ignore_index=True)
    res.to_csv(OUT/'reasons_contrasts.csv',index=False)
    _,source=fit_reasons(a)
    pd.DataFrame({'term':source.params.index,'estimate':source.params.values,
                  'standard_error':source.bse.values,'p_value':source.pvalues.values}).to_csv(OUT/'reasons_ols_coefficients.csv',index=False)
    logistic=[]
    for label,t,c in SPECS:
        subset=a[a.algo_condition.isin(t+c)]
        x=sm.add_constant(subset.algo_condition.isin(t).astype(float).rename('treatment'))
        m=sm.GLM(subset.vaccinated,x,family=sm.families.Binomial()).fit()
        ci=m.conf_int().loc['treatment']
        logistic.append({'contrast':label,'n':len(subset),'odds_ratio':np.exp(m.params.treatment),
                         'or_ci_low':np.exp(ci.iloc[0]),'or_ci_high':np.exp(ci.iloc[1]),'p_value':m.pvalues.treatment})
    log=pd.DataFrame(logistic)
    log['p_holm']=multipletests(log.p_value,method='holm')[1]
    log.to_csv(OUT/'logistic_sensitivity.csv',index=False)
    main=res[(res.population=='analysis') & (res.outcome=='vaccinated')].reset_index(drop=True)
    fig,ax=plt.subplots(figsize=(9,4.5))
    values=main.hc1_difference_pp
    ax.errorbar(values,range(4),xerr=np.vstack([values-main.hc1_ci_low_pp,main.hc1_ci_high_pp-values]),fmt='o',capsize=4,color='#176B87')
    ax.axvline(0,color='grey',linestyle='--',linewidth=1)
    ax.set_yticks(range(4),['3 vs 1: medical records','3 vs 1: algorithm','Interaction: algorithm minus records','3 vs 1: equal-arm average'])
    ax.invert_yaxis()
    ax.set_xlabel('Difference in vaccination (percentage points), 95% HC1 intervals')
    ax.set_title('Does giving three reasons improve vaccination uptake?')
    ax.grid(axis='x',alpha=.2)
    fig.tight_layout()
    fig.savefig(OUT/'reasons_effects.png',dpi=180)
    plt.close(fig)
    manifest={'reference_cell':'medical records, one reason','interaction_sign':'algorithm (3-1) minus medical records (3-1)',
              'average':'equal weight to the two messaging arms; not weighted by observed cell sizes',
              'multiplicity':'four related contrasts per population and endpoint; no global error control',
              'analysis_reasons_n':len(d),
              'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [RAW/'study_2_analysis_data_deid.csv',RAW/'study_2_fulldata_deid.csv']}}
    (OUT/'reasons_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(main[['contrast','hc1_difference_pp','hc1_ci_low_pp','hc1_ci_high_pp','hc1_p','hc1_p_holm_within_family']].to_string(index=False))
    print(log.to_string(index=False))
    print('Unadjusted model contrasts match observed cell differences.')

if __name__=='__main__':
    main()
