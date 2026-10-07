# Řídicí report pro vedení PAPYRA

## Zadání výzvy

Vedení společnosti PAPYRA Industry a.s. se rozhoduje podle měsíčních tabulek, které nikdo nečte,
a podle dojmů z obchodních schůzek. Dostali jste šest let fakturačních dat a úkol: postavit report,
podle kterého se dá rozhodovat, a dokázat, že to funguje.

Výstupem není dokument s odpověďmi. Výstupem je **funkční prototyp reportu, který jste otestovali
na lidech**. Nástroj je na vás – Power BI, Looker Studio, vlastní webová aplikace, notebook
s grafy, cokoli, co dokážete ukázat a předat.

Výzva se řeší individuálně nebo v týmu do tří lidí, je za 25 bodů a odevzdává se do 13. prosince.
Na kolokviu ji obhajujete jako pitch pro vedení firmy, který končí konkrétní žádostí.

Počítejte zhruba s dvaceti hodinami práce.

## Pro koho report stavíte

Report čtou tři lidé. Žádný z nich neotevře tabulku s milionem řádků a žádný nebude nic
dopočítávat.

**Vít Hanousek, generální ředitel.** Ve firmě dvanáct let, z toho pět ve vedení. Tržby se podle
něj „drží", marže podle controllingu roste a on má na jaře jednat s vlastníkem o investici do
nové linky. Potřebuje vědět, jestli je firma dnes v lepší kondici než před pěti lety, a umět to
říct třemi větami. Na report se podívá jednou měsíčně, vždy před poradou, a dá mu deset minut.

**Lenka Sýkorová, obchodní ředitelka.** Řídí sedm obchodníků a rozděluje jejich čas. Ví, že pár
odběratelů dělá většinu obratu, ale nemá přehled o tom, komu se věnovat přednostně a kdo naopak
tiše odchází. Číslům, která si neumí sama přepočítat, nevěří; když jí report ukáže žebříček,
bude chtít vědět, podle čeho je seřazený.

**Tomáš Jelínek, finanční ředitel.** Hlídá cashflow a bankovní kovenanty. Zajímá ho, co se stane
s výsledkem, když odejde největší odběratel, a jestli sezónní výkyvy neohrozí splátky. Zná pojem
marže ve třech různých významech a bude se ptát, který z nich report používá.

Kdo report čte a co potřebuje rozhodnout, je první fází vaší práce. Vedení je fiktivní, takže
s ním rozhovory dělat nebudete – vyjděte z popisu výše a z toho, co se dá odvodit z dat.

## Co odevzdáte

**1. Přípravu dat.** Doložte, že máte data načtená správně: čisté tržby roku 2025, tedy součet
sloupce `TRZBY_CZK` za rok 2025 včetně záporných řádků dobropisů, musí vyjít **399,6 milionu
korun**. Popište, co jste z dat vyřadili nebo opravili a proč. Data nejsou připravená k analýze
a to, jak si s tím poradíte, je součástí hodnocení.

**2. Report.** Musí být srozumitelný pro člověka, který dataset nikdy neviděl a nebude si k němu
nic dohledávat. Hodnotí se i vizuální zpracování: co je vidět na první obrazovce, jestli grafy
odpovídají typu dat a jestli se v reportu dá najít odpověď, aniž by k tomu byl potřeba návod.

**3. Napojení na rozhodnutí.** Report musí unést tři povinná rozhodnutí, která najdete níž,
a jednu až dvě další úlohy z cvičení *Rozhodování z dat* podle vlastního výběru. U každého
rozhodnutí napište, který pohled v reportu ho podporuje, co z něj plyne a co se z dat zjistit
nedá.

**4. Test.** Dejte report jednomu až dvěma lidem, kteří data neviděli, spolu s rozhodovacími
otázkami. Zapište, jestli podle reportu dokázali rozhodnout, kde se zasekli, co jste po jejich
reakci změnili a jak to dopadlo. Test bez zaznamenané změny není test.

K dokumentu podle šablony předmětu přiložte odkaz na report nebo exportovaný soubor a skript či
popis postupu, kterým jste data připravili.

