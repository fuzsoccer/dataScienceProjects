"""Rebuild Study 2 descriptive EDA and exploratory A/B contrasts.

Run from any directory: python path/to/src/analyze.py
"""
from pathlib import Path
import hashlib
import json
import platform
import numpy as np
import pandas as pd
from scipy.stats import norm, chisquare
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW, OUT = ROOT / 'data/raw', ROOT / 'reports'
ARMS = ['nocontact', 'control', 'unspecified', 'medrec', 'algorithm']
LABELS = ['Passive control', 'Active control', 'High risk only',
          'Medical records + reasons', 'Algorithm + reasons']

def contrast(a, treatment, reference, name):
    t = a.loc[a.algo_condition.isin(treatment), 'vaccinated']
    c = a.loc[a.algo_condition.isin(reference), 'vaccinated']
    diff = t.mean() - c.mean()
    se = np.sqrt(t.mean()*(1-t.mean())/len(t) + c.mean()*(1-c.mean())/len(c))
    pooled = (t.sum()+c.sum())/(len(t)+len(c))
    null_se = np.sqrt(pooled*(1-pooled)*(1/len(t)+1/len(c)))
    return dict(contrast=name, n_treatment=len(t), n_reference=len(c),
                difference_pp=100*diff, ci_low_pp=100*(diff-1.96*se),
                ci_high_pp=100*(diff+1.96*se),
                relative_lift_pct=100*diff/c.mean(), p_value=2*norm.sf(abs(diff/null_se)))

def main():
    OUT.mkdir(exist_ok=True)
    a = pd.read_csv(RAW/'study_2_analysis_data_deid.csv')
    f = pd.read_csv(RAW/'study_2_fulldata_deid.csv')
    assert a.s_ID.is_unique and f.s_ID.is_unique
    assert set(a.algo_condition) == set(ARMS)
    assert a.vaccinated.isin([0,1]).all() and a.vaccinated_4weeks.isin([0,1]).all()
    included = f.loc[f.exclude_reason.isna()]
    assert set(a.s_ID) == set(included.s_ID)
    joined = a.merge(included, on='s_ID', suffixes=('_analysis','_full'), validate='one_to_one')
    for col in ['algo_condition','vaccinated','risk_condition']:
        assert (joined[col+'_analysis'] == joined[col+'_full']).all()
    assert ((a.vaccinated == 0) == a.vax_source.isna()).all()
    assert (a.vaccinated_4weeks <= a.vaccinated).all()

    summary = a.groupby('algo_condition').vaccinated.agg(n='size', vaccinated='sum', rate='mean').reindex(ARMS)
    z = norm.ppf(.975)
    n, p = summary.n, summary.rate
    center = (p+z*z/(2*n))/(1+z*z/n)
    half = z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
    summary['ci_low'], summary['ci_high'] = center-half, center+half
    summary.to_csv(OUT/'arm_rates.csv')
    a.isna().agg(['sum','mean']).T.to_csv(OUT/'missingness.csv')
    dictionary = pd.DataFrame({'variable':a.columns, 'dtype':a.dtypes.astype(str).values,
                               'unique_nonmissing':a.nunique().values,
                               'missing':a.isna().sum().values})
    dictionary.to_csv(OUT/'variable_inventory.csv', index=False)
    flow = pd.crosstab(f.algo_condition, f.exclude_reason.fillna('included')).reindex(ARMS)
    flow['enrolled'] = flow.sum(axis=1)
    flow['excluded_pct'] = 100*(flow.enrolled-flow.included)/flow.enrolled
    flow.to_csv(OUT/'exclusions_by_arm.csv')
    for col in ['sex','race','ethnicity','age_bin','risk_condition','modalities','dup_address','geis_pcp','num_reasons','sms_date_bin']:
        pd.crosstab(a[col].fillna('(missing/not applicable)'), a.algo_condition, normalize='columns').reindex(columns=ARMS).to_csv(OUT/f'distribution_{col}.csv')
    specs = [(['unspecified','medrec','algorithm'], ['control'], 'Pooled high risk vs active control'),
             (['medrec','algorithm'], ['unspecified'], 'Reasons arms vs high risk only'),
             (['algorithm'], ['medrec'], 'Algorithm vs medical records')]
    specs += [([arm], ['nocontact'], f'{arm} vs passive control') for arm in ARMS[1:]]
    contrasts = pd.DataFrame([contrast(a,*s) for s in specs])
    order = np.argsort(contrasts.p_value.to_numpy())
    adjusted = np.minimum(1,np.maximum.accumulate((len(order)-np.arange(len(order)))*contrasts.p_value.to_numpy()[order]))
    contrasts['p_holm'] = np.nan
    contrasts.loc[order,'p_holm'] = adjusted
    contrasts.to_csv(OUT/'exploratory_contrasts.csv',index=False)
    # Equal allocation is an explicitly provisional diagnostic, not a confirmed design assumption.
    enrollment_counts = f.algo_condition.value_counts().reindex(ARMS)
    srm = chisquare(enrollment_counts)
    manifest = {'python':platform.python_version(),'pandas':pd.__version__, 'numpy':np.__version__,
                'randomized_reported_in_R_script':45164, 'enrolled':len(f), 'analyzed':len(a),
                'equal_allocation_enrolled_chisq':float(srm.statistic),
                'equal_allocation_enrolled_p':float(srm.pvalue),
                'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(RAW.iterdir())}}
    (OUT/'run_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    fig, ax = plt.subplots(figsize=(9,4.8))
    ax.errorbar(summary.rate*100, np.arange(5), xerr=np.vstack([(summary.rate-summary.ci_low)*100,(summary.ci_high-summary.rate)*100]), fmt='o',capsize=4,color='#176B87')
    ax.set_yticks(np.arange(5),LABELS)
    ax.invert_yaxis()
    ax.set_xlabel('Vaccinated (%) with 95% Wilson confidence interval')
    ax.set_title('Study 2: observed vaccination by messaging arm')
    ax.grid(axis='x',alpha=.2)
    fig.tight_layout()
    fig.savefig(OUT/'vaccination_rates.png',dpi=180)
    plt.close(fig)
    print(summary.to_string())
    print(contrasts.to_string(index=False))
    print('Integrity checks passed; reports rebuilt.')

if __name__ == '__main__':
    main()
