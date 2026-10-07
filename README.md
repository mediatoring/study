# Study

Materiály pro kurzy a workshopy Mediatoring: datová a analytická cvičení a sada skills pro studium s AI.

## Cvičení

Každé cvičení má vlastní složku se zadáním, data visí u příslušného release.

<!-- cviceni:start -->
| Cvičení | O čem to je | Obtížnost | Data |
|---|---|---|---|
| 1. [Prodejní data PAPYRA Industry](exercises/prodeje-papyra/) | Milion řádků fakturace tak, jak vypadla ze systému. Jednatřicet otázek od prvního součtu po shrnutí pro vedení – a příběh, který si poskládáš sám. | střední | [74.7 MB](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1) |
| 2. [Analýzy, které vám přistály na stole](exercises/analyzy-na-stole/) | Šest hotových analýz nad prodejními daty. Některé sedí, některé ne. Zjisti které a dokaž to. | střední | [74.7 MB](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1) (data cvičení Prodejní data PAPYRA Industry) |
| 3. [Rozhodování z dat](exercises/rozhodovani-z-dat/) | Deset otázek, na které data nemají jedinou správnou odpověď. Vyber ukazatele, obhaj je a rozhodni. | těžká | [74.7 MB](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1) (data cvičení Prodejní data PAPYRA Industry) |
| 4. [Co běžný report neukáže](exercises/co-report-neukaze/) | Čtyři pohledy, které se do měsíčního reportu nevejdou: co se kupuje spolu, kdo platí kolik, na kom visí které výrobky a proč se dva závody nedají srovnat. | těžká | [74.7 MB](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1) (data cvičení Prodejní data PAPYRA Industry) |
| 5. [Řídicí report pro vedení PAPYRA](exercises/ridici-report/) | Firemní výzva: postav z prodejních dat report, podle kterého se dá rozhodovat, a otestuj ho na lidech, kteří data neviděli. | těžká | [74.7 MB](https://github.com/mediatoring/study/releases/tag/prodeje-papyra-v1) (data cvičení Prodejní data PAPYRA Industry) |
<!-- cviceni:end -->

Otevři složku cvičení, přečti `zadani.md` a stáhni data skriptem `stahni_data.py` z té samé složky. Nástroje jsou na tobě – Python, R, SQL, DuckDB, Power BI i Excel, cokoli, čím se dostaneš k výsledku.

## Skills pro studium s AI

Dvanáct hotových skills, které z umělé inteligence udělají tutora a pomocníka, ne tahák. Skill je složka se souborem `SKILL.md` – textový návod, podle kterého AI provede konkrétní úkol pokaždé stejně. Nahrajete ho jednou do Claude, Gemini nebo ChatGPT a dál ho AI použije sama, když se k vašemu dotazu hodí.

| Skill | K čemu je | Stáhnout |
|---|---|---|
| [zkousejici-tutor](skills/zkousejici-tutor/SKILL.md) | Vyzkouší vás před zkouškou z vašich skript nebo slidů, po jedné otázce a bez nápovědy. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zkousejici-tutor.zip) |
| [vysvetli-mi](skills/vysvetli-mi/SKILL.md) | Vysvětlí, čemu nerozumíte, a nechá vás to zopakovat vlastními slovy. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/vysvetli-mi.zip) |
| [cvicna-zkouska](skills/cvicna-zkouska/SKILL.md) | Zkouška nanečisto ve stylu vašeho předmětu, s limitem, bodováním a slabými tématy. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/cvicna-zkouska.zip) |
| [karticky](skills/karticky/SKILL.md) | Z vašich podkladů udělá kartičky k importu do Anki nebo Quizletu. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/karticky.zip) |
| [plan-zkouskoveho](skills/plan-zkouskoveho/SKILL.md) | Plán učení den po dni podle termínů a času, který opravdu máte. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/plan-zkouskoveho.zip) |
| [poznamky-z-prednasky](skills/poznamky-z-prednasky/SKILL.md) | Z poznámek a slidů udělá přehled pojmů a ukáže, co v nich chybí. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/poznamky-z-prednasky.zip) |
| [zpetna-vazba](skills/zpetna-vazba/SKILL.md) | Zhodnotí váš text jako přísný oponent. Nepřepisuje, radí. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zpetna-vazba.zip) |
| [rozporovac](skills/rozporovac/SKILL.md) | Hraje oponenta a hledá slabá místa v tezi, otázce nebo plánu. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/rozporovac.zip) |
| [citace-iso690](skills/citace-iso690/SKILL.md) | Ověří, že zdroje existují, a naformátuje je podle ČSN ISO 690. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/citace-iso690.zip) |
| [humanizator](skills/humanizator/SKILL.md) | Upraví váš text, aby nezněl strojově – česky i anglicky. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/humanizator.zip) |
| [lanyze](skills/lanyze/SKILL.md) | Pravidlo pro přepis po připomínkách, který nenese stopu po vyřazeném. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/lanyze.zip) |
| [pohovor-nanecisto](skills/pohovor-nanecisto/SKILL.md) | Pracovní pohovor podle konkrétního inzerátu, se zpětnou vazbou. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/pohovor-nanecisto.zip) |

Podrobnosti najdete ve [složce skills](skills/): kde skills fungují, jak je nainstalovat v Claude, Gemini a ChatGPT, co si ověřit před instalací a jak je sladit s pravidly školy. Je tam i [anglická verze](skills/README.en.md).

## Licence

Zadání, data i skills jsou k dispozici pod [CC BY 4.0](LICENSE). Data jsou syntetická, žádný reálný subjekt za nimi nestojí.

## Autor

Michal Kubíček · [kubicek.ai](https://kubicek.ai) · [aiedu.cz](https://aiedu.cz)

Nápady a připomínky posílejte přes [Issues](https://github.com/mediatoring/study/issues).

---

Aktualizováno 2026-10-03

<!-- Tabulku cvičení generuje nástroj publish_exercise.py, needituj ji ručně. Ostatní části README jsou psané ručně. -->