## Povinná rozhodnutí

### Rozhodnutí 1: Je firma v roce 2026 zdravější než v roce 2021?

Navrhněte nejvýš pět ukazatelů, podle kterých jde z těchto dat posoudit obchodní zdraví firmy,
a porovnejte podle nich oba roky. U každého ukazatele napište, proč jste ho vybrali, co ukazuje
a jestli se situace zlepšila, zhoršila, nebo zůstala stejná.

Pozor na slovo marže. Dataset umožňuje počítat ziskovost nejméně třemi způsoby a ne všechny
vyprávějí o roce 2026 totéž. Vyberte si jeden, řekněte proč, a držte se ho v celém reportu.

Na závěr napište nejvýš tři věty, které byste řekli generálnímu řediteli.

### Rozhodnutí 2: Čí odchod by firmu bolel nejvíc?

Jeden odběratel od ledna 2027 přestane nakupovat. Najděte toho, jehož odchod by měl podle dat
největší ekonomický dopad. Nemusí to být ten s nejvyššími tržbami.

Vyčíslete ztracené tržby, ztracenou marži a podíl na výsledku firmy. Napište také, co o skutečném
dopadu jeho odchodu z těchto dat zjistit nedokážete.

### Rozhodnutí 3: Které zákazníky firma možná ztrácí?

Nejdřív napište definici ohroženého zákazníka, teprve potom podle ní hledejte. Může jít
o klesající nákupy, o dlouhou dobu od posledního nákupu, o klesající frekvenci objednávek nebo
o kombinaci.

Odevzdejte seznam nejméně deseti odběratelů, které by měl obchod prověřit, u každého důvod,
a k tomu jednu větu o tom, jak by se ten seznam změnil, kdybyste definici postavili jinak.

### Volitelné úlohy

K povinné trojici přidejte jednu až dvě další úlohy z cvičení
[Rozhodování z dat](../rozhodovani-z-dat/). Povinná rozhodnutí 1, 2 a 3 z tohohle zadání
odpovídají úlohám 1, 3 a 4 toho cvičení, takže vybírejte z ostatních – číslování se mezi oběma
dokumenty nekryje. Vyberte si takové, které váš report skutečně unese.

Na pitch se navíc hodí úloha 10, tedy najít pravdivé číslo, kterým se dá vedení oklamat. Povinná
není, ale obhajoba, ve které ukážete, že váš report takovému číslu nenaletí, stojí o patro výš.

## Data

Pracuje se s datasetem cvičení **Prodejní data PAPYRA Industry** – řádkový výpis prodejů za roky
2021 až 2026, jeden řádek je jedna položka na jedné faktuře. Stáhnete ho skriptem
`stahni_data.py`, který leží ve stejné složce jako toto zadání:

```bash
python3 stahni_data.py
```

Legendu všech sloupců najdete v zadání toho cvičení:
<https://github.com/mediatoring/study/tree/main/exercises/prodeje-papyra>

## Jak se to hodnotí

Report se hodnotí podle toho, jestli podle něj dokáže rozhodnout někdo jiný než jeho autor. To je
taky důvod, proč je test povinnou součástí odevzdání: dokud report neviděl nikdo zvenčí, nevíte
o něm nic.

Dál se hodnotí, jestli je příprava dat doložená a obhajitelná, jestli zvolené ukazatele odpovídají
otázkám, na které mají odpovídat, a jestli u každého rozhodnutí umíte říct, co z dat neplyne.
Odpověď „data to neřeknou" je při správném zdůvodnění plnohodnotná odpověď.

Pitch na kolokviu není shrnutí toho, co jste udělali. Je to prodej řešení někomu, kdo o něm
rozhoduje, a končí konkrétní žádostí – o nasazení, o čas lidí, o rozpočet.

Správně provedený výpočet může vést ke špatnému rozhodnutí. Špatně zvolený ukazatel se dá
spočítat naprosto přesně. A přesvědčivý graf nemusí dokazovat to, co o něm jeho autor tvrdí.
Report, který tyhle tři věci ošetří, je dobrý report.
