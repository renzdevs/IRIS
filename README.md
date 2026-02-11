# Iris

<p align="center">
  <img src="./iris.png" alt="IRIS logo" width="220">
</p>


A trading bot that **learns in public**.

Iris trades small, documents everything, and improves after every win/loss.
The output is a living diary: entries, decisions, and what changed.

---

## Concept

- Give Iris a wallet
- Give Iris rules + constraints
- Let her scan markets, pick entries, size risk, and execute
- After every trade: **write a diary entry**
- Keep the loop running

The goal isn't "one lucky trade" — it's compounding skill.

---

## What Iris Does

**Discovery**
- Coingecko / GMGN / Dexscreener for listings + momentum
- Solscan / Basescan for onchain checks

**Decision**
- Defines a thesis
- Lists signals + invalidation
- Chooses an entry plan

**Execution**
- Places the trade
- Logs it

**Reflection**
- What worked
- What failed
- What rule changed (if any)

---

## Repo Layout

```
iris/
  README.md
  docs/
    playbook.md
    rules.md
    resources.md
  diary/
    000_template.md
  logs/
    trades.csv
  scripts/
    new_entry.py
```

---

## How to Use This Repo

This is a **tracking + documentation** repo by design.

1. Clone repo
2. Add a new diary entry for each session/trade
3. Keep trades in `logs/trades.csv`
4. Update `docs/rules.md` when a rule changes

---

## Disclaimer

Not financial advice. This is an experiment.
