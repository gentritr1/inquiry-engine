# Inquiry Engine

**Understand the code your AI agents wrote.**

AI agents can build a whole project in a few days. You approve the work, but you did not make the design decisions. Later you cannot say why it is built this way, what breaks first, or what to change next.

Inquiry Engine is a free skill for coding agents. Type `learn` in any project. The agent stops explaining and starts asking. You guess each design decision first. Then the code, or a real measurement, shows you the answer.

## The problem

- An explanation feels like learning. A week later you cannot rebuild the idea alone.
- An agent's summary of its own work says what was built. It does not say what was traded away.
- "It works" on a quiet day says nothing about the day traffic doubles or a service goes down.
- Nobody writes down what you believed before you saw the answer, so you never find out how often you are wrong.

## How it works

1. **Map.** The agent reads the code and its history. It picks the 3 to 5 decisions that are hardest to undo.
2. **Guess.** It states one problem in plain words, with no solution in it. You say how you would solve it and how sure you are.
3. **Push.** It adds one constraint at a time. Your design changes until it holds, or until you reach the design the project uses.
4. **Break.** You guess what fails first. A simulation or the project's own tests measure it. If nothing can measure it, the agent says "not measured".
5. **Find the gap.** When you are unsure, the agent looks for the missing idea underneath. It teaches that one idea with an example, gives you the technical term, and lets you try a new case alone.
6. **Think like an expert.** You choose between two checks an experienced engineer might run, and say why.
7. **Log.** Every guess is saved before the answer is shown. Over time the log shows what you know and where you are too sure.

The agent uses simple English, one new idea at a time. You still learn the real technical terms, because you need them to work with other engineers.

### What a session looks like

