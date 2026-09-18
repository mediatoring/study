# Analýzy, které vám přistály na stole

## O čem to je

Nastoupili jste do controllingu firmy PAPYRA Industry a.s. a ve složce po předchůdci jste našli
šest hotových analýz z ledna 2027. Každá má pár odstavců, tabulku a doporučení pro vedení. Podle
všeho vznikly rychle a s pomocí AI. Vedení podle nich chce rozhodovat.

Vaším úkolem není napsat je znovu. Máte u každé z nich rozhodnout, jestli závěr platí, a své
rozhodnutí doložit výpočtem z dat. Některé analýzy jsou v pořádku. Některé mají chybu, která
závěr obrací. A aspoň u jedné platí závěr navzdory postupu, kterým k němu autor došel – číslo
sedí, metoda ne.

Analýzy najdete ve složce [analyzy/](analyzy/), soubory `analyza-1.md` až `analyza-6.md`.

## Data

Pracuje se se stejným datasetem jako cvičení **Prodejní data PAPYRA Industry** – řádkový výpis
prodejů za roky 2021 až 2026, jeden řádek je jedna položka na jedné faktuře. Data i stahovací
skript jsou ve složce toho cvičení:
<https://github.com/mediatoring/study/tree/main/exercises/prodeje-papyra>

Tam je i legenda všech sloupců. Než začnete, ověřte si, že máte data načtená správně: čisté tržby
roku 2025, tedy součet sloupce `TRZBY_CZK` za rok 2025 včetně záporných řádků dobropisů, musí
vyjít **399,6 milionu korun**.

Pokud jste předchozí cvičení nedělali, nevadí. Všechno, co potřebujete, je v datech a v legendě
sloupců; jen počítejte s tím, že data nejsou vyčištěná a že to je součást úkolu.

## Co odevzdat

Ke každé z šesti analýz napište:

**Verdikt.** Jedno ze tří: *platí*, *neplatí*, nebo *platí náhodou* – tedy závěr je správný, ale
postup, kterým k němu autor došel, ho nedokazuje.

**Důkaz.** Číslo, které jste spočítali, a jednu větu o tom, jak jste ho spočítali. U analýz, které
neplatí, uveďte i správnou hodnotu toho ukazatele, o který jde.

**Čeho si měl autor všimnout.** Jedna až dvě věty. Ne „udělal chybu", ale co konkrétně v datech
nebo v postupu mělo rozsvítit červenou.

**Co s doporučením.** U analýz, které neplatí, napište, jestli se mění i doporučení pro vedení,
nebo jestli náhodou zůstává v platnosti z jiného důvodu.

Na závěr přidejte jeden odstavec: která z těch chyb by firmu stála nejvíc peněz, kdyby se podle
analýzy rozhodlo, a proč.

## Nepovinná část

Vezměte libovolnou z těch analýz, vložte ji do jazykového modelu, který máte po ruce, a požádejte
ho o kontrolu. Napište, co model našel, co přehlédl a co si vymyslel. Stačí půl stránky. Bezplatná
verze čehokoli na to bohatě stačí a výsledek bývá poučnější než samotné cvičení.

## Jak se to hodnotí

Hodnotí se důkaz, ne verdikt. Napsat „neplatí" se dá i hozením mincí; napsat „neplatí, protože
za tímhle číslem stojí jeden doklad na 178 milionů, bez něj vychází 34,5" se nedá.

Nehledejte chybu za každou cenu. Analytik, který označí za vadné všechno, je stejně nepoužitelný
jako ten, který nezkontroluje nic – a v datech je i práce, která je odvedená správně. Rozeznat
jedno od druhého je celé zadání.
