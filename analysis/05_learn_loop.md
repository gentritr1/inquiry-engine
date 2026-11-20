# The learn loop

*20 Nov 2026. Design note for `skills/learn/SKILL.md`, and a record of what we took from two outside repos.*

## Why

Agents build almost everything at Snaxx Tech. The owner reviews their work but did not make the design decisions, so the tradeoffs, the breaking points and the future of each system are known to nobody in the studio. Saying `learn` in a project starts a session that closes this gap.

The loop is the Inquiry Engine's own method, applied to code:

1. **Guess.** The owner designs each decision from the bare problem and states a confidence.
2. **Reveal by reality.** The code shows the real decision. A measurement shows what breaks.
3. **Log the gap.** Every guess goes into `logs/predictions.jsonl` before the reveal.

## What we took, and from where

| Source | Lesson taken | What we changed |
|---|---|---|
| Inquiry Engine (this repo) | Predict before reveal. Reality vetoes. Rigor is a budget. An unlogged prediction cannot fail. | The prediction is a design, not a yes/no claim. Decisions are picked by stakes x irreversibility, 3 to 5 per project. |
| [EricJujianZou/rederive](https://github.com/EricJujianZou/rederive) (MIT) | Pose the problem with no solution terms and add one constraint at a time. Build a decision map from code and diffs, not commit messages. Check every file and symbol reference with grep. One question per message. A better idea from the learner is a win. | A reveal is allowed after one ask for a guess, and is logged as `revealed`. Confidence is asked every time. Misses are re-asked in the next session. The share card and post are left out. |
| [workersio/breakscale](https://github.com/workersio/breakscale) (MIT) | Load a design until it breaks. Every number is measured from a run, never plausible. Say which inputs were guessed. A replay link reruns the same seed. | Used only for system-shaped decisions (requests, queues, retries, databases, webhooks). Other decisions use the project's own tests, or are labelled "not measured". |

Checked on 20 Nov 2026 by starting `npx -y breakscale-mcp --stdio` (version 0.1.1) and listing its tools: `read_me`, `create_view`, `export_design`, `open_design`. The hosted server lists the same four. The `break_it` tool in breakscale's README is not in either yet, so the skill uses it only when the server lists it.

## Baseline

Before the skill was written, a fresh agent was given the word "learn" in a clone of breakscale with no skill. It read the code and sent a full tour of the systems, tradeoffs and risks. Asked "just tell me how the retry handling works", it explained at once. It asked for no guess and no confidence, and it logged nothing. One run, so it shows the default, not a rate.

## Test runs

All four ran on 20 Nov 2026 in a clone of breakscale, each with a fresh agent and one run per scenario. They show that agents can follow the skill. They do not show that an owner learns from it; only the log can show that.

| Run | Scenario | What the agent did |
|---|---|---|
| Baseline, no skill | Owner says "learn" | Sent a full tour first. Explained at once when asked. No guess, no confidence, no log. |
| With skill, first session | Same message | Asked for the root problem first. Built a five-decision map; all 30 code references passed the grep check. Logged the guess before it answered. Revealed only after one ask for a guess. |
| With skill, returning session | Owner says "learn" again | Re-asked the revealed decision with no mention of the earlier try. Used the first constraint that broke the owner's design. Said "not measured" and named the command where nothing could be run. Logged all three guesses. |

| With skill, unsure owner | Owner gives a wrong rule at 90%, then hedges | Asked what led to the answer. Changed one detail to separate two causes. Tested the earlier idea with a fresh case. Showed the step, then gave the term **utilization**. Measured on its 16 messages: longest sentence 20 words, one question in each message, none in the stop report. |

In the last run the agent wrote most of the owner's replies itself, so its gap diagnosis rests partly on answers it invented. A real owner is the only real test of that part.

The first two skill runs also reported 41 places where the wording left the agent guessing. The fixes: one result vocabulary mapped to the prediction verdicts, a try number in each prediction id, one question in the Break ask, a rule for what a re-ask covers, and a full clone instead of a blobless one so diffs can be read.

## Second opinion (Astra 6.2)

On 20 Nov 2026 the skill was sent to a second model, Astra 6.2, for review as an instructional designer. Its findings that were adopted:

| Finding | Change in the skill |
|---|---|
| A picture before the guess gives the design away. | Plain words before a guess. The picture and the term come when teaching. |
| A wrong answer shows where the gap is, not why. | Find the gap now tests the cause first: ask what led to the answer, then change one detail that separates two likely causes. |
| An example the owner can copy does not show understanding. | Show the missing step in one case, hand over a second case, then return to the project with one condition changed and no hint. |
| "What would an expert check?" rewards guessing the agent's answer. | The Expert phase asks the owner to choose between two plausible checks and say why. |
| Only misses were reviewed, and the review rule clashed with the gap rule. | Each returning session opens with one review question from memory, hits included, with a next review date. |
| The ASD-STE100 summary was wrong in detail. | The skill says "guided by ASD-STE100" and states its own 20-word limit. |
| Result and verdict were mixed. | Result records how the owner reached the design. Verdict judges the first guess against the stated constraints. |

Its warning stands as the main risk: a good conversation can look like learning. The delayed review question, answered with no help, is the check for it.

## Approaches considered

- **A. Install rederive as it is and add a thin wrapper.** Rejected: it never reveals, asks for no confidence, keeps no prediction log and ends with a share card. Its behaviour could also change under us.
- **B. One self-contained skill in our own words (chosen).** It lives in this repo, so changes are tracked and fall under the amendment rule. `~/.claude/skills/learn` links to it.
- **C. A rule in CLAUDE.md only.** Rejected: it would load in every session, and the owner's notes show written rules alone did not change agent behaviour. CLAUDE.md gets one pointer line.

## The log

`logs/predictions.jsonl` is append-only. One line is written when a guess is made and a second line, with the same `id`, when it resolves. The field names match the `predictions` collection of the site's shared log (`question`, `answer`, `confidence`, `area`, `resolveBy`, `status`, `outcome`), so rows can be loaded into it later. The two logs are not synced yet.

## Review and kill rule

Review after 20 resolved `learn` lines:

- Compare the share of `hit` on cold re-asks of earlier misses with the share of `hit` on first asks. If re-asks are no better, the sessions are not teaching, and the skill is retired.
- Bucket guesses by stated confidence and report the calibration gap. It is reported, not thresholded.
- Count the briefs that came from a `better idea`.

No number in this note is a target. The first 20 lines are the baseline.

## Changing the skill

By the amendment rule: point to logged sessions where the skill misled, not to a version that reads better.
