# Prodejní data PAPYRA Industry a.s. – cvičení pro studenty

## O čem to je

PAPYRA Industry a.s. je středně velký výrobce kancelářského, školního a papírenského
zboží. Vyrábí ve dvou závodech a prodává ve dvou kanálech: velkoobchodním
distributorům a maloobchodním řetězcům, v tuzemsku i na export. Dataset je kompletní
řádkový výpis prodejů z podnikového systému za období **4. ledna 2021 až 24. prosince
2026**: jeden řádek = jedna položka na jedné faktuře.

Data jsou taková, jaká ze systému opravdu vypadnou. Nikdo je pro vás nepřipravil,
nevyčistil ani nezkontroloval. Obsahují chyby, nepoužitelné sloupce i hodnoty, které
vypadají podezřele a přitom jsou v pořádku. Rozpoznat jedno od druhého je součástí
úkolu, ne překážka před ním.

PAPYRA Industry a.s. je smyšlená firma a dataset je syntetický: vygeneroval ho nástroj, který
napodobuje strukturu i typické nešvary skutečného exportu z podnikového systému. Názvy firem,
položek a identifikátory neodkazují na nic existujícího – data se ale chovají přesně tak, jak se
data z praxe chovají.

## Soubory

Dataset je rozdělený po letech do šesti souborů `prodeje_papyra_2021.parquet` až
`prodeje_papyra_2026.parquet`. Dohromady mají 1 101 915 řádků a 41 sloupců.

Soubory nejsou součástí repozitáře, visí jako přílohy u release. Ve stejné složce jako toto
zadání leží skript `stahni_data.py`, který je stáhne všechny najednou a ověří kontrolní součty:

```bash
python3 stahni_data.py
```

Kdo chce stahovat ručně, najde odkazy, velikosti i kontrolní součty v souboru `README.md` vedle
tohoto zadání: <https://github.com/mediatoring/study/tree/main/exercises/prodeje-papyra>.

Většina nástrojů je umí načíst najednou. V DuckDB stačí
`SELECT * FROM 'prodeje_papyra_2*.parquet'`, v pandas
`pd.concat([pd.read_parquet(f) for f in glob.glob('prodeje_papyra_2*.parquet')])`.
Přiložený skript `slozit_dataset.py` je spojí do jednoho souboru a volitelně i do CSV
s oddělovačem čárkou, desetinnou tečkou a kódováním UTF-8; spouští se bez parametrů.

Pozor při čtení CSV: prázdné řetězce v textových sloupcích se standardně načtou jako
chybějící hodnota. Pokud chcete stejné výsledky jako z parquetu, čtěte s
`keep_default_na=False` a číselné sloupce převeďte explicitně.

Nástroje jsou na vás. Python s pandas nebo Polars, DuckDB, R, SQL, Power BI, Excel
s Power Query – cokoli, s čím dokážete dojít k výsledku. Klidně si nechte kód
vygenerovat AI; podstatné je, že rozumíte tomu, co počítáte, a umíte obhájit, proč to
tak počítáte. V Excelu se dataset v plné velikosti neotevře, počet řádků překračuje
limit listu; pokud chcete pracovat v Excelu, budete muset data nejdřív někde agregovat.

## Než začnete počítat

Ověřte si, že máte data načtená správně. Čisté tržby roku 2025 – tedy součet sloupce `TRZBY_CZK`
za rok 2025 včetně záporných řádků dobropisů – musí vyjít **399,6 milionu korun**. Když vám
vyjde něco jiného, nejspíš vám chybí některý z ročních souborů nebo jste cestou ztratili záporné
řádky; dokud to nesedí, nemá smysl počítat dál. Kontrola je schválně postavená na roce 2025,
takže projde i dřív, než se pustíte do čištění dat.

## Co znamenají sloupce

