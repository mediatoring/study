#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stahne datove soubory k tomuto cviceni a overi kontrolni soucty."""
import hashlib, sys, urllib.request
from pathlib import Path

BASE = "https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1"
FILES = [
    ('prodeje_papyra_2021.parquet', '258dfd253e1873a878a45c542a0568ae939a714271f5a937fbd655f4a584ccaa'),
    ('prodeje_papyra_2022.parquet', 'fb32ca41b6102df7464ee8e4e05e823e3c6c76f136a37aba3cee9f29d64fd008'),
    ('prodeje_papyra_2023.parquet', '5598d8fc667ab4d803161db9089a0137057dc69826f004d2ebf6088b4221f108'),
    ('prodeje_papyra_2024.parquet', '96b1efe9685b4d6143fc5a3b1112a122e8f12c6916259c9c46ac44a03fefff8c'),
    ('prodeje_papyra_2025.parquet', 'd3949df9b22bbf4da280c9b52a31781051da9353ce135b42230407a32cc18247'),
    ('prodeje_papyra_2026.parquet', 'd43482e90939ca6ed5c6f04e0ecd075a66dd12b7b350290283dbedefbef066c4'),
]

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "data")
    target.mkdir(parents=True, exist_ok=True)
    failed = 0
    for name, want in FILES:
        path = target / name
        if path.exists() and digest(path) == want:
            print(f"  uz stazeno  {name}")
            continue
        print(f"  stahuji     {name} ...", flush=True)
        urllib.request.urlretrieve(f"{BASE}/{name}", path)
        got = digest(path)
        if got != want:
            print(f"  NESEDI kontrolni soucet u {name}")
            print(f"    ceka se {want}")
            print(f"    je      {got}")
            failed += 1
    print("hotovo" if not failed else f"{failed} souboru se nepodarilo overit")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
