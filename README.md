<div align="center">

<!-- ============ HEADER (typing SVG, auto-animating) ============ -->
<a href="https://sidharthjatt.com">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&duration=3000&pause=900&color=64FFDA&center=true&vCenter=true&width=650&lines=Sidharth+Choudhary;AI+Builder+%7C+Agentic+Systems;IIT+Jodhpur+%C2%B7+Data+%26+Computational+Science" alt="Sidharth Choudhary" />
</a>

<p>
  <em>I build AI systems, then I try to break them.</em>
</p>

<p>
  <a href="https://sidharthjatt.com"><img src="https://img.shields.io/badge/Portfolio-sidharthjatt.com-64FFDA?style=for-the-badge&labelColor=0A192F" /></a>
  <a href="https://www.linkedin.com/in/sidharthjatt"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&labelColor=0A192F" /></a>
</p>

</div>

---

## The one-line version

Final-year **MSc–MTech Dual Degree** at **IIT Jodhpur** (Data & Computational Science, Mathematics).
I work on **agentic systems** and **quantitative research infrastructure**: agents that audit models,
models that say when they're unsure, and a trading strategy I keep testing for the ways it could be fooling me.
The interesting result is usually the one that *fails* honestly, not the one that looks good.

```yaml
role:        AI Builder — agentic systems, LLM tooling
focus:       ReAct agents · model auditing · cost-aware ML · quant backtest infrastructure
principle:   "A number you cannot defend is a number you do not have."
shipped:     Reasonable Doubt · Honest Mistake · RegretZero
ongoing:     Predictive Engine (M.Tech thesis, strategy one of a series)
```

---

## <!--PIN:START-->Live from my repos<!--PIN:END-->

<!-- This block is rewritten automatically by .github/workflows/refresh.yml -->
<!--METRICS:START-->

