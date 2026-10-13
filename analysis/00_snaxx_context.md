# Snaxx Tech context (for applying the inquiry thread)

Snaxx Tech is a 1–2 person software studio in Kosovo with a Polish company for billing. It ships Expo/React Native games on Google Play, web apps and client work, and builds almost everything with AI coding agents. It wants two things: SaaS products and an agency that solves problems. The owner's Vianova Health contract ends 31 Oct 2026. Paddle bills SaaS; services are invoiced directly. Clear-scope projects take days to a week.

## Current strategy (from mining 1,021 notes, 13 Oct 2026)

Your rarest asset is not any single idea. It is a measured discipline for making AI agents tell the truth about their work: verdict blocks, red-flag catalogues with dated firings, a 135k-call reliability audit, playbooks whose rules expire. Four of the eleven mining batches found it independently. In 2026 the market's pain has moved from 'write code faster' to 'prove it works', so you are early on the right problem.

The fastest money is deadline- and incident-driven rescue work where you have already done the job once: React Native upgrades with a hard Google Play deadline, and launch-safety checks for vibe-coded apps. Every engagement should leave behind a checklist, then a skill, then an automated check. That ladder is how the agency turns into the SaaS without a separate bet.

Your home market is a second, quieter edge. Albanian-language, cash-on-delivery commerce and venue booking are underserved, you have one real client chain already written up, and no global competitor will localise for it.

Ladder: Service → checklist → skill → automated check → SaaS. Charge for the service first; ship the product only after the same check has been run by hand on 3+ paying clients.

### Cash now (0–30 days)
- **Play Deadline Upgrade for React Native / Expo apps** — Fixed-price upgrade for apps that can no longer ship updates to Google Play. Offer: 48-hour dependency audit €290 → fixed upgrade €2.4k (≤15 native deps) or €4.8k (more) → 'keep it building' retainer €390/mo. Deliverables: passing EAS build, API 36 target, 16 KB check, smoke video on a real Android 16 phone. Invoiced by the Polish company (not Paddle, whose policy excludes services).
- **Launch-Safe Check for vibe-coded apps** — Attack the live app, prove each hole with a recorded demo, then fix it for a fixed price. Offer: $390 72-hour check of the live app (scripted anon-key probe of every table, keys in bundle, webhook signature and idempotency, auth redirects) → $1,490 fix-and-retest bundle → $99/mo re-scan. Invoice directly; Paddle excludes services.
- **Balkan COD Growth Package** — Storefront audit, Albanian prompt pack and a revenue scorecard for cash-on-delivery shops. Offer: Fixed sprint €1.5–4k (audit + rebuild prompts + scorecard), then €200–400/mo scorecard retainer. Upsell: AI product-video pack. Invoice directly; Paddle excludes services.
- **'Your real product, guaranteed' AI video packs** — AI-generated motion with the real logo and label composited back in, never redrawn. Offer: 5 vertical ads + 1 hero video, 72-hour delivery, 2 revisions: €249 for local shops, $690 for EU/US sellers. Bundle with the COD package. Invoice directly; Paddle excludes services.

### Build next (30–90 days)
- **Agent Guardrails Install for dev teams** — Ten days to put a measured verification harness into a team's real repo. Offer: €4.9k fixed, 10 working days: project rules file, hooks that refuse 'done' without test evidence and block test-weakening diffs, CI gate that re-runs claimed tests, evidence PR template, cost caps and a dashboard. Then €900/mo playbook upkeep and quarterly re-audit. Invoice directly; Paddle excludes services.
- **Agent UI Verification Kit (open-core CLI + MCP)** — One command that gives agents truthful screenshots, frames, keys, hover and reduced-motion. Offer: Free CLI and MCP server; paid hosted runs with baselines and pixel-diff history; team licence. Also the delivery tool inside the Guardrails install. Bill through Paddle as merchant of record.
- **Scars series: how AI agents fake success** — Measured, dated case studies of agent failures. It is the marketing engine for every other bet. Offer: Free posts on the Snaxx Tech site and LinkedIn/X. Monetised indirectly through Guardrails installs, the verification kit and the playbook pack.
- **Indie Play Compliance & Monetisation Leak Audit** — Check that the APK matches the privacy policy, that app-ads.txt resolves, and that ad placements can actually earn. Offer: €500–1,500 audit per game plus optional fix sprint; hosted legal pages at €5–15 per app per month. Invoice directly; Paddle excludes services.

### Own later (90–180 days)
- **AppCare scanner (productised Launch-Safe Check)** — Automated scan and score for AI-built apps, with fix prompts and monthly re-scans. Offer: Free score; paid full report with fix prompts; €29–99/mo re-scan; done-for-you fixes as agency upsell. Bill through Paddle as merchant of record.
- **Evidence-gated reviewer for agent-written PRs** — A GitHub Action that refuses to approve without evidence slots filled. Offer: €49–299 per repo per month by size; enterprise self-host licence. Bill through Paddle as merchant of record.
- **COD Refusal Guard** — WhatsApp confirmation before dispatch, plus collected-versus-ordered revenue. Offer: €19–79/mo or per order; Shopify and WooCommerce plug-ins. Bill through Paddle as merchant of record.
- **FJALË for the diaspora** — Family word circles and heritage cards for second-generation Albanian speakers. Offer: Free daily game; paid family circle and learning cards; licences for weekend Albanian schools in DE/CH/US/UK. Bill through Paddle as merchant of record.

