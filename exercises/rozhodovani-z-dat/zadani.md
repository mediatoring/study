# Rozhodování z dat

## O čem to je

V předchozích cvičeních jste dostali konkrétní otázky a hledali na ně odpovědi, případně jste
ověřovali cizí závěry. Tady je situace blíž skutečné práci analytika: vedení má problém a
potřebuje se rozhodnout, ale není předem jasné, který ukazatel je ten správný, jak data agregovat
ani co přesně znamená dobrý zákazník nebo rizikový vývoj.

U každé úlohy proto nejde jen o výpočet. Musíte rozhodnout, jaké ukazatele použijete, výpočet
provést, ověřit, že výsledek není způsoben chybou nebo zvláštností dat, vyložit, co znamená pro
firmu, a navrhnout rozhodnutí nebo další postup. U většiny úloh existuje víc obhajitelných
odpovědí. Hodnotí se, jestli je vaše obhajitelná.

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

Data nejsou připravená k analýze. Obsahují duplicity, dobropisy, mimořádné hodnoty a další jevy,
které dokážou výsledek obrátit. Ošetřit je je součástí každé úlohy, ne samostatný úkol.

---

# Úlohy

## A. Firma jako celek

**1. Je firma v roce 2026 zdravější než v roce 2021?**

Navrhněte nejvýš pět ukazatelů, podle kterých jde z těchto dat posoudit obchodní zdraví firmy,
a porovnejte podle nich oba roky. U každého ukazatele napište, proč jste ho vybrali, co ukazuje
a jestli se situace zlepšila, zhoršila, nebo zůstala stejná.

Pozor na slovo marže. Dataset umožňuje počítat ziskovost nejméně třemi způsoby a ne všechny
vyprávějí o roce 2026 totéž. Vyberte si jeden, řekněte proč, a držte se ho v celém cvičení.

Na závěr napište nejvýš tři věty, které byste řekli generálnímu řediteli.

**2. Čím se zlepšila marže?**

Hrubá marže firmy se mezi lety 2021 a 2026 výrazně zlepšila. Rozhodněte, kolik z toho zlepšení
udělalo to, že se zlepšila marže uvnitř jednotlivých produktových skupin, a kolik to, že se
změnila skladba prodeje mezi skupinami.

Rozklad proveďte na úrovni `PS1_SKUPINA` a ukažte, že se složky sečtou na celkovou změnu.
Výsledek okomentujte jednou větou pro vedení: zlepšila se firma, nebo jen prodává něco jiného?

## B. Zákazníci

**3. Čí odchod by firmu bolel nejvíc?**

Jeden odběratel od ledna 2027 přestane nakupovat. Najděte toho, jehož odchod by měl podle dat
největší ekonomický dopad. Nemusí to být ten s nejvyššími tržbami.

Vyčíslete ztracené tržby, ztracenou marži a podíl na výsledku firmy. Napište také, co o skutečném
dopadu jeho odchodu z těchto dat zjistit nedokážete.

**4. Které zákazníky firma možná ztrácí?**

Nejdřív napište definici ohroženého zákazníka, teprve potom podle ní hledejte. Může jít
o klesající nákupy, o dlouhou dobu od posledního nákupu, o klesající frekvenci objednávek nebo
o kombinaci.

Odevzdejte seznam nejméně deseti odběratelů, které by měl obchod prověřit, u každého důvod,
a k tomu jednu větu o tom, jak by se ten seznam změnil, kdybyste definici postavili jinak.

**5. Kdo je nový zákazník?**

Porovnejte zákazníky, kteří jsou s firmou dlouho, s těmi, kteří přibyli nedávno. Zjistíte, že
samotné slovo nový potřebuje definici, a že podle toho, kterou zvolíte, dostanete výrazně jinou
skupinu i jiný závěr.

Vyberte si definici, sestavte skupiny a porovnejte jejich velikost, marži a nákupní aktivitu.
Rozhodněte, jestli firma novými zákazníky kvalitativně nahrazuje ty, kteří odcházejí.

## C. Čas a změna

**6. Najděte strukturální změnu**

Najděte v období 2021 až 2026 okamžik, kdy se nějaká důležitá část podnikání začala chovat jinak
než předtím, a nevrátila se. Nejde o jeden mimořádný měsíc.

Ukažte, jak to vypadalo před změnou, kdy k ní přibližně došlo a jak to vypadá potom. Navrhněte
vysvětlení a jasně oddělte, co dokazují data a co je vaše hypotéza.

**7. Sezónnost není jedna**

Celkové tržby mají sezónní profil. To neznamená, že ho mají všechny části firmy stejný.

Porovnejte sezónnost aspoň tří vhodně zvolených skupin a najděte případ, kdy celofiremní průměr
skrývá výrazně odlišné chování jedné z nich. Vysvětlete, proč na tom záleží při plánování výroby.

## D. Předpověď bez budoucích dat

**8. Kdo u nás nakoupí i příští rok?**

Je 31. prosince 2026 a máte odhadnout, kteří odběratelé budou aktivní i v roce 2027. Data za rok
2027 nemáte, takže si postavte historický experiment: použijte data do konce roku 2025 a ověřte
předpověď na roce 2026.

Můžete použít jednoduché pravidlo, skóre i model. Složitější řešení není automaticky lepší.
Vyhodnoťte ho na období, které při tvorbě nevidělo.

**9. Model má přesnost 90 procent. Je dobrý?**

Výsledek předchozí úlohy popište dvakrát. Technicky – přesnost, přesnost kladné předpovědi,
úplnost, matice záměn. A obchodně: obchodníci mají kapacitu obvolat dvacet odběratelů, které mají
obvolat a proč.

Nejdřív ale spočítejte, jaké přesnosti dosáhne pravidlo „zůstanou všichni". Teprve proti němu má
smysl cokoli poměřovat.

## E. Závěr

**10. Najděte pravdivé číslo, kterým se dá vedení oklamat**

Najděte v datech číslo, které je spočítané správně, a přesto by z něj šlo vyvodit výrazně
zavádějící závěr. Číslo nesmíte zfalšovat.

Ukažte zavádějící tvrzení, číslo, které ho zdánlivě podporuje, informaci, která ho staví do jiného
světla, a korektnější výklad. Nesmí jít o opakování něčeho, co jste počítali v úlohách výš.

---

## Jak odevzdat

U každé úlohy odevzdejte výsledek, číslo nebo tabulku, ze které vychází, postup či kód, a jednu
až dvě věty o tom, co to znamená pro firmu.

Tam, kde neexistuje jediná správná metoda, se hodnotí, jestli zvolený postup odpovídá otázce,
jestli rozumíte významu použitých ukazatelů, jestli kontrolujete kvalitu dat a jestli rozlišujete
mezi tím, co data dokazují, a tím, co jen naznačují.

Správně provedený výpočet může vést ke špatnému rozhodnutí. Špatně zvolený ukazatel se dá spočítat
naprosto přesně. A přesvědčivý graf nemusí dokazovat to, co o něm jeho autor tvrdí. Rozeznat tyhle
situace je cílem celého cvičení.
