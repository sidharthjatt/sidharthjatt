<h1 align="center">Sidharth Choudhary</h1>

<p align="center">
  <b>AI Builder</b> · MSc–MTech, Data & Computational Science · IIT Jodhpur<br/>
  <em>I build AI systems, then I try to break them.</em>
</p>

<p align="center">
  <a href="https://sidharthjatt.com"><img src="https://img.shields.io/badge/Portfolio-sidharthjatt.com-64FFDA?style=for-the-badge&labelColor=0A192F" /></a>
  <a href="https://www.linkedin.com/in/sidharthjatt"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&labelColor=0A192F" /></a>
</p>

---

I'm in the final year of a dual degree at IIT Jodhpur, in the Mathematics specialisation. I build agentic systems and
quantitative research tooling, and I spend about as long trying to break them as building them.

All four projects below are public, and each one says where it fails: a quantised model that returned
chance-level answers without raising an error, a leak detector that only proves a floor, a trading edge that
didn't survive its own re-runs. I'd rather show that than quote a number I can't defend.

JAM 2023: top 1.2% of 13,333 candidates · Department rank 4

## At a glance

| Project | The question | What came out | Try it |
|---|---|---|---|
| [**Reasonable Doubt**](https://github.com/sidharthjatt/reasonable-doubt) | Can a small model sort contract clauses as well as a frontier LLM, for far less? | **0.8091** macro-F1 at **$0.00088** per 1,000 clauses. Claude Sonnet 5 zero-shot got 0.6148 at 496× the cost | [live demo](https://reasonable-doubt-111680840326.asia-south1.run.app) |
| [**Honest Mistake**](https://github.com/sidharthjatt/honest-mistake) | What does a credit model score with the leakage removed, and can an agent find leaks without being told where to look? | Honest **0.7296** ROC-AUC. The agent caught a planted leak in every canary configuration | [run the audit](https://sidharthjatt.github.io/honest-mistake/scan.html) |
| [**Predictive Engine**](https://github.com/sidharthjatt/predictive-engine) | Can a stock-ranking model survive real Indian market costs, and how would I know if it's luck? | Drawdown a little over half of buy & hold's. The return edge is *not* established, and the repo shows why | [experiment record](https://github.com/sidharthjatt/predictive-engine/blob/main/experiments/EXPERIMENTS.md) |
| [**RegretZero**](https://github.com/sidharthjatt/regret-zero) | Why judge an inventory forecast on RMSE when running short and overstocking cost different amounts? | **£54,631 (12.0%)** less lost over 12 held-out weeks | [live demo](https://regret-zero.streamlit.app) |

---

## The projects

### Reasonable Doubt: a contract-clause classifier that says when it isn't sure

LEDGAR has about 80,000 contract provisions from SEC filings, labelled into 100 types. I planned a three-tier cascade
and measured each tier before trusting it. Two of the three didn't earn their place, so what ships is one fine-tuned
DeBERTa-v3 in ONNX, on a CPU, with a flag on answers it isn't sure about.

- A QLoRA-tuned Qwen2.5-1.5B lost to the encoder. Sending the doubtful rows to Sonnet 5 moved macro-F1 by +0.0008, with a confidence interval across zero. Both tiers were dropped.
- The INT8 build of the same weights scored **0.000166** on CPUs without AVX-512 VNNI. That's chance, and nothing raised an error. The service now classifies 200 fixed rows at startup and won't answer until they pass.
- It still fails on text that isn't a contract: 10 of 20 unrelated paragraphs came back confident. That's in the [report](https://github.com/sidharthjatt/reasonable-doubt/blob/main/REPORT.md).

<sub>DeBERTa-v3 · QLoRA · ONNX Runtime · FastAPI · Docker · Cloud Run · [model on Hugging Face](https://huggingface.co/sidharthjatt/reasonable-doubt-deberta-ledgar) · the demo scales to zero, so the first request can take about 2 minutes</sub>

### Honest Mistake: a credit model built without leakage, and an agent that tries to catch it cheating

Public models on the Lending Club data report AUCs above 0.90, mostly by reading columns written after the loan closed.
I found and removed 41 of them in three passes (name patterns, the data dictionary, and asking why one column was
almost always empty), then tested once on a year the model never saw.

- **Layer 1, the model:** XGBoost on 1,061,042 loans. ROC-AUC 0.7296, PR-AUC 0.4404, and a validation-to-test gap of −0.0023.
- **Layer 2, the agent:** a plain ReAct loop on the Anthropic API, no framework, with eight read-only tools and pgvector search over the data dictionary. The prompt never mentions leakage. Of twelve live runs, eight were usable, and in every run where a leaking column had been planted, the agent caught it. The planted column's description gives it away, though, so this proves a floor, not a ceiling.
- **Layer 3, generated tools:** prompt caching cut input cost 71.1% on one measured run. One generated tool passed a sandbox and was admitted to a registry. Four planned parts were cut because nothing real was there to test them against. The [report](https://github.com/sidharthjatt/honest-mistake/blob/main/REPORT.md) says what that does and doesn't show.

<sub>XGBoost · SHAP · Optuna · Anthropic API · pgvector · Postgres · [benchmark site](https://sidharthjatt.github.io/honest-mistake/) · the live audit runs on your own API key, which is never stored</sub>

### Predictive Engine: a stock-ranking strategy for Indian markets (M.Tech thesis, ongoing)

Every 20 trading days a 10-seed LightGBM ensemble ranks the universe. The top eight names are held, sized inverse to
volatility, and the book is scaled by market breadth. Orders fill at the next open, with Zerodha's real charges and
15 bps of slippage. Twenty-five ideas have been tested against it and one was accepted. Every rejection is kept, with
the accept rule written before the run.

- **What holds:** max drawdown of −21.87% against −38.65% for equal-weight buy & hold on Nifty 100, and −20.01% against −37.73% on MidCap150 (Jan 2019 to Jun 2026).
- **What doesn't:** the strategy loses to its own basket on Nifty 100 and beats it on MidCap150, and re-runs on slightly perturbed prices flip that sign in both. So I don't quote the return edge as real.
- **Verified port:** the execution path is ported to NautilusTrader and matches the research engine on 93 of 93 rebalances at zero tolerance. That proves bookkeeping and timing, not execution, because there's no order book.
- **Still open:** survivorship bias. Index membership is today's list taken back to 2019, and point-in-time data only exists from March 2024.

<sub>LightGBM · NautilusTrader · pandas · pre-registration</sub>

### RegretZero: inventory ordering scored on money lost, not on forecast error

Two years of transactions from a UK online giftware retailer. LightGBM predicts five demand quantiles directly, with a
strict date split and rolling features shifted so no week sees itself. Each product then orders the quantile where
the cost of running short balances the cost of a leftover unit.

- Over 12 held-out weeks it lost **£54,631 less** than ordering the median forecast, a 12.0% saving, and all three price tiers came out ahead.
- The P90 forecast covers 91.7% of actual demand against a 90% target.
- The costs are assumptions, so they're sliders in the app. The saving holds until holding cost reaches about 26% of unit price per week, against a default of 10%.

<sub>LightGBM · quantile regression · newsvendor optimisation · Streamlit</sub>

---

## How I work

- **Rules before results.** An experiment's accept rule is written down before it runs. When a rule turns out wrong, the fix goes in as a dated amendment, not an edit.
- **Failures stay in the record.** Dropped tiers, cut layers and rejected ideas are kept next to the ones that passed, with the numbers.
- **Other people can check it.** Each project is public. Three are live, and the fourth publishes its code, experiment record and results, though a rerun needs 396 MB of vendor price data that isn't in the repo.

**Tools I use most:** Python, SQL/PostgreSQL · PyTorch, Hugging Face, ONNX Runtime, XGBoost, LightGBM, SHAP · Anthropic API, pgvector · NautilusTrader, pandas · Docker, FastAPI, Cloud Run, GitHub Actions, Streamlit

---

## Recent work

<!-- This block is rewritten automatically by .github/workflows/refresh.yml -->
<!--METRICS:START-->

| Repo | What it is | Commits, last 30 days | Last commit |
|---|---|---:|---|
| [`reasonable-doubt`](https://github.com/sidharthjatt/reasonable-doubt) | contract-clause classifier on a CPU | 141 | 4 days ago |
| [`honest-mistake`](https://github.com/sidharthjatt/honest-mistake) | multi-layer ML audit agent | 93 | 1 day ago |
| [`predictive-engine`](https://github.com/sidharthjatt/predictive-engine) | stock-ranking thesis, NSE | 242 | 11 hours ago |
| [`regret-zero`](https://github.com/sidharthjatt/regret-zero) | decision-regret inventory optimizer | 14 | 5 days ago |

<sub>Auto-refreshed by a GitHub Action · last run 23 Sep 2026, 21:09 UTC</sub>

<!--METRICS:END-->

<sub>Every project number on this page is copied from that project's repository, where the caveats sit right next to it.</sub>
