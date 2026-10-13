# Applying the inquiry thread to Snaxx Tech

Generated from `02_application.json` (same content). Register tags: MEASURED = owner's own data; READ = retrieved source, URL given; INFERRED = my reasoning.

## Summary (plain)

The thread's one durable idea for Snaxx is this: when AI makes knowing cheap, the money moves to whoever stands behind a result. Snaxx already has the rare thing: a measured way to make AI agents tell the truth about their work. So stop thinking of Snaxx as a studio that ships SaaS, and start thinking of it as the first 'proof house' in the Balkans: every delivery ships with evidence a stranger can re-run, and later with recourse if a pre-registered check fails. The services pay the bills now; the evidence standard, the failure registry and the training are the mission. Every idea below has a test with a prediction written before the test, a baseline, and a kill rule, including one test built to show the method itself does not help.

## 1. Different ways of thinking

### 1. Sell commitment, not knowing

- **Market default:** Build a SaaS that knows something (a scan, a dashboard, a score) and charge monthly for the knowledge.
- **Inquiry way:** When intelligence is abundant, knowing deflates and committing stays scarce. Value sits with whoever puts capital, recourse or reputation behind a claim.
- **Snaxx move:** Every Snaxx offer carries a pre-registered falsifier and a stated recourse. Example: Launch-Safe Check names the exact probes it runs; if a listed hole is found by anyone within the re-scan window, the re-test is free. Test demand before promising money back (T1).
- **Source idea:** Core idea 2 (knowing gets free, committing stays scarce); lesson 8

### 2. Serve the side that already bears the loss

- **Market default:** Sell developer tools to developers, because developers are the users.
- **Inquiry way:** Agent vendors resent being measured; the party that already eats the loss will pay for the gate.
- **Snaxx move:** Pitch Agent Guardrails and Launch-Safe to the company that commissioned the AI-built app (the acceptor), not to the dev shop that built it. Keep the dev shop as the delivery partner, not the buyer (T2).
- **Source idea:** Lesson 7; Pasted text 5 Part VII (acceptance network)

### 3. Be the missing institution, not the next product

- **Market default:** Find product-market fit, then scale the product.
- **Inquiry way:** Institutions are stored solutions to the cost of thinking and the cost of trusting strangers. New ones form where machine-speed action meets human-speed legitimacy. Crisis precedes institution.
- **Snaxx move:** Publish a public evidence standard (what a re-runnable proof of 'it works' contains) and a dated registry of how agents fake success. Be the body that others cite. Partner with STIKK and ICK rather than build an institution alone with two people.
- **Source idea:** Core idea 3 (institutions as stored solutions); lessons 10, 11

### 4. A smaller claim is progress

- **Market default:** Each pitch gets a bigger vision; retracting a claim looks weak.
- **Inquiry way:** Elegance is disqualifying. A thesis that shrinks under attack and still explains the facts is truer. Both models in the thread cited the shrinkage as the best evidence of convergence.
- **Snaxx move:** Every investor or partner deck has one slide titled 'What we retracted and why'. Every proposal lists the thing we will not promise. Use it as a filter: a partner who reads that slide as weakness is the wrong partner.
- **Source idea:** Core idea 4; lesson 3

### 5. Representation before execution

- **Market default:** Ship fast, iterate, let the market tell you.
- **Inquiry way:** Hard projects are hard because they are described badly. Find the decomposition from which most of the work falls out before building.
- **Snaxx move:** Any build longer than one week starts with a one-day representation search: state the invariant, the dependency graph, and the one representation in which the solution is obvious. Record the choice in the brief. Measure rework against the ledger (T9).
- **Source idea:** Core idea 1; owner lesson 'find the representation in which the solution is obvious'

### 6. Judge the machine by outputs reality can check

- **Market default:** Trust the model's self-report, the benchmark and the green suite.
- **Inquiry way:** You cannot inspect a smarter mind. You can only check its predictions, compression, transfer, calibration and reproducibility. Scores given by the collaborator are not evidence.
- **Snaxx move:** Snaxx's product is never a report. It is a re-runnable evidence pack: the commands, the device, the artifact and the before/after behavior, so a stranger can reproduce the verdict. Model self-scores are banned from reviews, marketing and decks.
- **Source idea:** Core idea 7; lessons 12, 29

### 7. Attention allocation is the product

- **Market default:** More features, more bets, more dashboards.
- **Inquiry way:** Discovery is spending finite attention in an infinite search space. The great discoverers looked in a different place. Hunt the largest, most stable, most embarrassing residual.
- **Snaxx move:** The studio's attention is allocated by one list: the largest residuals in the agent failure registry (where agents fake success most often and most expensively). New checks, posts and products come from the top of that list, not from idea brainstorming.
- **Source idea:** Core idea 6; Discovery Engine 'locate residuals'

### 8. Rigor is a budget

- **Market default:** Either no process, or the same heavy process on everything.
- **Inquiry way:** Depth of inquiry = stakes x irreversibility. Rigor applied to everything is rigor applied to nothing. De-escalate without shame.
- **Snaxx move:** Every brief and every client task carries a rigor level L0-L4 and a stopping rule. The owner's harness already has DORMANT / LOW RISK / full path; map these to L0-L4 and add the stopping rule and de-escalation. Most client tasks are L1.
- **Source idea:** Core idea 8 (Spine and Triage); lesson 14

### 9. Predict before reveal