**Doklad a čas.** `MISTO` je závod, ve kterém prodej vznikl. `DATUM` je datum
vystavení dokladu, `ROK`, `MESIC`, `KVARTAL` a `POLOLETI` jsou z něj odvozené.
`FAKTURA` je číslo dokladu; prefix `FA` označuje fakturu, prefix `DB` dobropis.

**Odběratel.** `ODBER_ID`, `ODBER_ICO` a `ODBER_NAZEV` identifikují zákazníka,
`ODBER_SKUP` je obchodní segment, do kterého ho firma řadí, `DODACI_MISTO` je konkrétní
dodací adresa nebo pobočka. `ZEME` a `REGION` popisují, kam zboží šlo.

**Položka.** `POLOZKA_ID` a `POLOZKA_NAZEV` identifikují výrobek. `PROD_SKUPINA` je
sedmimístný kód produktové skupiny a sloupce `PS1_SKUPINA` až `PS5_TYP` jsou jeho
postupné předpony, tedy pět úrovní stromu sortimentu od nejhrubší po nejjemnější.
`PS6_ZPUS_PRODEJE` a `PS7_ZPUS_VZNIKU` jsou interní kódy způsobu prodeje a původu
položky, `SKLAD` rozlišuje tuzemský a exportní sklad, `KOD_TRHU` kóduje trh.

**Peníze a množství.** `MNOZSTVI` je počet kusů, u dobropisů záporný. `TRZBY_CZK` je
tržba řádku v korunách, `TRZBY_MENA` tatáž tržba v měně dokladu a `KOD_MENY` říká, o
jakou měnu jde. `NAKLADY_CZK` jsou náklady prodaného zboží, `OPN_CZK` ostatní přímé
náklady (doprava, obalový materiál). `MARZE` je hrubá marže řádku v korunách.

**Ceny za jednotku.** `CENIK_MENA` je katalogová ceníková cena za měrnou jednotku v měně
dokladu, `PRODEJNI_CENA_MENA_MJ` skutečně fakturovaná cena za měrnou jednotku v téže
měně a `PRODEJNI_CENA_MJ` totéž v korunách. `NAKLADY_MJ` je náklad na měrnou jednotku.
`SLEVA` je pole, do kterého obchodní systém zapisuje slevu.

**Kalkulace.** `NAKL_PRIME_CZK` jsou přímé náklady z výrobní kalkulace, `PRIME_MZDY`
přímé mzdy a `KRYCI_PRISPEVEK` krycí příspěvek spočtený controllingem. Tyto tři sloupce
pracují s kalkulačními cenami, ne s účetními, takže se s předchozí skupinou nemusí
přesně sejít.

---

# Otázky

## A. Základní orientace

**1.** Kolik dataset obsahuje řádků, faktur, odběratelů a položek a jaké přesně období
pokrývá? Kolik řádků zbude, když odstraníte to, co v datech nemá co dělat?

**2.** Sestavte pro každý rok celkové tržby, náklady, hrubou marži v korunách i
procentech a prodané množství. Popište, co se s firmou mezi lety 2021 a 2026 stalo.

**3.** Které tři měsíce byly za celou historii nejsilnější a které tři nejslabší?
Je za tím sezónnost, nebo jednorázová událost?

**4.** Jaký podíl tržeb tvoří export mimo Českou republiku a jak se tento podíl vyvíjel?
Které země za tím stojí?

**5.** Jaká část tržeb se fakturuje v eurech? Spočítejte z dat implikovaný kurz pro každý
rok a posuďte, jestli kurzový vývoj firmě pomohl, nebo uškodil.

**6.** Jak je koncentrovaná zákaznická základna? Spočítejte podíl pěti, deseti a dvaceti
největších odběratelů na tržbách roku 2026.

## B. Kvalita dat

**7.** Obsahuje dataset duplicitní řádky? Kolik jich je a kdy vznikly? Jak poznáte
duplicitu od dvou legitimních stejných řádků na jedné faktuře?