## The owner's existing method (their CLAUDE.md working harness, in short)

- Tag every claim VERIFIED/UNVERIFIED; label evidence MEASURED / READ / INFERRED.
- Review = re-run the original failure; reading the diff is not a review. Verdicts: APPROVE / REQUEST CHANGES / UNCERTAIN.
- Attack your own verdict before approving: construct the input that breaks it.
- A gate that cannot fail proves nothing: new tests must go red on the pre-fix tree; zeros need a positive control.
- Agreement between 'independent' oracles proves consistency, not correctness.
- Never invent a threshold: every number names the script or source that produced it.
- Compound learning: pattern → detection rule → brief update; twice → global red flag.
- Process ledger per task; change routes only on measured patterns, judged with A/B and null spread.
- Monitoring is part of the build: alive signal, failure reason, where the owner sees it, cost, drill.

## Deepest lessons found in the notes (depth 5)

- Rank ideas only after fetching the one primary source that could kill each: all three round-one picks (flat-price Shopify app, Daggerheart companion, developer API) fell to a marketplace scan, the licence PDF and a base-rate sample.
- Test your game against its own product doc with simulation: Arrows can never be bricked by tap order (so it is a visual-search task, not a logic puzzle), difficulty is flat to level 1000, and the best shapes appear after level 160.
- Every dashboard tile must map to exactly one revenue lever (sessions, conversion, AOV, repeat, COD refusals) or be deleted; each metric must name the decision it drives.
- Treat AI models as proposal-only adapters: they may draft dialogue, hints or interpretations, but a deterministic engine decides what enters canonical state.
- Every custom gate an agent writes ships a way to pass without measuring anything. Attack it with synthetic input (empty lists, misspelled flags, mutated report fields) before reading its tests.
- A zero count, or a negative grep, needs a positive control in the same build. Releases had dev-only log sinks, and Hermes bytecode made grep return 0 even for strings that were present.
- Simulating the real generator showed the game was not what the product doc claimed. It was a visual-search task, not a puzzle, with a flat difficulty curve. Measure the design before polishing it.
- Demanding computation produces honesty better than demanding honesty: once every spec number had to name the script that produced it, the proposing agent retracted 4 of its own claims.
- In agentic delivery, implementation was ~4% of wall-clock; reference build + review ~48%, review/fix loops ~27%, verification ~18%. Cheaper implementer models don't move the bottleneck.
- 'Feels like art, not a game' was an agency problem: autonomous desynchronised NPCs plus player click-to-move fixed what four rounds of motion polish could not.
- A gate that cannot fail proves nothing: every new test must go red on the pre-fix tree and catch a mutant, and every zero must be printed beside a positive-control count from the same build.
- Agreement proves consistency, not correctness. An 'independent' oracle written from the same reading fails together with the implementation, so constants and behaviours must be re-derived from the primary source (binary, spec, data).
- Green suites are blind to the real screen: fakes cannot segfault and tree hashes cannot see compositing. Layout, event and lifecycle changes close only by running the app and reaching that screen.
- Intuition picks the wrong bottleneck. Builds were guessed to dominate and were 6.2 % of helper time; model time was 34 %, and nothing ran in 80 % of calendar time. Answer 'why is it slow' from a ledger.
- Written rules alone did not change agent behaviour (foreground cap hits 0.28 % before the rule vs 0.39 % after). Behaviour changed only through enforcement such as hooks, judged against a frozen baseline with a workaround detector and a kill switch.
- Verification may get cheaper but never thinner. A faster route that worsens evidence, UI, perf or owner round-trips counts as a downgrade, and loosening a gate is never part of a speed change.
- Knowledge has a half-life. Rules should carry the versions and conditions they were measured under, an expiry date for heuristics, and a retirement register with reopen conditions, so stale advice is not served as fact.
- When a model cannot perceive the output (sound, motion feel, color), tell it so and make it measure with instruments, then hand bounded spot-checks to a human. Self-reported quality is worthless.
- Find the representation in which the solution is obvious before writing code; the biggest gains come from reframing, not typing faster.
- Turn every repeated agent mistake into a lint rule whose error names the correct helper. Strong abstractions plus strict lint narrow the design space so agents can only make good choices.
- If a record counts as open for business rules, the UI must also offer a way to close it. Fix the missing transition instead of bulk-patching the data, because the producer (e.g. fax intake) keeps creating that state, and the old rows carry real history.
- Never invent a limit: a threshold, cap or count is admissible only if the requester, a platform contract, project policy or a measurement supplies its exact value.
- Split entitlement checks into three questions. Org-level surfaces ask whether the org has the program enabled. History asks whether this record has data worth showing. New actions need org enabled, record in a valid state and user permission. Missing config means disabled. Old records stay visible; new work is blocked.

## What the owner asked for (13 Oct 2026, paraphrased)

Use the inquiry thread to find other ways of thinking, because thinking like the market makes us like the market. Apply it to: the startup, our methodology, AI as a whole, and setting Snaxx apart beyond basic SaaS ideas. Some SaaS is needed for money, but we want a broader mission that can scale and attract investors and others in our region (Kosovo, Albania, the Balkans), where nobody is doing this. Design foolproof tests for each idea.
