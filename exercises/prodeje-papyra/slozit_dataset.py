"""
Slozi rocni soubory prodeje_papyra_<rok>.parquet zpet do jednoho datasetu.
Spusteni:  python3 slozit_dataset.py
Vytvori:   prodeje_papyra_2021_2026.parquet  (~60 MB)
           prodeje_papyra_2021_2026.csv      (~373 MB)

Vyzaduje pandas a pyarrow:  pip install pandas pyarrow
CSV se da preskocit parametrem --bez-csv, pokud staci parquet.
"""
import glob, sys, pandas as pd

files = sorted(glob.glob('prodeje_papyra_2*.parquet'))
files = [f for f in files if '2021_2026' not in f]
if not files:
    sys.exit('Nenasel jsem rocni soubory prodeje_papyra_<rok>.parquet ve stejne slozce.')

print(f'Nactam {len(files)} souboru...')
df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
df = df.sort_values(['DATUM', 'FAKTURA']).reset_index(drop=True)
print(f'Celkem {len(df):,} radku, {len(df.columns)} sloupcu, '
      f'{df.DATUM.min().date()} az {df.DATUM.max().date()}')

df.to_parquet('prodeje_papyra_2021_2026.parquet', index=False, compression='zstd')
print('Ulozeno: prodeje_papyra_2021_2026.parquet')

if '--bez-csv' not in sys.argv:
    out = df.copy()
    out['DATUM'] = out.DATUM.dt.strftime('%Y-%m-%d')
    out.to_csv('prodeje_papyra_2021_2026.csv', index=False, encoding='utf-8')
    print('Ulozeno: prodeje_papyra_2021_2026.csv')