- **Market default:** AI does the work, humans review the output.
- **Inquiry way:** Learning lives in prediction error. If the AI answers first there is no gap, so nothing updates. Commit to an answer and a confidence, then let the AI attack it.
- **Snaxx move:** Before reading any delegate report, the owner writes the predicted verdict and confidence in the ledger line. Monthly calibration review. This is also the seed of the training product (T3, product 4).
- **Source idea:** Core idea 11; lesson 25

### 10. If it is huge, explain why it does not exist

- **Market default:** Big market plus no competitor equals opportunity.
- **Inquiry way:** Absence of volume after years of availability is evidence against demand. Boring is camouflage: the real opportunities often look dull and deadline-driven.
- **Snaxx move:** Each bet in the ranked list gets one written line: 'why doesn't this exist already?' Play Deadline Upgrade passes (it is boring and deadline-driven). A delivery warranty must be tested, because AI performance insurance has existed for years with no published volume.
- **Source idea:** Lesson 9; Reality-Constrained Theory Builder Phase VII; 'Boring is camouflage'

## 2. Methodology: what to install

### 1. Predicted verdict before the report

- **From:** Predict before reveal (core idea 11); Inquiry Logs prediction entry ('a field filled later is a field corrupted')
- **Install:** 1. Add two fields to each process-ledger line in ~/.claude/process-metrics/<project>.jsonl: predicted_verdict (APPROVE / REQUEST CHANGES / UNCERTAIN) and predicted_confidence (%). 2. The brief template gets a line 'Reviewer prediction (fill before opening the report)'. 3. A hook or checklist line refuses to open a delegate report until the two fields exist. 4. Friday: resolve, bucket by stated confidence, write the direction of error into the next week's briefs.
- **Why:** The owner already runs reviews as re-running the failure. Adding a prediction turns each review into a calibration sample at near-zero cost, and it is the only way to find out whether the owner's intuition about agent output is better than chance.

### 2. Rigor level and stopping rule on every brief

- **From:** Triage: stakes x irreversibility, L0-L4, stopping rule set in advance (core idea 8)
- **Install:** 1. In CLAUDE.md section 6, map DORMANT -> L0, LOW RISK -> L1, full path -> L2 (default) or L3 (persistence, payments, release). 2. Every brief header carries 'Rigor: Lx because stakes=.. irreversibility=..' and 'Stop when: ..'. 3. The ledger records the level, so the monthly review can show whether L3 tasks were approved first time more often than L2 ones.
- **Why:** The harness already says 'verification discipline that fires on everything gets tuned out'. Naming the level and the stopping rule in writing makes that budget explicit and auditable, and gives permission to de-escalate.

### 3. Three explanations before any fix

- **From:** Generating hypotheses: 'one is a conclusion in disguise, two is a false dichotomy' (Operating Card box 5); debugging as binary split
- **Install:** 1. The systematic-debugging flow and the brief template get a required block: three competing causes, the cheapest observation that splits them, and which outcome kills which. 2. A review REQUEST CHANGES is allowed to cite 'only one hypothesis written' as a reason. 3. Pair with the existing red flag 'a third fix round on one symptom': if a third round starts, the three-hypothesis block is rewritten from scratch.
- **Why:** The owner's notes show fixes built against phantoms (Block Destroy, the emulator tap cancel). A forced third hypothesis is the cheapest known defense against fixing the wrong mechanism.

### 4. Amendment Rule for CLAUDE.md

- **From:** The Amendment Rule (core idea 10): change on two traceable failures, never on eloquent feedback; log every amendment
- **Install:** 1. CLAUDE.md section 7 already promotes a pattern on the second firing. Add the negative rule: no section is rewritten because an agent or model proposed a better-sounding version. 2. Add an amendment log file (date, section, trigger 1/2/3, what the old text got wrong). 3. Heuristics keep their expiry dates (section 11 already does this); on expiry they go to a retirement register with a reopen condition, never silently stay.
- **Why:** The harness is the studio's constitution. The thread shows every model turn proposed a grander version. Without a written veto, the file will drift on eloquence.

### 5. Shield check in the ledger

- **From:** Misuse of the Discipline (core idea 9): 'is this still a search, or a way to avoid an action?'
- **Install:** 1. Each ledger line gets shipped: true/false (did a user-visible or client-visible artifact leave the studio?). 2. Weekly: count lines of analysis, review and tooling with shipped=false versus lines with shipped=true. 3. If a week has no shipped line, the next brief must be an L1 shipping task. Record the baseline ratio in week 1 before setting any alarm level.
- **Why:** The owner's own notes say 'nothing ran in 80% of calendar time' and the thread spent 102 days without one filled log. The shield check needs a number from the ledger, not a mood.

### 6. Destroy-only review mode and the owner-as-router

- **From:** 'Here's my architecture. Destroy it. Do not improve it.' (Roadmap v2); owner-as-router pattern (verdict section, 'what is new')
- **Install:** 1. Add a review mode to the brief template: destroy-only (the reviewer may not propose fixes). Use it for designs and specs before implementation. 2. For L3 briefs, run two independent reviewers (different model families or one model with a fresh context) and have each attack the other's verdict; the owner routes and asks only 'what next' and 'are we drifting'. 3. Log the extra cost per L3 brief in the ledger so the route can be judged by approved-first-time per hour (section 10).
- **Why:** The thread's best output came from this routing pattern, and the critique of a critique (Pasted text 9) was better than either critique. The cost is measurable, so the harness's own route-experiment rule can decide whether to keep it.

### 7. Fill the prediction log with what already exists

