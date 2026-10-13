"""Build the Inquiry Engine site from analysis/*.json.
python3 -I site/build.py   (run from the repo root or anywhere)
"""
import json, os
from html import escape as E

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "analysis")
OUT = os.path.join(ROOT, "site", "dist")
os.makedirs(OUT, exist_ok=True)
X = json.load(open(os.path.join(A, "01_extraction.json")))
AP_PATH = os.path.join(A, "02_application.json")
AP = json.load(open(AP_PATH)) if os.path.exists(AP_PATH) else None

PHASES = {
    "1-discovery-engine": ("Discovery Engine", "1 Jul", "p1"),
    "2-retrospective-pdf": ("Looking back", "2 Jul", "p2"),
    "3-book-of-inquiry": ("Book of Inquiry", "6 Jul", "p3"),
    "4-daily-practice": ("Daily practice", "10 Jul", "p4"),
    "5-archive-verdict": ("Verdict", "11 Oct", "p5"),
}
PAGES = [("index.html", "Overview"), ("ideas.html", "Ideas"), ("prompts.html", "Prompts"), ("lessons.html", "Lessons"),
         ("apply.html", "Apply to Snaxx"), ("mission.html", "Mission"), ("tests.html", "Tests")]

CSS = """
/* Layout: a field notebook for a method. Overview first, then one idea-type per page. Phase colours tag provenance. */
:root{
  --bg:#eef0f3;--surface:#fbfcfd;--sunk:#e3e7ec;--line:#d3d9e0;
  --ink:#121820;--ink-2:#444d59;--muted:#6b7480;--accent:#3346c8;
  --p1:#2a78d6;--p2:#eb6834;--p3:#1baf7a;--p4:#eda100;--p5:#e87ba4;
  --good:#1f6f4a;--warn:#8a5a12;--bad:#a33a2a;
  --f-display:"Literata",Georgia,"Times New Roman",serif;
  --f-body:"IBM Plex Sans","Helvetica Neue",Arial,system-ui,sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#12161b;--surface:#1a1f26;--sunk:#222830;--line:#2f363f;--ink:#eceff3;--ink-2:#b6bdc6;--muted:#8b939d;--accent:#8c9bff;
  --p1:#3987e5;--p2:#d95926;--p3:#199e70;--p4:#c98500;--p5:#d55181;--good:#6fcf9d;--warn:#e0b064;--bad:#f08a78;color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#12161b;--surface:#1a1f26;--sunk:#222830;--line:#2f363f;--ink:#eceff3;--ink-2:#b6bdc6;--muted:#8b939d;--accent:#8c9bff;
  --p1:#3987e5;--p2:#d95926;--p3:#199e70;--p4:#c98500;--p5:#d55181;--good:#6fcf9d;--warn:#e0b064;--bad:#f08a78;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15.5px/1.6 var(--f-body);margin:0}
.wrap{max-width:1100px;margin:0 auto;padding-inline:20px;padding-block:0 72px}
h1,h2,h3{font-family:var(--f-display);font-weight:600;text-wrap:balance;margin:0;letter-spacing:-.005em}
h1{font-size:clamp(32px,5vw,50px);line-height:1.08}
h2{font-size:26px;line-height:1.2}
h3{font-size:18px;line-height:1.3}
p{margin:0}
a{color:inherit;text-underline-offset:2px;text-decoration-color:var(--muted)}
nav.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);display:flex;gap:4px;overflow-x:auto;padding-block:10px;border-bottom:1px solid var(--line)}
nav.top .brand{font:600 15px var(--f-display);padding:7px 12px 7px 0;white-space:nowrap}
nav.top a{font:500 14px var(--f-body);color:var(--ink-2);text-decoration:none;border:1px solid transparent;border-radius:6px;padding:7px 12px;white-space:nowrap}
nav.top a[aria-current="page"]{color:var(--ink);background:var(--surface);border-color:var(--line)}
a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.tag{font:600 11px var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.lede{color:var(--ink-2);max-width:66ch;font-size:17px}
.page{display:grid;gap:26px;padding-top:26px}
.eli5{background:var(--sunk);border-radius:10px;padding:18px 20px;display:grid;gap:8px}
.eli5 p{font:400 19px/1.5 var(--f-display);max-width:62ch}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
@media (max-width:860px){.grid3{grid-template-columns:1fr}}
@media (max-width:760px){.grid2{grid-template-columns:1fr}}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px;display:grid;gap:10px;align-content:start;min-width:0}
.card p{font-size:14.5px}
.muted{color:var(--muted)} .ink2{color:var(--ink-2)}
.chip{font:600 10.5px var(--f-mono);letter-spacing:.05em;text-transform:uppercase;border:1px solid var(--line);border-radius:4px;padding:1px 6px;color:var(--ink-2);white-space:nowrap}
.dot{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:baseline}
.timeline{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
@media (max-width:900px){.timeline{grid-template-columns:1fr}}
.timeline li{background:var(--surface);border:1px solid var(--line);border-top-width:5px;border-radius:10px;padding:14px;display:grid;gap:6px;align-content:start}
.timeline .n{font:600 13px var(--f-mono);color:var(--muted)}
.timeline .q{font-size:13.5px;color:var(--ink-2)}
.timeline .u{font-size:14px;border-top:1px dashed var(--line);padding-top:8px}
.verdict{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media (max-width:760px){.verdict{grid-template-columns:1fr}}
.vbox{border-radius:10px;padding:14px;display:grid;gap:4px;background:var(--surface);border:1px solid var(--line);border-left-width:5px}
.vbox.good{border-left-color:var(--good)} .vbox.mid{border-left-color:var(--warn)} .vbox.bad{border-left-color:var(--bad)}
.vbox b{font:600 17px var(--f-display)}
.best{border:2px solid var(--accent);border-radius:12px;padding:18px 20px;background:var(--surface);display:grid;gap:6px}
.best p{font:500 20px/1.45 var(--f-display)}
.pagecards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
.pagecard{display:grid;gap:4px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px;text-decoration:none}
.pagecard:hover{border-color:var(--ink-2)}
.pagecard b{font:600 17px var(--f-display)}
.pagecard span{font-size:13px;color:var(--ink-2)}
.idea{display:grid;gap:8px}
.idea .plain{font:400 17px/1.5 var(--f-display)}
.obj{border-left:3px solid var(--warn);padding-left:10px;font-size:14px;color:var(--ink-2)}
ol.steps{margin:0;padding-left:20px;display:grid;gap:4px;font-size:14px}
pre{white-space:pre-wrap;word-break:break-word;background:var(--sunk);border-radius:8px;padding:12px;margin:0;font:12.8px/1.55 var(--f-mono);color:var(--ink)}
.btn{font:500 13px var(--f-body);background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:6px 10px;cursor:pointer;justify-self:start}
.btn:hover{background:var(--sunk)}
blockquote{margin:0;font:italic 400 17px/1.5 var(--f-display);border-left:3px solid var(--line);padding-left:14px}
blockquote footer{font:400 12px var(--f-mono);font-style:normal;color:var(--muted);margin-top:4px}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:8px;border-bottom:1px solid var(--line);vertical-align:top}
th{font:600 11.5px var(--f-mono);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
td.num{font-variant-numeric:tabular-nums;text-align:center;font:600 15px var(--f-mono)}
.tbl{overflow-x:auto}
.vs{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:0;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.vs > div{padding:14px;display:grid;gap:6px;align-content:start}
.vs .mk{background:var(--sunk)} .vs .iq{background:var(--surface)}
@media (max-width:640px){.vs{grid-template-columns:1fr}}
.move{border-top:1px solid var(--line);padding:12px 14px;background:var(--surface);grid-column:1/-1;font-size:14.5px}
.test{display:grid;gap:10px}
.tgrid{display:grid;grid-template-columns:150px minmax(0,1fr);gap:6px 14px;font-size:14px}
@media (max-width:560px){.tgrid{grid-template-columns:1fr}}
.tgrid dt{font:600 11px var(--f-mono);text-transform:uppercase;letter-spacing:.05em;color:var(--muted);padding-top:3px}
.tgrid dd{margin:0}
.pred{background:var(--sunk);border-radius:8px;padding:10px 12px;font-size:14.5px}
.kill{border-left:3px solid var(--bad);padding-left:10px}
.rec{border:2px solid var(--accent)}
.weeks{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
@media (max-width:860px){.weeks{grid-template-columns:1fr}}
.weeks li{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:6px;align-content:start}
.weeks ul{margin:0;padding-left:18px;font-size:14px;display:grid;gap:4px}
.note{font-size:13px;color:var(--muted);max-width:75ch}
.reg{font:600 10.5px var(--f-mono);letter-spacing:.05em}
.reg.MEASURED{color:var(--good)} .reg.READ{color:var(--accent)} .reg.INFERRED{color:var(--warn)}
.toc{display:flex;flex-wrap:wrap;gap:8px}
.toc a{font-size:13.5px;background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:5px 9px;text-decoration:none}
section[id]{scroll-margin-top:70px}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;600&display=swap">'
COPY_JS = r"""document.querySelectorAll("button[data-copy]").forEach(b=>b.addEventListener("click",()=>{const pre=document.getElementById(b.dataset.copy);const t=pre.textContent;const ok=()=>{b.textContent="Copied";setTimeout(()=>b.textContent="Copy",1500)};const sel=()=>{const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent="Selected, press Copy"};if(navigator.clipboard)navigator.clipboard.writeText(t).then(ok,sel);else sel()}));"""

def nav(cur):
    links = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f == cur else ""}>{E(n)}</a>' for f, n in PAGES)
    return f'<nav class="top" aria-label="Pages"><span class="brand">Inquiry Engine</span>{links}</nav>'

def page(fname, title, body, script="", first=False):
    head = f"<title>{E(title)}</title>{FONTS}<style>{CSS}</style>"
    content = f'<div class="wrap">{nav(fname)}<main class="page">{body}</main></div>' + (f"<script>{script}</script>" if script else "")
    html = head + content if first else ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' + head + "</head><body>" + content + "</body></html>")
    open(os.path.join(OUT, fname), "w").write(html)

def phase_tag(ph):
    name, date, var = PHASES.get(ph, (ph, "", "p1"))
    return f'<span class="chip"><span class="dot" style="background:var(--{var})"></span>{E(name)} · {E(date)}</span>'

def phase_of(src):
    for k in PHASES:
        if k in (src or ""): return k
    return None

def reg(r):
    r = (r or "INFERRED").upper()
    return f'<span class="reg {E(r)}">{E(r)}</span>'

def pending(what):
    return f'<div class="card"><p class="muted">{E(what)} is being written. Republish after the application pass finishes.</p></div>'

# ---------- index ----------
V = X["verdict"]
arc = "".join(f'''<li style="border-top-color:var(--{PHASES[a["phase"]][2]})"><span class="n">{i} · {E(PHASES[a["phase"]][1])}</span><h3>{E(PHASES[a["phase"]][0])}</h3>
<p class="q"><b>Question.</b> {E(a["driving_question"][:260])}</p><p class="u"><b>Unlocked.</b> {E(a["unlock"][:320])}</p></li>''' for i, a in enumerate(X["arc"], 1))
eli5 = AP["summary_eli5"] if AP else "A long chat with ChatGPT and Claude turned one question into a method for thinking. The method says: guess first, test against reality, and let the idea shrink when it is wrong. The method is strong. It has not been tested on a real unknown problem yet."
cards = "".join(f'<a class="pagecard" href="{f}"><b>{E(n)}</b><span>{E(d)}</span></a>' for f, n, d in [
    ("ideas.html", "Ideas", f"{len(X['core_ideas'])} core ideas and {len(X['frameworks'])} frameworks, in plain words."),
    ("prompts.html", "Prompts", f"{len(X['prompts'])} prompts in the order they were used, and {len(X['quotes'])} quotes."),
    ("lessons.html", "Lessons", f"{len(X['lessons'])} lessons by depth, and {len(X['weak_spots'])} weak spots to check."),
    ("apply.html", "Apply to Snaxx", "Think differently from the market: startup, method, AI."),
    ("mission.html", "Mission", "A mission bigger than SaaS, for the region and for investors."),
    ("tests.html", "Tests", "Tests that can prove each idea wrong, with predictions written first.")])
body = f"""
<header style="display:grid;gap:10px"><span class="tag">From the thread “Project Planning with LLM” · 1 Jul – 11 Oct 2026 · 198 messages, 24 files</span>
<h1>Inquiry Engine</h1>
<p class="lede">How one question about planning with a very smart AI turned into a method for finding truth, and what Snaxx Tech can do with it. Read by Fable and checked against the source files.</p></header>
<div class="eli5"><span class="tag">In simple words</span><p>{E(eli5)}</p></div>
<div><h2>Is it profound?</h2><p class="note" style="margin-top:6px">Fable's honest verdict after reading 100% of the material.</p></div>
<div class="verdict">
 <div class="vbox good"><span class="tag">Profound</span><b>The path and the tools</b><p class="ink2" style="font-size:14px">Two AI models attacking each other's answers while you route. A thesis that shrank three times under pressure. A method with its own budget, abuse check and change rule.</p></div>
 <div class="vbox mid"><span class="tag">Known elsewhere</span><b>Most of the theory</b><p class="ink2" style="font-size:14px">{E(V["what_is_known_elsewhere"][:330])}</p></div>
 <div class="vbox bad"><span class="tag">Not proven</span><b>No real use yet</b><p class="ink2" style="font-size:14px">102 days of material, and the prediction, calibration and failure logs are still empty templates. By the book's own rule, it is decoration until it is used on a problem with an unknown answer.</p></div>
