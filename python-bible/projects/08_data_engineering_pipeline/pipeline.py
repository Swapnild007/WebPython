from pathlib import Path
import pandas as pd

def extract(csv_path): return pd.read_csv(csv_path)
def transform(df):
    df=df.copy(); df.columns=[c.strip().lower() for c in df.columns]
    if 'timestamp' in df: df['timestamp']=pd.to_datetime(df['timestamp'],errors='coerce',utc=True)
    return df.drop_duplicates().dropna(how='all')
def load(df,out='processed.parquet'):
    Path(out).parent.mkdir(parents=True,exist_ok=True); df.to_parquet(out,index=False); return out

def run(source,out='data/processed.parquet'): return load(transform(extract(source)),out)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('source'); p.add_argument('--out',default='data/processed.parquet'); a=p.parse_args(); print(run(a.source,a.out))
