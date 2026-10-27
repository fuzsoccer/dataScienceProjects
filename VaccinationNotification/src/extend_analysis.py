"""Baseline balance and source-aligned model/sensitivity extension."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import statsmodels
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

ROOT = Path(__file__).resolve().parents[1]
RAW, OUT = ROOT/'data/raw', ROOT/'reports'
ARMS = ['nocontact','control','unspecified','medrec','algorithm']
HIGH = ['unspecified','medrec','algorithm']
SPECS = [('1a_highrisk_vs_active', HIGH, ['control']),
         ('1b_highrisk_vs_passive', HIGH, ['nocontact']),
         ('2_reasons_vs_highrisk_only', ['medrec','algorithm'], ['unspecified']),
         ('3_active_vs_passive', ['control'], ['nocontact'])]

def fit_contrast(df, outcome, treatment, reference, label, population, adjust_risk=False):
    d = df[df.algo_condition.isin(treatment+reference)].copy()
    assert d[outcome].notna().all() and d[outcome].isin([0,1]).all()
    x = d.algo_condition.isin(treatment).astype(float).rename('treatment')
    design = sm.add_constant(x)
    if adjust_risk:
        design['top3'] = (d.risk_condition == 'top3').astype(float)
    model = sm.OLS(d[outcome].astype(float), design).fit()
    # HC1 with t-based inference mirrors the source robustness approach.
    robust = model.get_robustcov_results(cov_type='HC1', use_t=True)
    raw_diff = d.loc[x==1,outcome].mean()-d.loc[x==0,outcome].mean()
    if not adjust_risk:
        assert np.isclose(model.params['treatment'],raw_diff,atol=1e-12)
    result = dict(population=population,outcome=outcome,contrast=label,n=len(d),
                  n_treatment=int(x.sum()),n_reference=int((x==0).sum()),
                  difference_pp=100*model.params['treatment'])
    for name, mod in [('ols',model),('hc1',robust)]:
        ci = np.asarray(mod.conf_int())[1]
        result.update({f'{name}_se_pp':100*np.asarray(mod.bse)[1],
                       f'{name}_ci_low_pp':100*ci[0],f'{name}_ci_high_pp':100*ci[1],
                       f'{name}_p':np.asarray(mod.pvalues)[1]})
    return result

def balance(df, variables, population):
    rows=[]
    for var in variables:
        for level in sorted(df[var].fillna('(missing)').astype(str).unique()):
            indicator=(df[var].fillna('(missing)').astype(str)==level)
            proportions=indicator.groupby(df.algo_condition).mean().reindex(ARMS)
            for i,left in enumerate(ARMS):
                for right in ARMS[i+1:]:
                    p,q=proportions[left],proportions[right]
                    denom=np.sqrt((p*(1-p)+q*(1-q))/2)
                    smd=(p-q)/denom if denom else (0 if p==q else np.nan)
                    rows.append(dict(population=population,variable=var,level=level,
                                     arm_left=left,arm_right=right,p_left=p,p_right=q,smd=smd,abs_smd=abs(smd)))
    return pd.DataFrame(rows)

def main():
    a=pd.read_csv(RAW/'study_2_analysis_data_deid.csv')
    f=pd.read_csv(RAW/'study_2_fulldata_deid.csv')
    b=pd.concat([balance(f,['sex','race','ethnicity','risk_condition','modalities_orig'],'enrolled'),
                 balance(a,['sex','race','ethnicity','risk_condition','age_bin','geis_pcp','dup_address'],'analysis')],ignore_index=True)
    b.to_csv(OUT/'baseline_balance_pairwise.csv',index=False)
    b.groupby(['population','variable']).abs_smd.max().rename('maximum_absolute_smd').to_csv(OUT/'baseline_balance_summary.csv')
    rows=[]
    populations={'analysis':a,'analysis_no_shared_address':a[a.dup_address==0],
                 'enrolled_excluding_contra':f[f.exclude_reason.fillna('included')!='contra'],
                 'all_enrolled':f}
    for population, data in populations.items():
        for label,t,c in SPECS:
            rows.append(fit_contrast(data,'vaccinated',t,c,label,population))
    for label,t,c in SPECS:
        rows.append(fit_contrast(a,'vaccinated_4weeks',t,c,label,'analysis'))
    results=pd.DataFrame(rows)
    # Separate exploratory family per population and endpoint; not global control across this report.
    results['hc1_p_holm_within_family']=results.groupby(['population','outcome']).hc1_p.transform(lambda x:multipletests(x,method='holm')[1])
    results.to_csv(OUT/'source_aligned_models.csv',index=False)
    adjusted=pd.DataFrame([fit_contrast(a,'vaccinated',t,c,label,'analysis_risk_adjusted',True) for label,t,c in SPECS])
    adjusted['hc1_p_holm_within_family']=multipletests(adjusted.hc1_p,method='holm')[1]
    adjusted.to_csv(OUT/'risk_adjusted_models.csv',index=False)
    arm=pd.crosstab(f.algo_condition,f.exclude_reason.fillna('included')).reindex(ARMS)
    arm['excluded']=arm.sum(axis=1)-arm.included
    arm['total']=arm.included+arm.excluded
    arm['exclusion_rate']=arm.excluded/arm.total
    arm.to_csv(OUT/'exclusion_audit.csv')
    manifest={'statsmodels':statsmodels.__version__, 'method':'OLS and HC1 with t reference distribution',
              'families':'four source-aligned contrasts within each population/endpoint',
              'no_shared_address_n':len(populations['analysis_no_shared_address']),
              'enrolled_excluding_contra_n':len(populations['enrolled_excluding_contra']),
              'all_enrolled_n':len(f)}
    (OUT/'extension_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(b.groupby(['population','variable']).abs_smd.max().to_string())
    print(results[['population','outcome','contrast','difference_pp','hc1_ci_low_pp','hc1_ci_high_pp','hc1_p','hc1_p_holm_within_family']].to_string(index=False))
    print('All model coefficients match direct differences in means.')

if __name__=='__main__':
    main()