This is from a test run on the open-source [breakscale](https://github.com/workersio/breakscale) repo. The agent's lines are real output. The owner's lines were written by the test.

> **Agent:** A student draws a few boxes, some servers and a database, and the lines between them. Each box has two settings: how many requests it can work on at once, and how long one request takes. The student drags the traffic up. The tool has to show how slow the slowest 1 in 100 requests is, and how many fail. How would you solve it, and how sure are you, 50 to 99%?
>
> **Owner:** I'd calculate it. Arrivals divided by what the box can handle, then a waiting-line formula for the latency. 80% sure.
>
> **Agent:** Logged at 80%. For one box by itself that holds. Next constraint: a caller does not wait forever. It gives up after a set time and asks again. Now the load depends on the failures, and the failures depend on the load. How would you change it?

When the owner is unsure, the agent does not repeat the answer louder. It looks for the idea underneath. This is from a second test run. The agent's lines are shortened, and the test wrote the owner's lines here too.

> **Owner:** If the box can do 100 each second and only 80 come, then every request goes straight in. So no line.
>
> **Agent:** Now I change one detail. The 80 requests still come in one second, but 20 of them arrive at the same moment. What happens to those 20, and why?
>
> **Owner:** Still no line. 80 is less than 100.
>
> **Agent:** At that moment, 20 requests want 10 places. 10 go in, and 10 wait. Think of a shop with 10 tills when a bus brings 20 people. Your rule, 80 under 100, is true for the whole second. It says nothing about a single moment. Engineers call this average fullness **utilization**. Why did 10 requests wait when utilization was only 80 percent?

In the first test, an agent without the skill answered the word "learn" with a full tour of the project. It asked for no guess and logged nothing.

## Use it

It is free and MIT licensed. There is no account, no key and no telemetry.

```bash
git clone https://github.com/gentritr1/inquiry-engine
```

```bash
ln -s "$PWD/inquiry-engine/skills/learn" ~/.claude/skills/learn
```

Open any project in Claude Code and type `learn`. Other agents that read skill folders work the same way; link the folder into their skills directory.

- Your session notes stay in the project, in `.learn/`. They are kept out of git.
- Your guesses go to `logs/predictions.jsonl` in your copy of this repo.
- For decisions about load and failure, the skill can use the [breakscale](https://github.com/workersio/breakscale) simulator if you connect it. It works without it.

## The end goal

People who can explain, defend and improve the systems their agents build.

Each project should leave you with better judgment, not only more code. The prediction log is the proof: it shows your guesses, how sure you were, and what was real. If the log shows the sessions do not teach, the skill is retired. That rule is written down in `analysis/05_learn_loop.md`.

## The method behind it, in five lines

1. **Spine.** Say what you want in one plain sentence, name the one thing in the way, and find the cheapest test that could change your mind.
2. **Predict before reveal.** Write your own answer and your confidence *before* you ask the AI. Learning lives in the gap.
3. **Let reality veto.** An idea is worth what it predicts. If it gets smaller under attack, that is progress. Elegance is a warning, not a proof.
4. **Rigor is a budget.** Spend it by stakes × irreversibility. The shield check asks: *is this method helping me decide, or helping me hide?*
5. **Amendment rule.** The rules change only after real, logged failures, never because feedback sounds smart.

## Honest status

**Not yet proven.** The method's theory is mostly known (Popper, Kuhn, Tetlock, Galef). What is new here is the path and the tools.

The `learn` skill was tested on agents: three scenarios with the skill and one without, one run each, on one repo. Those runs show that an agent follows it. They do not show that a person learns from it. Only filled logs can show that, and the skill's log starts empty. The first 20 logged guesses are the baseline.

## Where it came from

The method was taken from a 102-day ChatGPT thread (*Project Planning with LLM*, 1 Jul – 11 Oct 2026). The thread began with one question: *how do I get a very smart LLM to plan a project that is too complex to handle without the plan?* It became a Discovery Engine, *The Book of Inquiry* (v1 → v3), an Operating Card and Inquiry Logs. Claude and ChatGPT were used against each other, with the owner routing between them.

The `learn` skill also takes lessons from two open-source projects, both MIT licensed:

- [EricJujianZou/rederive](https://github.com/EricJujianZou/rederive): re-derive each design decision from the bare problem, and the decision map.
- [workersio/breakscale](https://github.com/workersio/breakscale): load a design until it breaks, and show only measured numbers.

`analysis/05_learn_loop.md` says what was taken from each and what was changed.

## Folders

| Path | What it holds |
|---|---|
| `skills/learn/SKILL.md` | The `learn` skill |
| `logs/predictions.jsonl` | Append-only prediction log the skill writes to (created on first use) |
| `analysis/05_learn_loop.md` | The learn loop: design note, lessons taken, test runs, review and kill rule |
| `TIMELINE.md` | Every file of the thread in the order it appeared |
| `sources/1-…` to `sources/5-…` | Each phase: its transcript (`00_transcript.md`) and every file attached or generated, prefixed by order and UTC time |
| `analysis/00_snaxx_context.md` | Who we are and what we asked for (input to the analysis) |
| `analysis/01_extraction.*` | Arc, core ideas, frameworks, prompts, lessons, quotes, weak spots, verdict (Fable) |
| `analysis/02_application.*` | Different thinking, methodology, AI view, mission, region, products, tests, 30-day plan (Fable) |
| `site/build.py` → `site/dist/` | The multi-page site built from `analysis/*.json` |
| `raw/` *(git-ignored)* | The full ChatGPT export, the tool log and the original files. Verified by SHA-256 against the page at export time |

## How to keep advancing it

- Say `learn` in a real project and let the log fill.
- Log every other real decision too: date, question, your answer, confidence, what happened.
- Run the tests in `analysis/02_application.md` with the prediction written first.
- Change the method only through the amendment rule: point to a logged failure.
- Rebuild the site: `python3 -I site/build.py`.

## License

[MIT](LICENSE). Use it, change it and share it for free.

## Provenance

Exported 13 Oct 2026 through the owner's signed-in ChatGPT session. Transcript and text files match the page's own SHA-256 hashes. No credentials were found in the thread (secret scan run; flagged lines were filenames and code).