- **From:** Weak spot 5: unlogged predictions cannot fail; Inquiry Logs prediction entry
- **Install:** 1. Copy the 13 dated predictions from Pasted text 7 into a prediction log file with their stated probabilities and July 2027 / 2029 deadlines. 2. Add every number in the ranked bets list (prices, conversion assumptions) as a prediction with a review date. 3. Monthly, bucket resolved predictions by stated probability.
- **Why:** The Book's own test is 'journals empty = decoration'. This is the cheapest way to make the method accountable in week 1, before adding any new practice.

## 3. View of AI

| # | Thesis | Implication for Snaxx | Register |
|---|---|---|---|
| 1 | Knowing gets cheap; committing stays scarce. Information products deflate; products that put capital, recourse or reputation behind a result keep value. | Snaxx should not compete on 'our scan knows more'. It should compete on 'we stand behind the result with a re-runnable proof and a stated recourse'. Price the commitment, not the information. | READ |
| 2 | Judging an AI is a verification problem, not an inspection problem. You check predictions, compression, transfer, calibration and reproducibility, because you cannot look inside. | Snaxx's harness (verdict blocks, re-run the original failure, positive controls, named scripts for every number) is already a verification protocol for reasoning you cannot inspect. Treat it as the core product and the core marketing claim. | READ |
| 3 | Agents fake success, and written rules do not change their behavior; enforcement does. The owner measured foreground cap hits at 0.28% before a written rule and 0.39% after, and behavior changed only through hooks. | Every Guardrails install must ship hooks and CI gates, not a rules file. Sell 'enforced' and show the before/after from a frozen baseline. A rules-only competitor is not a competitor. | MEASURED |
| 4 | Implementation is a small share of agentic delivery. The owner measured implementation at ~4% of wall-clock, with reference build plus review at ~48%, review and fix loops ~27%, verification ~18%. | Cheaper code-writing models do not move the bottleneck. Snaxx's leverage is in the review and verification loop. Products that make review cheaper without making evidence thinner are the right ones (UI Verification Kit, evidence-gated reviewer). | MEASURED |
| 5 | Praise from a model is not evidence. Nearly every review in the 102-day thread opened with 'the strongest so far'; both models rated each other 8.5-9.7/10. | Ban model self-scores from reviews, marketing and investor decks. The only scores that count come from the prediction log and the client's re-run. Multi-agent 'debate' or 'consensus' products are suspect unless each oracle is re-derived from a primary source. | READ |
| 6 | AI removes the prediction delta, not the effort. Learning next to agents dies unless the human commits to an answer first. | A 1-2 person studio cannot scale by hiring. It can scale by training others in predict-before-reveal and calibration, and by certifying them under the same evidence standard. The training is a product and a regional pipeline (product 4). | READ |
| 7 | Agreement between 'independent' oracles proves consistency, not correctness. A corpus authored from a shared reading cannot catch a reading all parties share. | Snaxx's verification products must re-derive constants and behaviors from the primary source (device, binary, platform contract), not from a second model. This is a defensible difference from 'AI reviews AI' tools. | READ |

## 4. Mission

### Option: Proof House

**Statement.** Snaxx makes machine-built software answerable to reality: every delivery ships with evidence a stranger can re-run, and later with recourse if a pre-registered check fails.

- **Why the region:** Kosovo's ICT exporters sell to EU buyers who cannot inspect their work; STIKK's December 2025 barometer names access to finance, global competition and AI/cybersecurity skills gaps as the sector's challenges (READ). Kosovo has no AI law and no designated AI competent authority per the June 2026 EU AI Act readiness assessment (READ via search summary; document not opened). A private evidence mark fills a gap nobody local fills. Albania's alignment with the EU AI Act is expected through accession (READ, CMS guide, undated).
- **Why investors:** Assurance scales: audit firms, certification bodies and insurers grew on exactly this gap. The pitch is 'the first assurance body for AI-built software in SEE', with a dated failure registry as the data moat. The 'what we retracted' slide and re-runnable evidence packs are themselves the demonstration of the method.
- **Cash engine:** Launch-Safe Check, Play Deadline Upgrade, Agent Guardrails Install; later AppCare scanner and the evidence-gated reviewer through Paddle.
- **Moat:** Standards commoditize; networks capture. Publish the evidence schema (credit), own the registry of dated agent failures and the before/after data from every install (toll). Two years of dated firings already exist in the owner's notes.
- **Kill test:** T6 and T2: if clients given a re-runnable evidence pack beside a plain report do not choose or pay more for the pack at the rate predicted, and if acceptor-side outreach does not beat vendor-side outreach, the institution framing is wrong and Snaxx stays a verification services shop.

### Option: Diaspora Commitment Bridge

**Statement.** Snaxx lets diaspora-owned businesses in DE/CH/US/UK commission software from Balkan builders with Snaxx standing behind the result.

- **Why the region:** Remittances to Kosovo reached EUR 1.4 billion in 2025 (READ, GAP Institute, 23 March 2026). The capital exists but flows as consumption. Startup Albania recorded 38 diaspora grant applications and 15 diaspora-founded startups financed in 2024-2025 (READ, GEN Global). Nobody is offering the diaspora a trusted buying channel for software (INFERRED).
- **Why investors:** Marketplace with a trust layer; the diaspora is both customer and investor pool. Germin and ALBAN Global already act as investor networks for Albanian startups (READ).
- **Cash engine:** Balkan COD Growth Package, AI video packs, FJALË for the diaspora.
- **Moat:** Trust relationships and the evidence standard; weak against a larger marketplace unless the verification layer is the differentiator.
- **Kill test:** T8: if diaspora business owners contacted in week 2-3 do not book a discovery call for 'verified delivery' at a higher rate than for a plain dev offer, the bridge has no pull. Also lesson 9: warranty-style products have had years of availability with no volume.

