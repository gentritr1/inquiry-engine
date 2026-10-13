# Inquiry Engine

A method for thinking with AI, taken from a 102-day ChatGPT thread (*Project Planning with LLM*, 1 Jul – 11 Oct 2026), and a plan to test it on real work at Snaxx Tech.

The thread began with one question: *how do I get a very smart LLM to plan a project that is too complex to handle without the plan?* Over five phases it became a Discovery Engine, *The Book of Inquiry* (v1 → v3), an Operating Card, Inquiry Logs and a personal Investigator Roadmap. Claude and ChatGPT were used against each other, with the owner routing between them.

## The method in five lines

1. **Spine.** Say what you want in one plain sentence, name the one thing in the way, and find the cheapest test that could change your mind.
2. **Predict before reveal.** Write your own answer and your confidence *before* you ask the AI. Learning lives in the gap.
3. **Let reality veto.** An idea is worth what it predicts. If it gets smaller under attack, that is progress. Elegance is a warning, not a proof.
4. **Rigor is a budget.** Spend it by stakes × irreversibility. The shield check asks: *is this method helping me decide, or helping me hide?*
5. **Amendment rule.** The rules change only after real, logged failures, never because feedback sounds smart.

## Honest status

Profound in its path and tools, mostly known in its theory (Popper, Kuhn, Tetlock, Galef…), and **not yet proven**: the prediction, calibration and failure logs are still empty. The next step is not a grander framework. It is filled logs on problems whose answers we do not know. See `analysis/02_application.md` → *Tests*.

## Folders

| Path | What it holds |
|---|---|
| `TIMELINE.md` | Every file in the order it appeared |
| `sources/1-…` to `sources/5-…` | Each phase: its transcript (`00_transcript.md`) and every file attached or generated, prefixed by order and UTC time |
| `analysis/00_snaxx_context.md` | Who we are and what we asked for (input to the analysis) |
| `analysis/01_extraction.*` | Arc, core ideas, frameworks, prompts, lessons, quotes, weak spots, verdict (Fable) |
| `analysis/02_application.*` | Different thinking, methodology, AI view, mission, region, products, tests, 30-day plan (Fable) |
| `site/build.py` → `site/dist/` | The multi-page site built from `analysis/*.json` |
| `raw/` *(git-ignored)* | The full ChatGPT export, the tool log and the original files. Verified by SHA-256 against the page at export time |

## How to keep advancing it

- Log every real decision in a prediction log: date, question, your answer, confidence, what happened.
- Run the tests in `analysis/02_application.md` with the prediction written first.
- Change the method only through the amendment rule: point to a logged failure.
- Rebuild the site: `python3 -I site/build.py`.

## Provenance

Exported 13 Oct 2026 through the owner's signed-in ChatGPT session. Transcript and text files match the page's own SHA-256 hashes. No credentials were found in the thread (secret scan run; flagged lines were filenames and code).
