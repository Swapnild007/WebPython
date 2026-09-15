import pandas as pd

def analyze(path):
    df=pd.read_csv(path)
    required={'skill_name','incoming','handled','abandoned','aht_seconds'}
    missing=required-set(df.columns)
    if missing: raise ValueError(f'Missing columns: {sorted(missing)}')
    df['abandon_rate_pct']=df['abandoned'].div(df['incoming'].replace(0,pd.NA)).mul(100)
    summary=(df.groupby('skill_name',dropna=False).agg(Offered=('incoming','sum'),Handled=('handled','sum'),Abandoned=('abandoned','sum'),AHT=('aht_seconds','mean')).reset_index())
    return summary

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('csv'); a=p.parse_args(); print(analyze(a.csv).to_string(index=False))