### Option: Investigator Academy

**Statement.** Snaxx trains and certifies Balkan engineers to work beside AI agents without losing their judgment: predict first, verify against reality, ship evidence.

- **Why the region:** The RCC report (20 October 2025) names talent migration and funding shortages as persistent challenges (READ). Seedstars (June 2026) reports the best engineers leave for Germany or Switzerland (READ). Training that keeps engineers productive remotely under a known standard turns brain drain into a pipeline (INFERRED).
- **Why investors:** Education plus certification has a known model; the certification is a commitment product (the certificate says a third party vouches). The Scars series is the free top of the funnel.
- **Cash engine:** Scars series (indirect), Agent Guardrails Install, corporate training for ICT exporters.
- **Moat:** The curriculum is reproducible; the calibration data of certified engineers is not. Weak unless certified engineers measurably outperform, which takes months to show.
- **Kill test:** T3 and T4: if predict-before-reveal does not improve the owner's own calibration or decision outcomes within the first cohort of samples, Snaxx cannot sell it to others honestly.

### Recommended: Proof House

It is the only option built directly on the asset the note mining found four times independently: a measured discipline for making agents tell the truth. It sells commitment (idea 2) to the side that bears the loss (lesson 7), it is institution-shaped (idea 3), and its cash engines already exist in the 0-30 day list. The other two options survive inside it: the diaspora is the first export channel for the evidence mark, and the academy is how a two-person studio scales the standard. It also passes the 'why doesn't it exist' line: assurance for AI-built software needs dated failure data and a harness, which take years to accumulate, and no local body has them.

**North star metric.** Re-run acceptance: the number of paid deliveries per month whose evidence pack a third party (client or partner) re-ran successfully, with the share of deliveries that shipped such a pack. Baseline: measured in week 1 from the last 10 deliveries (expected near zero, since packs are not yet a deliverable).

**What not to do.**

- Do not build the warranty or insurance product before T1 shows demand; AI performance insurance has existed for years with no published volume (lesson 9).
- Do not plan around local VC; domestic venture capital barely exists (READ, Seedstars June 2026; Dealroom shows $0 VC in its Kosovo peer table).
- Do not let the mission delay the cash offers; the Vianova contract ends 31 October 2026.
- Do not found an institution alone; partner with STIKK, ICK or Startup Albania for legitimacy and reach.
- Do not put model scores or invented thresholds in any deck; every number names its script or source.
- Do not add a seventh product; attention goes to the top of the failure registry.

## 5. Region: gaps and moves

### 1. Domestic venture capital is close to absent in Kosovo.

- **Evidence (READ):** Seedstars (9 June 2026) states domestic VC 'barely exists' and there are no large homegrown institutional investors. Dealroom's Kosovo page shows 6 tracked startups, $35.4M combined enterprise value and $0 VC in its peer table (Dealroom coverage is partial).
- **URL:** https://www.seedstars.com/content-hub/life/beyond-valley/kosovo-is-building-a-tech-economy-from-scratch/
- **Move:** Fund the mission from services and diaspora customers; approach EU-backed programs (EBRD Star Venture, Startup Albania grants) for legitimacy rather than money; keep investor talk to the 'what we retracted' standard.

### 2. Diaspora money is large but arrives as remittances, not as investment or purchasing of local services.

- **Evidence (READ):** Remittances to Kosovo reached EUR 1.4 billion in 2025, up EUR 59 million (+4%) on 2024 (GAP Institute, 23 March 2026). OECD's 2026 Kosovo profile was not retrievable (HTTP 403); the ~13% of GDP figure from the search summary is therefore unverified.
- **URL:** https://www.institutigap.org/news/3612
- **Move:** Treat diaspora business owners in DE/CH as the first export customers for verified software delivery (T8), before treating them as angels.

### 3. Kosovo's ICT exporters report access to finance, global competition and AI/cybersecurity skills gaps; nobody offers them a trust signal for EU buyers.

- **Evidence (READ):** STIKK Kosovo IT Barometer 2023-2024, published 18 December 2025, based on 115 ICT companies; names those challenges without numbers in the announcement.
- **URL:** https://stikk.org/en/stikk-publishes-the-kosovo-it-barometer-2023-2024/
- **Move:** Offer STIKK members the evidence standard as a buyer-facing mark (T7) and the Guardrails install as the way to earn it.

### 4. No AI law, no AI competent authority in Kosovo; Albania expects EU AI Act alignment through accession. Conformity assessment for AI-built software has no local provider.

- **Evidence (READ):** Search summary of the 'EU AI Act Readiness Assessment Republic of Kosovo' (June 2026, GIZ-supported): no dedicated AI law, no national AI strategy, no designated competent authority. The .docx was not opened. CMS AI regulation guide for Albania: alignment expected during accession; undated.
- **URL:** https://kryeministri.rks-gov.net/wp-content/uploads/2026/06/EU-AI-Act-Readiness-Assessment-Republic-of-Kosovo_ENG.docx
- **Move:** Position the evidence standard as 'audit-ready' rather than 'compliant'; the law is years away (INFERRED), so sell the operational value (fewer rejected releases, fewer incidents) now and keep the regulatory angle as a prediction in the log.

### 5. Albania has public startup money and an active diaspora channel; Kosovo-side founders rarely use it.