| Repo | What it is | Stars | Last commit | Latest commit message |
|---|---|---|---|---|
| [`reasonable-doubt`](https://github.com/sidharthjatt/reasonable-doubt) | contract-clause classifier on a CPU | ⭐ 4 | 3 days ago | `docs: note that section letter 3bo was never used` |
| [`honest-mistake`](https://github.com/sidharthjatt/honest-mistake) | multi-layer ML audit agent | ⭐ 5 | 15 hours ago | `D26: decided after the design pass, not fixed` |
| [`predictive-engine`](https://github.com/sidharthjatt/predictive-engine) | stock-ranking thesis, NSE | ⭐ 4 | 1 hour ago | `Record why the same-day assessment fix is kept` |
| [`regret-zero`](https://github.com/sidharthjatt/regret-zero) | decision-regret inventory optimizer | ⭐ 5 | 4 days ago | `Fix machine reference order in README` |

<sub>Auto-refreshed by a GitHub Action · last run 23 Sep 2026, 10:56 UTC</sub>

<!--METRICS:END-->

---

## Work worth defending

### ① [Reasonable Doubt](https://github.com/sidharthjatt/reasonable-doubt): a contract-clause classifier that says when it isn't sure
[Live demo](https://reasonable-doubt-111680840326.asia-south1.run.app) (scales to zero, so the first request after a quiet spell takes about 2 minutes) · [model on Hugging Face](https://huggingface.co/sidharthjatt/reasonable-doubt-deberta-ledgar)

Sorts a contract clause into one of LEDGAR's 100 provision types, on a CPU, for **$0.00088 per thousand**.
Macro-F1 **0.8091** on 3,000 held-out clauses. Claude Sonnet 5 zero-shot scored 0.6148 on the same rows, at **496×** the cost.

- I planned a three-tier cascade and measured each tier before trusting it. A QLoRA-tuned Qwen2.5-1.5B lost to the encoder. Sending the low-confidence rows to Sonnet 5 moved macro-F1 by +0.0008, with a confidence interval across zero. Both tiers were dropped. What ships is one DeBERTa-v3 in ONNX with a `needs_review` flag.
- The INT8 build of the same weights scored **0.000166** on CPUs without AVX-512 VNNI. That's chance, and it raised no error. So the service classifies 200 fixed rows at startup and won't answer until they pass.
- Where it fails: 10 of 20 non-contract paragraphs came back confident. A data-access policy got labelled `Records` at 99.9%. It's in the [report](https://github.com/sidharthjatt/reasonable-doubt/blob/main/REPORT.md).

`DeBERTa-v3` · `ONNX Runtime` · `FastAPI` · `Docker` · `Cloud Run` · pre-registration

---

### ② [Honest Mistake](https://github.com/sidharthjatt/honest-mistake): a multi-layer ML audit agent
[Browse the benchmark](https://sidharthjatt.github.io/honest-mistake/) · [run the audit yourself](https://sidharthjatt.github.io/honest-mistake/scan.html) (your own Anthropic key, billed to you, never stored)

Public credit-risk models on the Lending Club data report **0.90+ ROC-AUC**. Most of that is post-loan leakage.
I stripped 41 leakage columns, rebuilt on a true temporal holdout, and landed at an
**honest 0.7296 AUC / 0.4404 PR-AUC**. Validation-to-test gap: `−0.0023`.

Then I built an agent to audit the model without being told what to look for:

| Layer | What it does | Status |
|---|---|---|
| **L1: Honest baseline** | Leakage-free feature set, temporal split, SHAP audit with 3 findings | ✅ Shipped |
| **L2: ReAct audit agent** | Raw ReAct loop (no framework), 8 read-only tools, 2 ablation switches, pgvector semantic search over the data dictionary | ✅ Shipped |
| **L3: Runtime tool generation** | Prompt caching (input cost −71.1% on one measured run), a sandbox with a known-answer validator, a gap detector that was *not* accepted, and one generated tool admitted to a registry with its limits written down. The chain never ran end to end. Four planned parts were cut because nothing real was there to test them against | 🟡 Partly built |

Twelve live runs, eight usable. I planted a leaking column as a canary and the agent caught it in every canary configuration.
What changed between configurations was the false-positive count, not whether the leak was found.
The canary's description gives it away, so this shows a floor, not a ceiling.
Numbers and limitations are in [LAYER2_EVAL.md](https://github.com/sidharthjatt/honest-mistake/blob/main/outputs/agent_cache/LAYER2_EVAL.md) and [REPORT.md](https://github.com/sidharthjatt/honest-mistake/blob/main/REPORT.md).

`Python` · `Anthropic API` · `XGBoost` · `SHAP` · `pgvector` · raw ReAct, deliberately no framework

---

### ③ [Predictive Engine](https://github.com/sidharthjatt/predictive-engine): a stock-ranking strategy for Indian markets (M.Tech thesis)
Every 20 trading days a 10-seed LightGBM ensemble ranks the universe. The top eight names are held, sized inverse to volatility,
and the whole book is scaled by market breadth. Decisions are made on the close and filled at the next open, with Zerodha's
real delivery charges and 15 bps of slippage. Strategy one of a planned series on the same data.

- **Twenty-five ideas tested, one accepted** (holding eight names instead of twelve). Every rejection is in [`EXPERIMENTS.md`](https://github.com/sidharthjatt/predictive-engine/blob/main/experiments/EXPERIMENTS.md) with the accept rule written before the run.
- **Drawdown is the part that holds.** Shipping arm max drawdown −21.87% against −38.65% for equal-weight buy & hold on Nifty 100, and −20.01% against −37.73% on MidCap150 (Jan 2019 to Jun 2026).
- **The return edge doesn't, and I measured that.** The shipping arm loses to its own basket on Nifty 100 and beats it on MidCap150. Re-runs on slightly perturbed prices flip that sign in both universes, so neither sign is quoted as established.
- **NautilusTrader port** matches the research engine on 93 of 93 rebalances at zero tolerance on both live universes. That proves bookkeeping and timing, not execution: there's no order book.
- **Survivorship bias is unresolved.** Membership is today's index taken back to 2019. Point-in-time membership only exists from March 2024.

`LightGBM` · `NautilusTrader` · `pandas` · pre-registration

---

### ④ [RegretZero](https://github.com/sidharthjatt/regret-zero): a decision-regret inventory optimizer
[Live demo](https://regret-zero.streamlit.app) (free-tier app sleeps when idle; about 30 seconds to wake)

Two years of transactions from a UK online giftware retailer. LightGBM **quantile** forecasting (P33 to P90, strict date split,
rolling features shifted so no week sees itself) feeds a newsvendor rule that orders for the cost of being wrong, not for forecast error.

- Over 12 held-out weeks, it lost **£54,631 less** than ordering the median forecast: a **12.0%** saving. All three price tiers came out ahead.
- The P90 forecast covers 91.7% of actual demand against a 90% target.
- The costs are assumptions, so they're sliders in the app. The saving holds until holding cost reaches about 26% of unit price per week (default is 10%).

`LightGBM` · quantile regression · newsvendor optimization · `Streamlit`

---

## Stack

<div align="center">

**Languages & Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**AI / ML**

![Anthropic](https://img.shields.io/badge/Anthropic_API-D97757?style=flat-square&logo=anthropic&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![ONNX](https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![LightGBM](https://img.shields.io/badge/LightGBM-9ACD32?style=flat-square)
![SHAP](https://img.shields.io/badge/SHAP-1F77B4?style=flat-square)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat-square)

**Quant**

![NautilusTrader](https://img.shields.io/badge/NautilusTrader-0A192F?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**Infra & Tooling**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Cloud Run](https://img.shields.io/badge/Cloud_Run-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
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
  <sub>Every number on this page is copied from its repository, where the caveats sit right next to it.</sub>
</div>