**8.** Najděte v datech doklad, jehož hodnota je zjevně chybná. O jakou chybu jde, jak
velkou škodu nadělá v součtech a proč si jí nemusíte všimnout, pokud se díváte jen na
čisté tržby? Pozor: ne každý řádek s vysokou jednotkovou cenou je chyba – vysvětlete,
které takové řádky jsou v pořádku a proč.

**9.** Sloupec `SLEVA` vypadá jako užitečný. Ověřte, jestli je. Pokud není, najděte
způsob, jak skutečně poskytnutou slevu z dat spočítat, a řekněte, kolik v roce 2026 dělá.

**10.** Ve kterých sloupcích chybí hodnoty a jak často? Rozhodněte u každého, jestli
chybějící hodnotu doplníte, vyřadíte, nebo necháte být, a rozhodnutí zdůvodněte.

**11.** Ověřte, jestli v datech platí vztah `MARZE = TRZBY_CZK − NAKLADY_CZK − OPN_CZK`.
Pak ověřte, jestli `KRYCI_PRISPEVEK` odpovídá rozdílu tržeb a nákladů. Pokud ne,
vysvětlete proč a řekněte, který ukazatel použijete pro měření ziskovosti obchodu.

**12.** Jaký je rozdíl mezi hrubými a čistými tržbami po započtení dobropisů? Spočítejte
podíl dobropisů na hrubých tržbách v každém roce.

## C. Zákazníci

**13.** Jeden významný odběratel z dat na přelomu let zmizel. Který, kdy naposledy
nakoupil a kolik ročně firmě přinášel?

**14.** Nahradil někdo jeho výpadek? Sestavte žebříček největších meziročních přírůstků a
úbytků 2026 proti 2025.

**15.** Najděte odběratele, který se objevil až v průběhu roku 2026 a rychle vyrostl.
Porovnejte jeho marži s průměrem jeho segmentu a rozhodněte, jestli je to dobrá zpráva.

**16.** U kterého většího odběratele rostou dobropisy? Ukažte vývoj po měsících a
odhadněte, o kolik korun firma kvůli tomu v roce 2026 přišla.

**17.** Kolik odběratelů z roku 2021 nakupuje i v roce 2026? Kolik jich za tu dobu
přibylo? Co to vypovídá o obchodní strategii firmy?

**18.** Sestavte ABC analýzu odběratelů za rok 2026. Kolik zákazníků tvoří prvních 80 %
tržeb?

## D. Sortiment a ceny

**19.** Jak se vyvíjela hrubá marže jednotlivých produktových skupin (`PS1_SKUPINA`) mezi
lety 2021 a 2026? Které skupiny táhnou ziskovost nahoru a které dolů?

**20.** Která produktová skupina ztratila nejvíc prodaného množství a kdy? Co se v té
době stalo s jejími cenami a marží?

**21.** Ve čtvrtém čtvrtletí 2026 se jedné skupině prudce zhoršila marže. Které, o kolik a
proč? Zjistěte, jestli firma reagovala, jak rychle a jestli to stačilo.

**22.** Najděte položku, které dlouhodobě klesá jednotková cena, zatímco prodané množství
roste. Spočítejte, jestli na ní firma vydělává víc, nebo míň než před dvěma lety.

**23.** Kolik položek tvoří 80 % tržeb roku 2026? Jak velká část sortimentu se prakticky
neprodává?

**24.** Jak velkou skutečnou slevu z ceníku dostávají jednotlivé segmenty odběratelů?
Výsledek bude nejspíš protiintuitivní – vysvětlete, čím to může být.

## E. Rozbory a rozhodnutí

**25.** Rozložte meziroční změnu tržeb 2026 proti 2025 na čtyři složky: vliv objemu, vliv
ceny, příspěvek nově zavedených položek a ztrátu po položkách, které z nabídky vypadly.
Zkontrolujte, že se složky sečtou na celkovou změnu.

