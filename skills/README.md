# Skills pro studium s AI

**Česky** · [English](README.en.md)

Dvanáct hotových skills, které z umělé inteligence udělají tutora a pomocníka, ne tahák. Stáhnete, nahrajete do Claude, Gemini nebo ChatGPT a můžete se učit.

Tato složka je součástí repozitáře [mediatoring/study](../README.md), kde najdete i datová a analytická cvičení.

## Co je skill

Skill je složka se souborem `SKILL.md`: textový návod, podle kterého AI provede konkrétní úkol pokaždé stejně. Místo toho, abyste do chatu znovu a znovu vkládali dlouhý prompt, nahrajete skill jednou. AI ho pak použije sama, když se k vašemu dotazu hodí, nebo si ho zavoláte jménem. Formát je otevřený standard Agent Skills, takže stejný soubor funguje v Claude, Gemini i ChatGPT.

Sada vznikla k přednášce „AI jako tahák, pomocník nebo tutor“ na Festivalu příležitostí 2026 (OPF Slezské univerzity v Karviné). Všechny skills spojuje jedna myšlenka: AI se ptá, opravuje a vysvětluje, ale odpověď musí vzniknout ve vaší hlavě.

## Sada

### Učení

| Skill | K čemu je | Stáhnout |
|---|---|---|
| [zkousejici-tutor](zkousejici-tutor/SKILL.md) | Vyzkouší vás před zkouškou z vašich skript nebo slidů. Klade po jedné otázce, neprozradí odpověď, dokud to nezkusíte, a postupně přitvrzuje. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zkousejici-tutor.zip) |
| [vysvetli-mi](vysvetli-mi/SKILL.md) | Vysvětlí, čemu nerozumíte – od příkladu ze života k definici – a nechá vás látku zopakovat vlastními slovy. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/vysvetli-mi.zip) |
| [cvicna-zkouska](cvicna-zkouska/SKILL.md) | Zkouška nanečisto ve stylu vašeho předmětu, s časovým limitem a bodováním. Vyhodnotí ji až po odevzdání a ukáže slabá témata. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/cvicna-zkouska.zip) |
| [karticky](karticky/SKILL.md) | Z vašich podkladů udělá kartičky, které nutí vysvětlovat, ne jen opakovat, a připraví je k importu do Anki nebo Quizletu. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/karticky.zip) |
| [plan-zkouskoveho](plan-zkouskoveho/SKILL.md) | Realistický plán učení den po dni podle termínů a času, který opravdu máte. Nejslabší témata dopředu, s rezervou a cvičnou zkouškou. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/plan-zkouskoveho.zip) |
| [poznamky-z-prednasky](poznamky-z-prednasky/SKILL.md) | Z poznámek a slidů udělá přehled pojmů, ukáže, co vám v poznámkách chybí, a přidá kontrolní otázky. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/poznamky-z-prednasky.zip) |

### Psaní a práce

| Skill | K čemu je | Stáhnout |
|---|---|---|
| [zpetna-vazba](zpetna-vazba/SKILL.md) | Zhodnotí váš text jako přísný oponent – argumentaci, zdroje, strukturu i splnění zadání. Nepřepisuje, řekne, která úprava přinese nejvíc. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zpetna-vazba.zip) |
| [rozporovac](rozporovac/SKILL.md) | Hraje oponenta: vyslýchá vás a hledá slabá místa v tezi, výzkumné otázce nebo plánu, dokud je neobhájíte. Příprava na obhajobu. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/rozporovac.zip) |
| [citace-iso690](citace-iso690/SKILL.md) | Nejdřív ověří, že zdroje existují, pak je naformátuje podle ČSN ISO 690. Neexistující zdroje označí, nic nedoplňuje odhadem. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/citace-iso690.zip) |
| [humanizator](humanizator/SKILL.md) | Upraví váš text, aby nezněl strojově – česky i anglicky, včetně kalků a úředního trpného rodu. Zachová význam a nic nevymýšlí. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/humanizator.zip) |
| [lanyze](lanyze/SKILL.md) | Pravidlo pro přepis po připomínkách: změní jen to, čeho se připomínka týká, a ve výsledku nezůstane stopa po tom, co se vyřadilo. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/lanyze.zip) |
| [pohovor-nanecisto](pohovor-nanecisto/SKILL.md) | Pracovní pohovor podle konkrétního inzerátu. AI hraje personalistu a po každé odpovědi řekne, co zlepšit. Funguje i hlasem. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/pohovor-nanecisto.zip) |