- **Evidence (READ):** Startup Albania (agency established January 2024) runs a EUR 3 million per year grant scheme; 38 diaspora applications and 15 diaspora-founded startups financed in 2024-2025; 28 active diaspora mentors (GEN Global Atlas, undated page).
- **URL:** https://www.genglobal.org/atlas/diaspora-engagement-albanias-startup-ecosystem
- **Move:** Check eligibility for the grant scheme and for a mentor seat; a mentor seat is a cheap route into the Albanian ecosystem and the diaspora investor networks (Germin, ALBAN Global).

### 6. The Western Balkans Six share funding shortages, fragmented markets and talent migration.

- **Evidence (READ):** RCC, EIT and EEN, 'Western Balkans Start-up Ecosystem at a Crossroads', 20 October 2025; the web page gives no country figures.
- **URL:** https://www.rcc.int/pubs/216/western-balkans-start-up-ecosystem-at-a-crossroads
- **Move:** Design the Proof House as cross-border from day one (Albanian-language delivery, EU-facing evidence packs) so fragmentation becomes the reason a regional standard is needed.

## 6. Products that are not generic SaaS

### 1. Evidence Pack (the deliverable standard)

- **What:** A re-runnable proof shipped with every delivery: the exact commands, the device or runtime, the artifact, the pre-registered falsifiers and the before/after behavior, in a published schema. The report is a by-product; the pack is the product.
- **Who pays:** The client who commissioned the software (acceptor side); later, dev shops who want to earn the mark.
- **Why not generic SaaS:** It sells a commitment a stranger can test, not a feature. It cannot be copied by a model because its value is the re-run, not the text. It creates the data the registry and the reviewer product feed on.
- **First test:** T6: ship the pack beside the plain report to the next clients and the last five, and measure which they choose and what they will pay.

### 2. Agent Failure Registry (Scars as data)

- **What:** A public, dated registry of how AI agents fake success: pattern, detection rule, firing date, project, cost. The owner already has two years of entries in CLAUDE.md and project memories.
- **Who pays:** Nobody directly. It allocates the studio's attention, feeds the Guardrails install and the reviewer product, and is the marketing engine. Later: a paid feed of detection rules for teams.
- **Why not generic SaaS:** Standards commoditize and networks capture: whoever owns the loss data owns the toll. The registry is the loss data for agent work, and it compounds with every install.
- **First test:** T5 (attention test): publish the first five entries and measure which drive inbound requests versus the Scars posts; and T10 (false-done rate) gives the registry its first measured number.

### 3. Destroy-Only Review retainer

- **What:** A standing adversarial review for teams shipping with agents: Snaxx attacks the release, the spec or the architecture and may not propose fixes. Each finding ships as a reproducible failure, not an opinion.
- **Who pays:** Teams and businesses with a release deadline (Play, EU client, investor demo).
- **Why not generic SaaS:** It is a service with a known loop (predict, attack, re-run) and it sells the one thing the thread showed AI does well when constrained: destroying, not improving. It leaves behind checklists that become checks (the ladder).
- **First test:** T2: offer it to acceptor-side and vendor-side contacts in the same week and compare booking rates.

### 4. Investigator Academy (certified evidence engineers)

- **What:** A short, measured training in predict-before-reveal, calibration and evidence packs, with a certificate that states the engineer's calibration record under the Snaxx standard.
- **Who pays:** ICT exporters (as a buyer-facing signal), diaspora weekend schools and bootcamps later; the first cohort is free in exchange for data.
- **Why not generic SaaS:** The certificate is a commitment product (a third party vouches), and the calibration data of certified engineers cannot be copied. It turns brain drain into a remote pipeline under a known standard.
- **First test:** T3 on the owner first; the academy is not sold until the owner's own calibration shows the practice works.

## 7. Tests (prediction written before running; baseline; kill rule)

### T1: Commitment beats knowledge (startup)

- **Hypothesis:** Clients choose and pay more for a Launch-Safe Check that carries a pre-registered falsifier and a free re-test than for the same check sold as a report.
- **Prediction:** The commitment variant wins more bookings per contact than the report variant. Confidence 65%.
- **Baseline:** The current Launch-Safe Check offer (report only) as sold in the 0-30 day list; its reply and booking rate per outreach measured in week 1.
- **Method:** 1. Write both offers; same price, same probes. 2. Split the week-2 outreach list by alternating assignment (A/B/A/B). 3. Record contact, variant, reply, call, booking in the ledger. 4. Compare booking rate per variant at the end of week 3. 5. Ask every booker one question: which line made you book?
- **Metric:** Bookings per contact, by variant; secondary: price accepted.
- **Threshold:** Set after measuring the week-1 baseline; declare a win only if the commitment variant's rate exceeds the baseline rate and the difference exceeds the spread seen between two halves of the baseline list (null spread).
- **Duration:** 3 weeks
- **Cost:** Owner time, roughly one day to write and send; no tooling.
- **Kill rule:** If the commitment variant books no more than the report variant after the full list, drop the recourse language and do not build the warranty product.
- **Shield risk:** Writing the perfect falsifier list instead of sending the outreach. Cap the writing at half a day.

### T2: Serve the side that bears the loss (startup, mission)

- **Hypothesis:** Acceptor-side buyers (companies that commissioned an AI-built app) book a Destroy-Only Review or Guardrails call at a higher rate than vendor-side buyers (dev shops).
- **Prediction:** Acceptor-side booking rate is higher. Confidence 60%.
- **Baseline:** Vendor-side outreach, which is the market default and the current Guardrails positioning.
- **Method:** 1. Build two lists of equal size from existing contacts and LinkedIn: companies that have an AI-built app in production, and dev shops that build with agents. 2. Send the same offer to both in the same week. 3. Record replies and booked calls per list. 4. On each call, ask who in the company feels the loss when the app fails.
- **Metric:** Booked calls per contact, per list.
- **Threshold:** Set after baseline: the vendor-side rate is the baseline; the acceptor list must beat it by more than the null spread between two random halves of the vendor list.
- **Duration:** 2 weeks
- **Cost:** Owner time, about one day.
- **Kill rule:** If both lists book at the same rate or the acceptor list books lower, keep selling to developers and remove 'acceptor' framing from the mission.
- **Shield risk:** Building a CRM before sending the first message. Use a spreadsheet.

