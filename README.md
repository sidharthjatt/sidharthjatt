<div align="center">

<!-- ============ HEADER (typing SVG, auto-animating) ============ -->
<a href="https://sidharthjatt.com">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&duration=3000&pause=900&color=64FFDA&center=true&vCenter=true&width=650&lines=Sidharth+Choudhary;AI+Builder+%7C+Agentic+Systems;IIT+Jodhpur+%C2%B7+Data+%26+Computational+Science" alt="Sidharth Choudhary" />
</a>

<p>
  <em>I build agents that audit models, and models that survive their own backtest.</em>
</p>

<p>
  <a href="https://sidharthjatt.com"><img src="https://img.shields.io/badge/Portfolio-sidharthjatt.com-64FFDA?style=for-the-badge&labelColor=0A192F" /></a>
  <a href="https://www.linkedin.com/in/sidharthjatt"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&labelColor=0A192F" /></a>
</p>

</div>

---

## The one-line version

Final-year **MSc–MTech Dual Degree** at **IIT Jodhpur** (Data & Computational Science, Mathematics).
I work on **agentic systems** and **quantitative research infrastructure** — the kind where the
interesting result is usually the one that *fails* honestly instead of the one that looks good.

```yaml
role:        AI Builder — agentic systems, LLM tooling
focus:       ReAct agents · evaluation & auditing · quant backtest infrastructure
principle:   "A number you cannot defend is a number you do not have."
building:    Honest Mistake · Predictive Engine (strategy series)
```

---

## <!--PIN:START-->Live from my repos<!--PIN:END-->

<!-- This block is rewritten automatically by .github/workflows/refresh.yml -->
<!--METRICS:START-->

| Repo | What it is | Stars | Last push | Latest commit |
|---|---|---|---|---|
| [`honest-mistake`](https://github.com/sidharthjatt/honest-mistake) | multi-layer ML audit agent | ⭐ 3 | 5 days ago | `Merge pull request #2 from…` |
| [`predictive-engine`](https://github.com/sidharthjatt/predictive-engine) | quant backtest thesis | ⭐ 1 | 5 days ago | `Merge pull request #2 from…` |
| [`regret-zero`](https://github.com/sidharthjatt/regret-zero) | decision-regret inventory optimizer | ⭐ 3 | 2 months ago | `Expand findings with sensitivity and…` |

<sub>Auto-refreshed by a GitHub Action · last run 04 Sep 2026, 20:21 UTC</sub>

<!--METRICS:END-->

---

## Work worth defending

### ① [Honest Mistake](https://github.com/sidharthjatt/honest-mistake) — a multi-layer ML audit agent
Public credit-risk models report **0.90+ ROC-AUC**. Most of that is post-loan leakage.
I stripped 41 leakage columns, rebuilt on a true temporal holdout, and landed at an
**honest 0.7296 AUC / 0.4404 PR-AUC** with a generalization gap of `-0.002`.

Then I built an agent to audit the model automatically:

| Layer | What it does | Status |
|---|---|---|
| **L1 — Honest baseline** | Leakage-free feature set, temporal split, SHAP audit → 3 findings | ✅ Shipped |
| **L2 — ReAct audit agent** | Raw ReAct loop (no framework), 8 read-only tools, 4 verdicts, JSONL tracing, 2 ablation switches, pgvector semantic retrieval over the data dictionary | ✅ Shipped |
| **L3 — Runtime tool generation** | Capability-gap detection → tool-spec synthesis → sandboxed exec → known-answer validation → HITL checkpoint | ⬜ Not started |

Four scored ablation runs: the planted column was caught in every canary configuration, and what varied between configurations was the false-positive count, not whether the leak was found. Numbers and limitations in [LAYER2_EVAL.md](https://github.com/sidharthjatt/honest-mistake/blob/main/outputs/agent_cache/LAYER2_EVAL.md).

`Python` · `Anthropic API` · `XGBoost` · `SHAP` · raw ReAct, deliberately no framework

---

### ② [Predictive Engine](https://github.com/sidharthjatt/predictive-engine) — quant backtest thesis
A pre-registered systematic strategy ported to **NautilusTrader**, tested for the ways it could be wrong.

- **Nifty100:** CAGR **25.36%**, Sharpe **1.88** (verified port)
- **MidCap150:** CAGR ~27–29% — and the edge **collapses** when one name is removed. That finding stays in the repo.
- Survivorship-bias module: `survivorship.py`, 50/50 tests, hard validation gate
- Pre-registered experiments **EXP18 / EXP20 / EXP21 / EXP22 — rejected.** Negative results are logged, not deleted.

`NautilusTrader` · `pandas` · pre-registration · survivorship correction

---

### ⓷ [RegretZero](https://github.com/sidharthjatt/regret-zero) — decision-regret inventory optimizer · [live demo](https://regret-zero.streamlit.app) (free-tier app sleeps when idle; ~20s to wake)
LightGBM **quantile** forecasting (P33 → P90, zero leakage) feeding a newsvendor optimizer framed around
**decision regret** rather than forecast error. Measured **+12.3% cost improvement**. Streamlit cockpit is live.

`LightGBM` · quantile regression · newsvendor optimization · `Streamlit`

---

## Stack

<div align="center">

**Languages & Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**AI / Agents**

![Anthropic](https://img.shields.io/badge/Anthropic_API-D97757?style=flat-square&logo=anthropic&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![LightGBM](https://img.shields.io/badge/LightGBM-9ACD32?style=flat-square)
![SHAP](https://img.shields.io/badge/SHAP-1F77B4?style=flat-square)

**Infra & Tooling**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white)

</div>

---

## The numbers

<div align="center">

<img height="165" src="https://github-stats-extended.vercel.app/api?username=sidharthjatt&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&title_color=64FFDA&icon_color=64FFDA&text_color=CCD6F6&bg_color=0A192F" />
<img height="165" src="https://streak-stats.demolab.com?user=sidharthjatt&hide_border=true&background=0A192F&stroke=64FFDA&ring=64FFDA&fire=FF6B6B&currStreakLabel=64FFDA&sideLabels=CCD6F6&dates=8892B0&currStreakNum=CCD6F6&sideNums=CCD6F6" />

<img height="150" src="https://github-stats-extended.vercel.app/api/top-langs/?username=sidharthjatt&layout=compact&langs_count=8&hide_border=true&title_color=64FFDA&text_color=CCD6F6&bg_color=0A192F" />

</div>

---

## Contribution graph, eaten by a snake

<div align="center">
  <img src="https://raw.githubusercontent.com/sidharthjatt/sidharthjatt/output/snake.svg" alt="snake animation" />
</div>

---

<div align="center">
  <sub>Every number on this page has a defence document behind it. Ask me for one.</sub>
</div>