Humanizátor je editor stylu pro text, za kterým stojíte – vlastní koncept nebo text psaný s pomocí AI, kterou přiznáváte. Detektory AI neobchází a použití AI se ve studijních pracích přiznává i tak.

## Kde skills fungují

Stav k září 2026. Nabídky se rychle mění, proto si dostupnost ověřte ve svém účtu.

**Claude** podporuje skills na všech tarifech včetně bezplatného. V nastavení musí být zapnuté spouštění kódu a tvorba souborů.

**Gemini** podporuje skills na osobních účtech Google pro uživatele od 18 let. Nahrát skill jde zatím na webu gemini.google.com a v aplikaci Gemini pro Mac, ne v telefonu. Dosavadní Gems se od 17. 11. 2026 automaticky mění na skills.

**ChatGPT** zatím nabízí skills jen v tarifech Business, Enterprise a Edu, v bezplatné verzi ani v Plus ne.

Skills podporují také nástroje pro vývojáře: Claude Code, OpenAI Codex, Gemini CLI, Cursor, VS Code a GitHub Copilot.

## Instalace

Nejdřív si stáhněte ZIP skillu z tabulky výše. ZIP nerozbalujte, platformy ho načtou celý.

**Claude:** Na claude.ai otevřete Nastavení a v části Capabilities zapněte „Code execution and file creation“. Pak v nabídce Customize otevřete Skills a nahrajte ZIP. Hotovo – napište třeba „Vyzkoušej mě z mikroekonomie“ a Claude skill použije sám.

**Gemini:** Na gemini.google.com (nebo v aplikaci pro Mac) otevřete stránku Skills a zvolte nahrání souboru. Vyberte ZIP nebo samotný `SKILL.md`. V chatu pak skill vyvoláte lomítkem a jeho názvem, případně ho Gemini použije samo.

**ChatGPT (Business, Enterprise, Edu):** Otevřete Skills, zvolte Create a Upload from your computer a nahrajte ZIP. V chatu skill zavoláte zmínkou @ a názvem.

Názvy položek v menu se mohou měnit. Když některou nenajdete, hledejte v nastavení slovo „Skills“.

## Než skill nainstalujete

Skill je obyčejný text. Otevřete si `SKILL.md` a přečtěte si, co přesně AI říká – tohle platí pro každý skill, který najdete na internetu. Instalujte jen skills, kterým rozumíte a jejichž zdroji věříte. Do AI nevkládejte osobní údaje, své ani cizí.

## Skills a pravidla školy

Tyto skills vám mají pomáhat se učit, ne odevzdávat práci za vás. Použití AI ve studijních pracích přiznejte podle pravidel své školy (na Slezské univerzitě Pokyn rektora č. 4/2025) a u konkrétního předmětu se řiďte tím, co určí vyučující.

## Vlastní úpravy

Skills si klidně upravte: dopište svůj předmět, obtížnost nebo tón. Dvě věci zachovejte, jinak skill nepůjde nahrát. Pole `name` musí být malými písmeny se spojovníky a shodovat se s názvem složky. Pole `description` říká, co skill dělá a kdy ho použít – podle něj AI pozná, že ho má zapnout.

Pokud chcete ZIPy sestavit sami, spusťte `scripts/build_skills.sh`.

## Inspirace

Humanizátor vychází ze stránky Wikipedie „Signs of AI writing“ a ze skillu [humanizer](https://github.com/blader/humanizer), doplněného o vzorce specifické pro češtinu. Rozporovač je inspirovaný skillem grill-me z kolekce Matta Pococka.

## Autor

Michal Kubíček, AI výzkumník · [kubicek.ai](https://kubicek.ai) · [aiedu.cz](https://aiedu.cz)

Nápady a připomínky posílejte přes [Issues](https://github.com/mediatoring/study/issues).

## Licence

[CC BY 4.0](../LICENSE) – skills můžete volně používat, upravovat a sdílet, pokud uvedete autora.