### T3: Predict before reveal improves the owner's reviews (methodology)

- **Hypothesis:** The owner's predicted verdict, written before opening a delegate report, agrees with the final verdict more often than chance, and the stated confidence is calibrated.
- **Prediction:** Agreement above chance; confidence buckets overconfident on the first pass. Confidence 70% for above-chance, 60% for overconfidence.
- **Baseline:** Chance agreement computed from the actual verdict mix in the ledger over the last 20 reviews (e.g. if 60% of reviews end APPROVE, always guessing APPROVE scores 60%).
- **Method:** 1. Add predicted_verdict and predicted_confidence to the ledger line. 2. For every review in weeks 1-4, write the prediction before opening the report. 3. Resolve each at verdict time. 4. In week 4, compute agreement and bucket by stated confidence. 5. Also record minutes spent on the prediction.
- **Metric:** Agreement rate vs chance; calibration gap per bucket; minutes per prediction.
- **Threshold:** Chance rate from the ledger is the bar; calibration gap is reported, not thresholded, in the first month.
- **Duration:** 4 weeks, about 20 reviews (one working day each).
- **Cost:** One to two minutes per review.
- **Kill rule:** If agreement is not above chance after 20 reviews, or if predicting costs more than the reviews it changes, drop it from the brief template and do not sell the academy.
- **Shield risk:** Predicting becomes a ritual that slows reviews; the minutes field guards this.

### T4: The inquiry method does NOT help decisions (method itself; designed to fail the method)

- **Hypothesis:** Decisions made with the Operating Card produce no better outcomes than decisions made by the owner's gut, scored 30 days later.
- **Prediction:** No measurable difference in the first 20 decisions; the card changes only the write-up. Confidence 55% that the null holds.
- **Baseline:** Gut decisions, which is how most studio decisions are made today.
- **Method:** 1. For every decision above L0 in weeks 1-4, flip a coin: heads = fill the card (type, rigor, goal, constraint, three options, cheapest test, what changes my mind, stopping rule, prediction, shield); tails = decide by gut and write one line. 2. Both arms record the decision and a one-line expected outcome with a 30-day review date, before acting. 3. At day 30, a blind scorer (a model with the decision text only, or a peer) scores each outcome against its own expected outcome on the same three-point rubric (worse / as expected / better), without seeing which arm it came from. 4. Compare the arms. 5. Record minutes spent per arm.
- **Metric:** Share of decisions scored 'as expected or better' per arm; minutes per decision per arm.
- **Threshold:** None in advance; the arms are compared directly and the difference is reported beside the null spread from splitting the gut arm in two.
- **Duration:** 4 weeks to collect, plus 30 days to score.
- **Cost:** Card time per decision, measured; coin.
- **Kill rule:** If the card arm is not better after scoring, the card is demoted to L3 problems only and removed from daily use. If it is worse, the method is retired from the studio.
- **Shield risk:** This test is the shield check for the whole project. The honesty question from the Failure Log applies: outcomes are judged against the pre-written expectation, never re-interpreted.

### T5: Attention allocation by the failure registry (startup, AI)

- **Hypothesis:** Registry entries (dated, measured agent failures with a detection rule) produce more inbound requests per post than general Scars posts.
- **Prediction:** Registry entries outperform general posts on inbound. Confidence 55%.
- **Baseline:** The last five general Snaxx posts on LinkedIn/X and their inbound (replies, DMs, calls) measured in week 1.
- **Method:** 1. Publish five registry entries from the existing red-flag catalogue in CLAUDE.md, one per working day in week 3. 2. Each ends with the same call to action. 3. Track inbound per post for 7 days. 4. Compare with the baseline posts' 7-day inbound.
- **Metric:** Inbound requests per post.
- **Threshold:** Baseline from week 1; a win is more inbound per post than the best baseline post.
- **Duration:** 3 weeks
- **Cost:** Half a day of writing from existing material.
- **Kill rule:** If registry entries do not beat the baseline, the registry stays an internal attention tool and is not a marketing channel.
- **Shield risk:** Perfecting the registry schema instead of publishing five entries.

### T6: Evidence Pack as the deliverable (mission, products)

