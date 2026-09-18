# Co běžný report neukáže

## O čem to je

Měsíční report firmy PAPYRA Industry a.s. má tržby, marži, žebříček zákazníků a srovnání
s minulým rokem. To všechno jsou pohledy shora dolů: vezmi celek a rozděl ho.

Tohle cvičení jde jinudy. Čtyři úlohy, z nichž každá se dívá na vztah mezi dvěma věcmi, které
report drží odděleně – co se prodává spolu s čím, kdo platí za stejnou věc kolik, na kom visí
který výrobek a co se stane, když se do jedné tabulky dostanou dvě různé činnosti. Každá z nich
potřebuje jinou techniku a v každé je něco, co se z agregovaných čísel nedá uvidět.

Úlohy jsou nezávislé, dají se dělat v libovolném pořadí.

## Data

Pracuje se se stejným datasetem jako cvičení **Prodejní data PAPYRA Industry** – řádkový výpis
prodejů za roky 2021 až 2026, jeden řádek je jedna položka na jedné faktuře. Stáhnete ho skriptem
`stahni_data.py`, který leží ve stejné složce jako toto zadání:

```bash
python3 stahni_data.py
```

Legendu všech sloupců najdete v zadání toho cvičení:
<https://github.com/mediatoring/study/tree/main/exercises/prodeje-papyra>

Než začnete, ověřte si, že máte data načtená správně: čisté tržby roku 2025, tedy součet sloupce
`TRZBY_CZK` za rok 2025 včetně záporných řádků dobropisů, musí vyjít **399,6 milionu korun**.

Data nejsou připravená k analýze. Ošetření duplicit, dobropisů a mimořádných hodnot je součástí
každé úlohy.

---

# Úlohy

## 1. Co zákazníci nakupují společně?

Jedna faktura obvykle obsahuje víc položek. Využijte tu strukturu a zjistěte, které produktové
skupiny zákazníci nakupují společně častěji, než by odpovídalo náhodě.

Začněte na úrovni `PS1_SKUPINA`, tedy nejhrubšího dělení sortimentu. Pokud budete chtít,
pokračujte na konkrétní položky – tam ale narazíte na to, že dvojic je řádově víc a většina se
vyskytne jen několikrát.

Použijte ukazatele nákupního košíku: support, confidence a lift. Pozor, nejčastější dvojice nemusí
být nejzajímavější: dvě skupiny, které se prodávají skoro všude, se budou potkávat často jen proto,
že jsou obě všude.

**Odevzdejte** pět nejsilnějších nebo obchodně nejzajímavějších vztahů i s jejich support,
confidence a liftem. K jednomu konkrétnímu výsledku vysvětlete rozdíl mezi těmi třemi ukazateli
tak, aby tomu rozuměl obchodní ředitel. Najděte dvojici, která vypadá zajímavě podle support nebo
confidence, ale po výpočtu liftu zajímavá není. A navrhněte aspoň dvě věci, které by firma
s výsledkem mohla udělat.

Dejte pozor na faktury s mimořádně velkým počtem řádků a napište, jak jste s nimi naložili.

## 2. Které výrobky existují prakticky jen pro jednoho zákazníka?

Firma sleduje koncentraci tržeb podle zákazníků. Méně viditelné riziko je opačné: některé výrobky
mohou být skoro úplně závislé na jediném odběrateli.

Zjistěte, jak je u jednotlivých položek prodej rozložený mezi zákazníky, a navrhněte způsob, jak
odlišit běžně distribuovaný sortiment od výrobků závislých na několika odběratelích a od těch,
které se fakticky vyrábějí pro jednoho.

Počet zákazníků sám o sobě nestačí. Položka s jedním odběratelem a ročním obratem pět tisíc korun
je něco jiného než položka s jedním odběratelem a obratem několik milionů.

**Odevzdejte** metriku, kterou závislost měříte, přehled nejvýznamnějších koncentrovaných položek
s jejich tržbami, marží a počtem zákazníků, u těch největších i jméno odběratele, na kterém visí,
a vyčíslení, jak velká část podnikání firmy na takto koncentrovaný sortiment připadá.

Na závěr odpovězte a doložte daty: je pro firmu rizikovější zákazník, který odebírá hodně
standardních výrobků, nebo zákazník, pro kterého firma vyrábí několik téměř výhradních položek?

## 3. Proč různí zákazníci platí za stejný výrobek jinou cenu?

Vyberte položky, které se v roce 2026 prodávaly dost různým zákazníkům na to, aby se dalo
srovnávat, a porovnejte skutečně dosaženou cenu za jednotku mezi odběrateli.

Samotné zjištění, že dva zákazníci platí jinak, nestačí. Zkuste zjistit, s čím rozdíl souvisí –
s odebraným množstvím, segmentem, zemí, měnou, velikostí zákazníka, četností nákupů nebo s něčím
jiným, co v datech je.

Pozor na drobné odběry. Rozdíl mezi jedním kusem a deseti tisíci kusů má obvykle legitimní důvod.

**Odevzdejte** pravidlo, podle kterého jste vybrali dost významné položky, metriku cenového
rozpětí a její zdůvodnění, pět položek s nejzajímavější cenovou strukturou a u každé to, co
rozdíl pravděpodobně způsobuje. Najděte aspoň jeden případ, který podle dat stojí za prověření
obchodním oddělením.

Na konec oddělte, co jste z dat skutečně zjistili, a co by vyžadovalo znát obchodní smlouvy.

## 4. Je závod B opravdu horší než závod A?

Vedení dostalo jednoduché srovnání obou závodů a zarazil ho rozdíl v tržbách, množství i marži.
Má z těch čísel plynout, že jeden ze závodů funguje podstatně hůř?

Projděte oba závody v letech 2021 až 2026. Nezůstávejte u tržeb a procentní marže; podívejte se,
co se v každém z nich vlastně prodává a jak vypadá typická faktura a typická položka.

**Odevzdejte** charakteristiku obchodního modelu obou závodů, seznam ukazatelů, které mezi nimi
jde smysluplně porovnat, a seznam těch, u kterých by přímé porovnání bylo zavádějící, vždy
s vysvětlením proč. Vysvětlete nejvýraznější rozdíly a odpovězte, jestli tahle data vůbec stačí
na rozhodnutí o ekonomické výkonnosti obou závodů. Pokud ne, napište přesně, co byste potřebovali.

Cílem není najít lepší závod. Cílem je zjistit, jestli srovnávaná čísla měří srovnatelnou činnost.

---

## Jak odevzdat

U každé úlohy odevzdejte výsledek, čísla nebo tabulku, ze kterých vychází, postup či kód a jednu
až dvě věty o tom, co to znamená pro firmu.

Hodnotí se, jestli zvolená metrika odpovídá otázce, jestli jste ověřili, že výsledek nestojí na
jednom dokladu nebo jedné faktuře, a jestli poznáte rozdíl mezi číslem, které něco měří, a číslem,
které jen vypadá, že něco měří.
