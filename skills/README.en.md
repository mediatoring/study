# Skills for studying with AI

[Česky](README.md) · **English**

Twelve ready-made skills that turn AI into a tutor and an assistant, not a cheat sheet. Download them, upload them to Claude, Gemini or ChatGPT, and start learning.

This folder is part of the [mediatoring/study](../README.md) repository, which also holds data and analytics exercises.

## What is a skill

A skill is a folder with a `SKILL.md` file: a plain-text playbook that tells the AI how to handle a specific task the same way every time. Instead of pasting a long prompt into every chat, you upload the skill once. The AI then uses it on its own whenever it fits your request, or you call it by name. The format is the open Agent Skills standard, so the same file works in Claude, Gemini and ChatGPT.

The set was created for the talk “AI as a cheat sheet, an assistant or a tutor” at Festival příležitostí 2026 (School of Business Administration, Silesian University in Karviná, Czech Republic). All the skills share one idea: the AI asks, corrects and explains, but the answer has to come from your own head.

## The set

The instructions are written in Czech, but every skill replies in the language you write in.

### Learning

| Skill | What it does | Download |
|---|---|---|
| [zkousejici-tutor](zkousejici-tutor/SKILL.md) | Exam tutor. Quizzes you from your own course materials one question at a time, never reveals the answer before you try, and raises the difficulty as you go. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zkousejici-tutor.zip) |
| [vysvetli-mi](vysvetli-mi/SKILL.md) | Explains what you don't understand – from an everyday example to the formal definition – then asks you to explain it back in your own words. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/vysvetli-mi.zip) |
| [cvicna-zkouska](cvicna-zkouska/SKILL.md) | Mock exam in the style of your course, with a time limit and scoring. Graded only after you submit, with a breakdown of weak topics. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/cvicna-zkouska.zip) |
| [karticky](karticky/SKILL.md) | Turns your materials into flashcards that make you explain, not just recite, ready to import into Anki or Quizlet. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/karticky.zip) |
| [plan-zkouskoveho](plan-zkouskoveho/SKILL.md) | A realistic day-by-day study plan built around your exam dates and the time you actually have. Weakest topics first, with buffer days and a mock exam. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/plan-zkouskoveho.zip) |
| [poznamky-z-prednasky](poznamky-z-prednasky/SKILL.md) | Turns your lecture notes and slides into a list of key concepts, shows what your notes are missing, and adds review questions. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/poznamky-z-prednasky.zip) |

### Writing and work

| Skill | What it does | Download |
|---|---|---|
| [zpetna-vazba](zpetna-vazba/SKILL.md) | Critiques your draft like a strict examiner – argument, sources, structure and fit to the assignment. Doesn't rewrite; tells you which one change will gain the most. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/zpetna-vazba.zip) |
| [rozporovac](rozporovac/SKILL.md) | Plays devil's advocate: grills you and probes your thesis, research question or plan for weak spots until you defend them. Good prep for a thesis defence. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/rozporovac.zip) |
| [citace-iso690](citace-iso690/SKILL.md) | Checks that your sources actually exist, then formats them according to ISO 690 (the Czech ČSN ISO 690 variant). Flags anything it cannot verify and never guesses missing data. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/citace-iso690.zip) |
| [humanizator](humanizator/SKILL.md) | Edits your text so it doesn't sound machine-made – in Czech and English, including calques and bureaucratic passive voice. Keeps the meaning and invents nothing. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/humanizator.zip) |
| [lanyze](lanyze/SKILL.md) | The “truffles” rule for revising after feedback: changes only what the feedback was about and leaves no trace of anything that was removed. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/lanyze.zip) |
| [pohovor-nanecisto](pohovor-nanecisto/SKILL.md) | Mock job interview based on a real job ad. The AI plays the recruiter and gives feedback after each answer. Works in voice mode too. | [ZIP](https://github.com/mediatoring/study/releases/download/skills-v1/pohovor-nanecisto.zip) |

The humanizer is a style editor for text you stand behind – your own draft, or text written with AI help that you disclose. It does not defeat AI detectors, and AI use in coursework still has to be disclosed.

## Where skills work

As of September 2026. Offers change fast, so check what your account includes.

**Claude** supports skills on all plans, including the free one. Code execution and file creation must be turned on in settings.

**Gemini** supports skills on personal Google accounts for users aged 18 and over. For now you can upload a skill on the web at gemini.google.com and in the Gemini app for Mac, not on your phone. Existing Gems are being converted to skills automatically from 17 November 2026.

**ChatGPT** currently offers skills only on the Business, Enterprise and Edu plans, not on Free or Plus.

Developer tools support skills as well, including Claude Code, OpenAI Codex, Gemini CLI, Cursor, VS Code and GitHub Copilot.

## Installation

First download the skill's ZIP from the table above. Don't unzip it – the platforms read the whole package.

**Claude:** On claude.ai open Settings and under Capabilities turn on “Code execution and file creation”. Then go to Customize, open Skills and upload the ZIP. That's it – write something like “Quiz me on microeconomics” and Claude will pick up the skill on its own.

**Gemini:** On gemini.google.com (or in the Mac app) open the Skills page and choose to upload a file. Select the ZIP or the `SKILL.md` file itself. In a chat, call the skill with a slash and its name, or let Gemini use it automatically.

**ChatGPT (Business, Enterprise, Edu):** Open Skills, choose Create and then Upload from your computer, and upload the ZIP. In a chat, call the skill with @ and its name.

Menu labels may change. If you can't find one, look for “Skills” in the settings.

## Before you install a skill

A skill is plain text. Open `SKILL.md` and read exactly what it tells the AI – this goes for any skill you find online. Only install skills you understand, from sources you trust. Don't put personal data into AI, neither yours nor anyone else's.

## Skills and academic rules

These skills are meant to help you learn, not to hand in work for you. Disclose your use of AI in coursework according to your school's rules and follow what your teacher sets for each course.

## Customising

Feel free to adapt the skills: add your course, difficulty or tone. Keep two things intact or the upload will fail. The `name` field must be lowercase with hyphens and match the folder name. The `description` field says what the skill does and when to use it – that is how the AI knows when to switch it on.

To upload an edited skill, zip its folder – the folder named after the skill has to sit at the top level of the archive.

## Credits

The humanizer builds on Wikipedia's “Signs of AI writing” page and the [humanizer](https://github.com/blader/humanizer) skill, extended with patterns specific to Czech. The devil's-advocate skill is inspired by grill-me from Matt Pocock's collection.

## Author

Michal Kubíček, AI researcher · [kubicek.ai](https://kubicek.ai) · [aiedu.cz](https://aiedu.cz)

Ideas and feedback are welcome via [Issues](https://github.com/mediatoring/study/issues).

## License

[CC BY 4.0](../LICENSE) – you may freely use, adapt and share the skills as long as you credit the author.