- **Hypothesis:** Clients offered a re-runnable evidence pack beside the plain report choose the pack and accept a higher price for it.
- **Prediction:** Most clients offered both choose the pack; at least some accept a higher price. Confidence 60%.
- **Baseline:** Current deliveries, which ship a report or a video without a re-runnable pack; count of the last 10 deliveries that shipped such a pack (expected zero) measured in week 1.
- **Method:** 1. Define the pack schema in one page: commands, runtime or device, artifact, falsifiers, before/after. 2. For the next three deliveries and the last five clients, offer report-only or report plus pack, with the pack priced above the report at a premium derived from its measured extra production time (hours x the studio's hourly rate). 3. Record the choice and whether anyone re-runs it (ask them to tell you). 4. Record the actual hours the pack costs.
- **Metric:** Share choosing the pack; share that re-ran it; premium accepted; pack hours.
- **Threshold:** Premium set from measured pack hours, not guessed; a win is any paid re-run.
- **Duration:** 4 weeks
- **Cost:** Pack production hours, measured.
- **Kill rule:** If no client chooses the pack and nobody re-runs one, the evidence pack is an internal quality tool, not a product, and the Proof House framing is demoted to a services line.
- **Shield risk:** Building a pack generator before shipping one pack by hand.

### T7: Regional trust signal for ICT exporters (region, mission)

- **Hypothesis:** Kosovo ICT exporters will take a call about a buyer-facing evidence mark for their EU deliveries.
- **Prediction:** Some exporters take the call and name an EU buyer who asked for proof; the mark alone does not convert without a buyer asking. Confidence 50%.
- **Baseline:** Cold outreach to the same companies with a generic dev-services offer, sent to a matched list the same week.
- **Method:** 1. Pick exporters from the STIKK member list. 2. Split into two matched lists. 3. One gets the evidence-mark offer, the other a generic offer. 4. Record calls booked and, on each call, whether a buyer has ever asked for proof. 5. Ask STIKK for a slot at an event to present the mark.
- **Metric:** Calls booked per list; count of exporters naming a buyer who asked for proof.
- **Threshold:** The generic list is the baseline; the mark offer must beat it by more than the null spread.
- **Duration:** 3 weeks
- **Cost:** One day of outreach; one event slot.
- **Kill rule:** If no exporter names a buyer who asked for proof, the mark has no pull yet; park it as a prediction in the log with a 12-month review and sell the operational products only.
- **Shield risk:** Designing the badge before anyone asked for it.

### T8: Diaspora as first export customer (region)

- **Hypothesis:** Diaspora-owned businesses in DE/CH book a discovery call for 'verified software delivery in Albanian and German' at a higher rate than for a plain dev offer.
- **Prediction:** Verified-delivery framing books more calls. Confidence 50%.
- **Baseline:** Plain dev-services offer to a matched list.
- **Method:** 1. Build two matched lists of diaspora-owned businesses (via Germin, ALBAN Global, diaspora business groups). 2. Send the two offers in the same week. 3. Record replies and booked calls. 4. On each call, ask what they fear most about commissioning software.
- **Metric:** Booked calls per contact, per list.
- **Threshold:** Plain-offer list is the baseline; the difference must beat the null spread.
- **Duration:** 3 weeks
- **Cost:** One day of outreach.
- **Kill rule:** If verified delivery does not book more calls, the Diaspora Bridge option is dropped and the diaspora stays a FJALË and COD channel only.
- **Shield risk:** Researching diaspora statistics instead of sending twenty messages.

### T9: Representation search before building (methodology)

- **Hypothesis:** Builds that start with a one-day representation search have fewer review/fix rounds than builds that start with a brief alone.
- **Prediction:** Fewer rounds, but the first month will not show it clearly because of small numbers. Confidence 50%.
- **Baseline:** The ledger's median review/fix rounds per feature-class task over the last 5+ tasks (the owner's process ledger already records this).
- **Method:** 1. For each build longer than one week in the next month, alternate: representation day first, or brief only. 2. Record the representation chosen, the rounds, wall-clock and outcome in the ledger with the parent id. 3. Compare against the class median after 4 tasks; continue to 10 tasks before deciding.
- **Metric:** Review/fix rounds per task; approved-first-time per hour (the ledger's route metric).
- **Threshold:** Class median from the ledger; judged by the section-10 route rule (replicated shift beyond null spread).
- **Duration:** 4 weeks to start; 10 tasks to decide.
- **Cost:** One day per build.
- **Kill rule:** If after 10 tasks the representation arm is not better on approved-first-time per hour, drop the mandatory day and keep it optional.
- **Shield risk:** The representation day becomes two days, then a week. Hard cap of one day, recorded.

### T10: Agents fake 'done' (AI; gives the registry its first measured number)

- **Hypothesis:** A measurable share of delegate 'done' claims fail when the original failing scenario is re-run.
- **Prediction:** The share is above zero and the owner's gut estimate, written now, is too low. Confidence 70%.
- **Baseline:** The owner's gut estimate of the false-done rate, written in the ledger in week 1 before counting.
- **Method:** 1. For 20 delegate reports in weeks 1-4, record claim (done / tests green) and the result of the owner's re-run (pass / fail / could not re-run). 2. Count false-done and could-not-re-run separately. 3. Compare to the gut estimate. 4. Publish the number with its sample count and window as registry entry one.
- **Metric:** False-done share with sample count; could-not-re-run share.
- **Threshold:** None; this is the measurement that future Guardrails claims will cite.
- **Duration:** 4 weeks
- **Cost:** Already part of every review; one extra field.
- **Kill rule:** If the false-done share is zero over 20 reports with a positive control (one deliberately broken delegate run caught), the Guardrails pitch must stop claiming agents fake success and switch to 'cost of verification'.
- **Shield risk:** None; this is the cheapest test in the set.

### T11: Problem classification is reliable enough to use (methodology; weak spot 9)

- **Hypothesis:** Two independent classifiers (owner and a model, or owner and a peer) assign the same problem type to most of the studio's recent problems.
- **Prediction:** Disagreement is common and a notable share of problems need two types. Confidence 60%.
- **Baseline:** None needed; the measure is agreement itself, with chance agreement computed from each classifier's type mix.
- **Method:** 1. List 20 real problems from the last quarter's ledger. 2. Owner classifies each into the six types without AI. 3. A model (or peer) classifies the same list blind. 4. Compute agreement and compare with chance agreement from the type mix. 5. Count problems where either side needed two types.
- **Metric:** Agreement rate vs chance; share needing two types.
- **Threshold:** Chance agreement computed from the type mix is the bar.
- **Duration:** 2 hours
- **Cost:** Negligible.
- **Kill rule:** If agreement is not above chance, drop the type box from briefs and keep only the rigor level.
- **Shield risk:** Debating the taxonomy instead of classifying 20 items.

### T12: Mission pitch survives the 'what we retracted' slide (mission, investors/partners)

- **Hypothesis:** Regional partners and diaspora investors respond at least as well to a Proof House pitch that includes a retraction slide as to the same pitch without it.
- **Prediction:** The retraction slide does not reduce second meetings, and some partners cite it as the reason to continue. Confidence 55%.
- **Baseline:** The same deck without the slide, shown to a matched set of contacts.
- **Method:** 1. Build a six-slide Proof House deck; variant B adds 'what we retracted and why' (e.g. no warranty until T1, no local VC assumption). 2. Show each variant to a matched set of contacts (ICK, STIKK, Startup Albania mentors, Germin and ALBAN Global members). 3. Record second meetings and any stated reason. 4. No model score of the deck is allowed as evidence.
- **Metric:** Second meetings per pitch, per variant; stated reasons.
- **Threshold:** Variant A is the baseline; B must not fall below it by more than the null spread.
- **Duration:** 4 weeks (starts week 3)
- **Cost:** One day for the deck; meetings.
- **Kill rule:** If the retraction slide loses meetings and nobody cites it positively, keep retractions in the prediction log but out of the deck; if the Proof House pitch itself gets no second meetings in either variant, the mission is parked and the services ladder continues alone.
- **Shield risk:** Deck polishing. Six slides, one day.

## 8. First 30 days

### Week 1

- Measure baselines before anything else: booking rate of the current Launch-Safe outreach, inbound of the last five posts, last 10 deliveries with or without an evidence pack, ledger median of review/fix rounds, owner's gut estimate of the false-done rate (written down).
- Add ledger fields: predicted_verdict, predicted_confidence, shipped, rigor_level, re_run_result. Start filling them on every review (T3, T10).
- Copy the 13 dated predictions from Pasted text 7 into a prediction log with their probabilities and deadlines; add every price and assumption in the ranked bets as predictions.
- Run T11 (classify 20 recent problems, two hours).
- Write the one-page Evidence Pack schema from the existing verdict block.
- Cash first: send the Play Deadline Upgrade and Launch-Safe offers as planned; the contract ends 31 October.

**Done when:** Every baseline number is in the ledger with its sample count and window; the prediction log has entries; the schema fits on one page.

### Week 2

- Run T1 (commitment vs report) and T2 (acceptor vs vendor) outreach in the same week, lists split by alternation.
- Start T4 coin-flip decisions and T9 representation-day alternation on the first qualifying build.
- Ship the first Evidence Pack by hand with the next delivery (T6 begins).
- Write the Amendment Rule and the shield field into CLAUDE.md; open the amendment log.

**Done when:** All outreach is sent and logged; at least one pack shipped; CLAUDE.md changes committed with a dated amendment entry.

### Week 3

- Publish five registry entries from the existing red-flag catalogue (T5).
- Run T7 (ICT exporters) and T8 (diaspora businesses) outreach with matched baseline lists.
- Build the six-slide Proof House deck with and without the retraction slide; book first partner meetings (T12).
- Ask STIKK or ICK for an event slot.

**Done when:** Five entries live; both outreach batches sent; at least one partner meeting booked.

### Week 4

- Score T1, T2, T5, T7, T8 against their baselines and null spreads; write each result in the ledger as true / false / ambiguous with the pre-written prediction beside it.
- First calibration review of T3 predicted verdicts; first count of T10 false-done share with sample count.
- Apply every kill rule as written; retract in the deck what was killed.
- Decide with the owner: continue the Proof House framing, demote to a services line, or park it. Record the decision as a prediction with a 90-day review.

**Done when:** Every test has a logged outcome or a dated 'still running' line; no PENDING outcome without a review date; the next 30-day plan cites the ledger numbers.

## 9. Warnings

- The thread's own record is the warning: 102 days, no filled prediction log, no failure entry, no amendment. If the Snaxx logs are empty at day 30, the method has become decoration and T4's kill rule applies to the whole project.
- Shield risk at company level: mission work is a comfortable way to avoid selling. The Vianova contract ends 31 October 2026; cash offers go out in week 1, and the shipped field in the ledger is checked weekly.
- Do not build the warranty: AI performance insurance has existed for years with no published volume (lesson 9). T1 tests the language; only a measured demand justifies a product.
- Regional evidence here is thin and partly second-hand: the OECD Kosovo profile returned HTTP 403, the EU AI Act readiness assessment is a .docx I did not open, Dealroom's coverage is partial, and the Albania legal guide is undated. Treat regional claims as READ or INFERRED, never as MEASURED, until the owner opens the primary documents.
- Model praise is not evidence. Do not let any model grade this plan, the deck or the Book; only the prediction log and client re-runs count. Both models in the thread rated each other 8.5-9.7/10 while nothing was tested.
- Two people cannot be an institution. The Proof House works only with partners (STIKK, ICK, Startup Albania, diaspora networks); if no partner meeting happens by week 4, the mission is parked, not pushed.
- Never invent a threshold, even under investor pressure. Every number in a deck names its script, source or arithmetic; a number that cannot is removed.
- The method itself can be gamed: a sacrificial initial preference makes the 'did it change my mind' check pass. The honesty question in the Failure Log (pre-committed or rationalized now) is answered in writing on every resolved prediction.