</div>
<div class="best"><span class="tag">The single best idea</span><p>{E(V["single_best_idea"])}</p></div>
<div><h2>How the thinking moved</h2><p class="note" style="margin-top:6px">Five phases, in order. Each colour marks a phase on every page.</p></div>
<ol class="timeline">{arc}</ol>
<details class="card"><summary class="btn">Read Fable's full verdict</summary><p style="margin-top:10px">{E(V["is_it_profound"])}</p><p><b>What is new.</b> {E(V["what_is_new"])}</p></details>
<div><h2>Pages</h2></div><div class="pagecards">{cards}</div>
<p class="note">Source files live in the repo folder inquiry-engine/sources/, by phase. This site holds no secrets; the thread had none.</p>"""
page("index.html", "Inquiry Engine", body, first=True)

# ---------- ideas ----------
ideas = "".join(f'''<article class="card idea"><div style="display:flex;gap:6px;flex-wrap:wrap">{phase_tag(phase_of(c["source"]))}<span class="chip">{E(c["kind"])}</span></div>
<h3>{E(c["name"])}</h3><p class="plain">{E(c["plain"])}</p><p><b>Why it is deep.</b> {E(c["why_deep"])}</p><p class="obj"><b>Strongest objection.</b> {E(c["strongest_objection"])}</p><p class="note">Source: {E(c["source"])}</p></article>''' for c in X["core_ideas"])
fw = "".join(f'''<article class="card"><h3>{E(f["name"])}</h3><p class="ink2"><b>Use it when:</b> {E(f["when_to_use"])}</p><ol class="steps">{"".join(f"<li>{E(s)}</li>" for s in f["steps"])}</ol><p class="note">Source: {E(f["source"])}</p></article>''' for f in X["frameworks"])
page("ideas.html", "Ideas · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Ideas</h1><p class="lede">The {len(X['core_ideas'])} core ideas in plain words, each with its strongest objection. Then the {len(X['frameworks'])} frameworks as step lists you can use.</p>
<div class="toc"><a href="#core">Core ideas</a><a href="#frameworks">Frameworks</a></div></header>
<section id="core" style="display:grid;gap:14px"><h2>Core ideas</h2><div class="grid2">{ideas}</div></section>
<section id="frameworks" style="display:grid;gap:14px"><h2>Frameworks</h2><div class="grid2">{fw}</div></section>""")

