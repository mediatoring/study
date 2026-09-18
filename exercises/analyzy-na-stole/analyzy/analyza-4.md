# Slevová politika a ziskovost segmentů

**Zpracoval:** obchodní controlling · **Pro:** vedení společnosti · **Datum:** 19. ledna 2027

## Dvě otázky

Před jednáním o cenících roku 2027 jsem dostal dvě otázky. Jak velké slevy z ceníku ve
skutečnosti dáváme a který zákaznický segment je pro firmu nejziskovější. Obojí počítám za rok
2026 a jen z řádků s kladnými tržbami, aby dobropisy nezkreslovaly obrázek.

## Slevy

Systémový sloupec `SLEVA` je pro tenhle účel nepoužitelný, je vyplněný jen u zlomku řádků.
Skutečnou slevu proto počítám jako rozdíl ceníkové a skutečně fakturované ceny za měrnou jednotku:

```
sleva_% = 100 * (1 - PRODEJNI_CENA_MENA_MJ / CENIK_MENA)
```

Průměr přes všechny řádky, kde jsou obě ceny vyplněné, vychází na **11,5 procenta**. Medián je
nula, protože 58,5 procenta řádků se prodává přesně za ceník. Slev nad třicet procent je
5,6 procenta řádků.

Po segmentech:

| Segment | Průměrná sleva na řádek |
|---|---|
| Velkoobchod | 21,6 % |
| `Ostatni` | 4,2 % |
| `Retezce` | 0,6 % |

Velkoobchod tedy dostává výrazně víc než řetězce, což na první pohled překvapí, ale dává smysl:
velkoobchod odebírá ve větších baleních a s delší splatností, zatímco řetězce mají ceny
vyjednané přímo v ceníku, takže sleva se u nich formálně neuplatňuje.

## Ziskovost segmentů

Ziskovost jsem spočítal jako průměrnou procentní marži řádku v daném segmentu. Marží se rozumí
tržby minus náklady prodaného zboží minus ostatní přímé náklady, tedy sloupec `MARZE`.

| Segment | Průměrná marže řádku | Počet řádků | Počet odběratelů |
|---|---|---|---|
| `Ostatni` | 49,6 % | 1 275 | 103 |
| Velkoobchod | 39,9 % | 84 942 | 66 |
| `Retezce` | 20,0 % | 76 292 | 12 |

Rozdíl mezi nejlepším a nejhorším segmentem je téměř třicet procentních bodů, což je na jednu
firmu hodně. Segment `Ostatni` je přitom nejpočetnější co do počtu odběratelů – je v něm 103 z
celkových 206 zákazníků.

## Interpretace

Obrázek je konzistentní. Řetězce nám dělají objem za nízkou marži, velkoobchod je zlatá střední
cesta a drobnější zákazníci v segmentu `Ostatni` platí nejlépe. Že zrovna u nich dáváme
nejmenší slevy a zároveň na nich máme nejvyšší marži, není náhoda, ale důsledek toho, že nemají
vyjednávací sílu velkých řetězců.

Slevová politika jako celek působí zdravě. Průměrných 11,5 procenta je hluboko pod tím, co se
v oboru běžně dává, a víc než polovina obchodu jde za plný ceník.

## Doporučení

Slevovou politiku bych neměnil, prostor pro zpřísnění tam nevidím. Obchodně bych se soustředil na
segment `Ostatni`, který je zdaleka nejziskovější a kde je zároveň nejvíc zákazníků, takže
i prostor růst. Naopak bych zvážil, jestli má smysl dál tlačit objem do segmentu `Retezce`, kde
marže sotva dosahuje dvaceti procent a kde nás dvanáct odběratelů drží v šachu vyjednáváním
o každé koruně.
