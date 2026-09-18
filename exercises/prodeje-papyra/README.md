# Prodejní data PAPYRA Industry

Milion řádků fakturace za šest let. Najdi, proč firmě letos poprvé klesla marže.

**Obtížnost:** střední · **Časová náročnost:** 8-12 hodin · **Nástroje:** Python, R, SQL, DuckDB, Power BI · **Témata:** čištění dat, maržová analýza, kohorty zákazníků, cenové rozklady

## Zadání

Zadání je v souboru [zadani.md](zadani.md).

## Data

Datové soubory (6, celkem 74.7 MB) visí u release [`prodeje-papyra-v1`](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1). Nejsou v gitu, aby klonování repozitáře zůstalo rychlé.

Stáhnout všechno najednou a ověřit kontrolní součty:

```bash
python3 stahni_data.py
```

Nebo jednotlivě:

| Soubor | Velikost | SHA-256 |
|---|---|---|
| [prodeje_papyra_2021.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2021.parquet) | 15.1 MB | `258dfd253e1873a8…` |
| [prodeje_papyra_2022.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2022.parquet) | 12.1 MB | `fb32ca41b6102df7…` |
| [prodeje_papyra_2023.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2023.parquet) | 12.1 MB | `5598d8fc667ab4d8…` |
| [prodeje_papyra_2024.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2024.parquet) | 12.0 MB | `96b1efe9685b4d61…` |
| [prodeje_papyra_2025.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2025.parquet) | 11.7 MB | `d3949df9b22bbf4d…` |
| [prodeje_papyra_2026.parquet](https://github.com/mediatoring/study/releases/download/prodeje-papyra-v1/prodeje_papyra_2026.parquet) | 11.6 MB | `d43482e90939ca6e…` |

## Další soubory

- [slozit_dataset.py](slozit_dataset.py)

---

Verze 1 · aktualizováno 2026-09-18

<!-- Generováno nástrojem publish_exercise.py, needituj ručně. -->
