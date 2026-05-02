# 🏦 Competitive Intelligence: Stablecoin Market Dominance (USDC vs USDT)

**Tech Stack:** `SQL (Dune Analytics)` | `Python (Pandas, Matplotlib)` | `Financial Data Wrangling`

## 📝 Project Overview
Stablecoins are the backbone of the decentralized economy, serving as the primary medium of exchange. This project performs a competitive landscape analysis between the two largest fiat-backed stablecoins in the world: **USDC (Circle)** and **USDT (Tether)**. 

By querying raw ERC-20 smart contract logs (`evt_Transfer`) on the Ethereum Mainnet, this dashboard extracts and compares the daily transfer volume and transaction frequency of both assets over a 30-day period.

## 🎯 Business Value & Impact
* **Market Share Analysis:** Provides actionable intelligence on which stablecoin holds dominance in daily economic velocity.
* **Institutional vs. Retail Behavior:** Differentiates macroeconomic trends by tracking spikes in billion-dollar transfer volumes.
* **Immutable Precision:** Bypassed third-party aggregated APIs by extracting financial data directly from the blockchain source of truth, ensuring zero discrepancies.

## 📊 Methodology
1. **Data Extraction:** Identified the official contract addresses for USDC and USDT. Extracted raw transfer logs using Dune Analytics SQL engine.
2. **Decimal Normalization:** Applied `/ 1e6` division directly within the SQL pipeline to convert raw blockchain integers into readable USD formats.
3. **Data Pivoting & Visualization:** Utilized Python's `Pandas` to pivot the timeseries data and `Matplotlib` to render a comparative trend analysis.

## 📂 Repository Structure
* `stablecoin_market_share.sql`: Core extraction logic hitting the Ethereum raw event tables.
* `stablecoin_dashboard.py`: Python visualization script with custom Y-axis formatting for billions/millions ($B/$M).
* `stablecoin_market_share_dashboard.png`: The final visual output.

## 🚀 How to Reproduce
1. Clone this repository.
2. Install requirements: 
   ```bash
   pip install pandas matplotlib dune-client