# ---------- prompts ----------
order = list(PHASES)
ps = sorted(X["prompts"], key=lambda p: order.index(p["phase"]) if p["phase"] in order else 9)
pr = "".join(f'''<article class="card"><div style="display:flex;gap:6px;flex-wrap:wrap">{phase_tag(p["phase"])}<span class="chip">{"you" if p["author"] == "owner" else E(p["author"])}</span></div>
<h3>{i}. {E(p["title"])}</h3><p class="ink2">{E(p["purpose"])}</p><pre id="p{i}">{E(p["text"])}</pre><button class="btn" data-copy="p{i}">Copy</button>
<p><b>Why it works.</b> {E(p["why_it_works"])}</p><p class="obj"><b>How it fails.</b> {E(p["failure_mode"])}</p></article>''' for i, p in enumerate(ps, 1))
qs = "".join(f'<blockquote>{E(q["text"])}<footer>{E(q["source"])}</footer></blockquote>' for q in X["quotes"])
page("prompts.html", "Prompts · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Prompts</h1><p class="lede">{len(X['prompts'])} prompts in the order they were used. Your own short questions drove the whole climb, so they are here next to the long prompts ChatGPT wrote.</p>
<div class="toc"><a href="#list">Prompts</a><a href="#quotes">Quotes</a></div></header>
<section id="list" style="display:grid;gap:14px">{pr}</section>
<section id="quotes" style="display:grid;gap:16px"><h2>Quotes</h2><p class="note">All {len(X['quotes'])} were checked: each appears word for word in the source files.</p>{qs}</section>""", COPY_JS)

# ---------- lessons ----------
ls = sorted(X["lessons"], key=lambda l: -l["depth"])
lrows = "".join(f'<tr><td class="num">{l["depth"]}</td><td><b>{E(l["lesson"])}</b><br><span class="ink2">{E(l["plain"])}</span></td><td><span class="chip">{E(l["transfers_to"])}</span></td></tr>' for l in ls)
wk = "".join(f'<article class="card"><h3>{E(w["claim"])}</h3><p class="obj"><b>Problem.</b> {E(w["problem"])}</p><p><b>How to check.</b> {E(w["how_to_check"])}</p></article>' for w in X["weak_spots"])
page("lessons.html", "Lessons · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Lessons</h1><p class="lede">{len(X['lessons'])} lessons, deepest first. Depth 5 means it changes how you would run a company or a research program.</p>
<div class="toc"><a href="#lessons">Lessons</a><a href="#weak">Weak spots</a></div></header>
<section id="lessons"><div class="tbl"><table><thead><tr><th style="width:56px">Depth</th><th>Lesson</th><th>Applies to</th></tr></thead><tbody>{lrows}</tbody></table></div></section>
<section id="weak" style="display:grid;gap:14px"><h2>Weak spots</h2><p class="note">Claims in the thread that need checking before anyone relies on them.</p><div class="grid2">{wk}</div></section>""")