Rozkladů existuje víc a každý dá trochu jiná čísla, takže se držte téhle konvence: počítejte po
položkách (`POLOZKA_ID`), jednotkovou cenu berte jako tržby dělené množstvím a za společné
považujte položky s kladným množstvím v obou letech. Vliv objemu je součet
(množství 2026 − množství 2025) × cena 2025, vliv ceny součet
(cena 2026 − cena 2025) × množství 2026. Nové položky vstupují celou tržbou roku 2026, vypadlé
celou tržbou roku 2025 se záporným znaménkem. Pokud zvolíte jinou konvenci, napište ji
k výsledku – uzná se, jen musí být zřejmé, co jste počítali.

**26.** Marže firmy mezi roky 2021 a 2026 výrazně vzrostla. Rozhodněte, kolik z toho udělal
růst prodejních cen a kolik vývoj nákladů. Použijte ukazatele na jeden kus.

**27.** Spočítejte sezónní index pro každý měsíc z let 2022 až 2025. Co z toho plyne pro
plánování výroby a pro cashflow?

Postup, se kterým se porovnává vzorové řešení: v každém roce zvlášť položte průměrné měsíční
tržby na 100 a každý měsíc vyjádřete jako procento tohoto průměru; index měsíce je pak prostý
průměr těchto čtyř ročních hodnot. Jiný postup – třeba index počítaný z celého období najednou –
dá mírně jiná čísla a je v pořádku, pokud ho u výsledku popíšete.

**28.** Simulujte, co by se stalo, kdyby firma odmítla veškerý obchod pod určitou hranicí
marže. Vyzkoušejte prahy 0, 10, 20 a 30 procent a ukažte, kolik tržeb a kolik krycího
příspěvku by v každé variantě zůstalo. Kde je hranice, za kterou už to firmě škodí?

**29.** Vyčíslete riziko koncentrace. Jaký podíl tržeb a jaký podíl marže drží největší
odběratel a první tři dohromady? Spočítejte Herfindahl-Hirschmanův index a odhadněte
dopad ztráty největšího zákazníka. Index počítejte z podílů odběratelů na tržbách roku 2026
vyjádřených v procentech, takže výsledek leží na stupnici 0 až 10 000. Z desetinných podílů vyjde
totéž číslo děleno deseti tisíci a obvyklé hranice pro nízkou a vysokou koncentraci pak neplatí
tak, jak se citují.

**30.** Napište jednostránkové shrnutí pro vedení firmy. Nejvýš pět zjištění, ke každému
číslo, které ho dokládá, a jedno doporučení. Píšete pro člověka, který dataset nikdy
neviděl a otevře váš text mezi dvěma schůzkami.

## F. Volná úloha

**31.** Předchozích třicet otázek vám řeklo, kam se podívat. Tahle ne. Najděte v datech příběh, na
který se nikdo neptal, a vyprávějte ho: co se ve firmě dělo, z čeho to v datech poznáte a co by to
znamenalo pro člověka, který ji řídí. Nemusí jít o velký objev. Musí to ale být tvrzení, které
doložíte číslem, a nesmí to být převyprávění něčeho, co jste už spočítali výš. Počítejte s jedním
grafem nebo tabulkou, třemi odstavci a kódem, kterým jste se k tomu dostali.

---

## Jak odevzdat

Ke každé otázce odevzdejte výsledek a kód nebo postup, kterým jste se k němu dostali.
U otázek, kde je potřeba něco posoudit, stačí pár vět; podstatné je, aby bylo jasné, na
základě čeho jste se rozhodli.

Dvě věci se hodnotí nad rámec správného čísla. První je, jestli jste si všimli, že data
nejsou čistá, a jestli jste si s tím poradili dřív, než jste začali počítat. Druhá je,
jestli váš výsledek dává smysl – číslo, které vyjde, není totéž co odpověď.