# ---------- apply / mission / tests (from application pass) ----------
if AP:
    dt = "".join(f'''<article style="display:grid;gap:0"><h3 style="margin-bottom:8px">{E(d["name"])}</h3><div class="vs"><div class="mk"><span class="tag">How the market thinks</span><p>{E(d["market_default"])}</p></div><div class="iq"><span class="tag">How the method thinks</span><p>{E(d["inquiry_way"])}</p></div><div class="move"><b>Snaxx move.</b> {E(d["snaxx_move"])} <span class="note">· from: {E(d["source_idea"])}</span></div></div></article>''' for d in AP["different_thinking"])
    me = "".join(f'<article class="card"><h3>{E(m["practice"])}</h3><p class="ink2"><b>Why.</b> {E(m["why"])}</p><p><b>Install.</b> {E(m["install"])}</p><p class="note">From: {E(m["from_idea"])}</p></article>' for m in AP["methodology"])
    ai = "".join(f'<article class="card"><h3>{E(a["thesis"])}</h3><p>{E(a["implication"])}</p><p>{reg(a.get("reg"))}</p></article>' for a in AP["ai_view"])
    pr2 = "".join(f'<article class="card"><h3>{E(p["name"])}</h3><p>{E(p["what"])}</p><p class="ink2"><b>Who pays.</b> {E(p["who_pays"])}</p><p class="ink2"><b>Why not generic SaaS.</b> {E(p["why_not_generic_saas"])}</p><p class="pred"><b>First test.</b> {E(p["first_test"])}</p></article>' for p in AP["products"])
    page("apply.html", "Apply to Snaxx · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Apply to Snaxx</h1><p class="lede">“If we think like the market, we are like them.” Each pair shows the usual startup move, the method's move, and what Snaxx does next.</p>
<div class="toc"><a href="#think">Think differently</a><a href="#method">Our methodology</a><a href="#ai">AI as a whole</a><a href="#products">Products</a></div></header>
<section id="think" style="display:grid;gap:18px"><h2>Think differently</h2>{dt}</section>
<section id="method" style="display:grid;gap:14px"><h2>Our methodology</h2><div class="grid2">{me}</div></section>
<section id="ai" style="display:grid;gap:14px"><h2>AI as a whole</h2><div class="grid2">{ai}</div></section>
<section id="products" style="display:grid;gap:14px"><h2>Products that are not generic SaaS</h2><div class="grid2">{pr2}</div></section>""")
    MS = AP["mission"]
    opts = "".join(f'''<article class="card{" rec" if o["name"] == MS["recommended"] else ""}"><div>{'<span class="chip" style="border-color:var(--accent);color:var(--accent)">Recommended</span>' if o["name"] == MS["recommended"] else ""}</div><h3>{E(o["name"])}</h3><p style="font:500 17px/1.45 var(--f-display)">{E(o["statement"])}</p>
<p><b>Why the region.</b> {E(o["why_region"])}</p><p><b>Why investors.</b> {E(o["why_investors"])}</p><p><b>Cash engine.</b> {E(o["cash_engine"])}</p><p><b>Moat.</b> {E(o["moat"])}</p><p class="kill"><b>Kill test.</b> {E(o["kill_test"])}</p></article>''' for o in MS["options"])
    rg = "".join(f'<tr><td><b>{E(r["gap"])}</b></td><td>{E(r["evidence"])} {reg(r.get("reg"))}{(" · <a href=" + chr(34) + E(r["url"]) + chr(34) + " target=_blank rel=noopener>source</a>") if r.get("url") else ""}</td><td>{E(r["move"])}</td></tr>' for r in AP["region"])
    wks = "".join(f'<li><span class="tag">Week {E(str(w["week"]))}</span><ul>{"".join(f"<li>{E(a)}</li>" for a in w["actions"])}</ul><p class="note"><b>Done when:</b> {E(w["done_when"])}</p></li>' for w in AP["first_30_days"])
    nots = "".join(f"<li>{E(x)}</li>" for x in MS.get("what_not_to_do", []))
    warns = "".join(f"<li>{E(x)}</li>" for x in AP["warnings"])
    page("mission.html", "Mission · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Mission</h1><p class="lede">Three mission options that go beyond SaaS, with the one Fable recommends. SaaS and agency work pay for it; the mission is what investors and the region can join.</p>
<div class="toc"><a href="#options">Options</a><a href="#region">Region</a><a href="#plan">First 30 days</a><a href="#warn">Warnings</a></div></header>
<div class="best"><span class="tag">Recommended · north-star metric</span><p>{E(MS["recommended"])}: {E(MS["rationale"])}</p><p class="ink2" style="font:400 15px var(--f-body)"><b>North star.</b> {E(MS["north_star_metric"])}</p></div>
<section id="options" style="display:grid;gap:14px"><h2>Options</h2><div class="grid3">{opts}</div><div class="card"><h3>What not to do</h3><ul style="margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px">{nots}</ul></div></section>
<section id="region" style="display:grid;gap:14px"><h2>The region</h2><p class="note">Facts marked MEASURED or READ have a source; INFERRED is judgement.</p><div class="tbl"><table><thead><tr><th>Gap</th><th>Evidence</th><th>Snaxx move</th></tr></thead><tbody>{rg}</tbody></table></div></section>
<section id="plan" style="display:grid;gap:14px"><h2>First 30 days</h2><ol class="weeks">{wks}</ol></section>
<section id="warn" style="display:grid;gap:10px"><h2>Warnings</h2><ul style="margin:0;padding-left:18px;display:grid;gap:6px">{warns}</ul></section>""")
    ts = "".join(f'''<article class="card test" id="{E(t["id"])}"><div style="display:flex;gap:8px;align-items:baseline;flex-wrap:wrap"><span class="chip">{E(t["id"])}</span><h3>{E(t["idea"])}</h3></div>
<p style="font:500 16.5px/1.45 var(--f-display)">{E(t["hypothesis"])}</p><div class="pred"><span class="tag">Prediction, written before the test</span><p>{E(t["prediction"])}</p></div>
<dl class="tgrid"><dt>Baseline</dt><dd>{E(t["baseline"])}</dd><dt>Method</dt><dd>{E(t["method"])}</dd><dt>Metric</dt><dd>{E(t["metric"])}</dd><dt>Threshold</dt><dd>{E(t["threshold"])}</dd><dt>Duration · cost</dt><dd>{E(t["duration"])} · {E(t["cost"])}</dd><dt>Kill rule</dt><dd class="kill">{E(t["kill_rule"])}</dd><dt>Shield risk</dt><dd class="ink2">{E(t["shield_risk"])}</dd></dl></article>''' for t in AP["tests"])
    toc = "".join(f'<a href="#{E(t["id"])}">{E(t["id"])} {E(t["idea"][:38])}</a>' for t in AP["tests"])
    page("tests.html", "Tests · Inquiry Engine", f"""<header style="display:grid;gap:8px"><h1>Tests</h1><p class="lede">Each idea gets a test that can prove it wrong. Write the prediction before you run it. Compare with a baseline. Stop when the kill rule fires.</p>
<div class="eli5"><span class="tag">The rule behind every test</span><p>Guess first and write the guess down. Then look at what really happened. The difference between the two is what you learn.</p></div>
<div class="toc">{toc}</div></header><section style="display:grid;gap:14px">{ts}</section>""")
else:
    for f, n in [("apply.html", "Apply to Snaxx"), ("mission.html", "Mission"), ("tests.html", "Tests")]:
        page(f, f"{n} · Inquiry Engine", f"<header><h1>{E(n)}</h1></header>{pending(n)}")
print("built", sorted(os.listdir(OUT)), "application:", bool(AP))
