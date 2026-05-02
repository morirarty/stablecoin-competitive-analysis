# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dune-client==1.10.0",
#     "marimo>=0.23.4",
#     "matplotlib==3.10.8",
#     "pandas==3.0.2",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from dune_client.client import DuneClient

    # ==========================================
    # 1. DUNE API CONFIGURATION
    # ==========================================
    DUNE_API_KEY = "iEuaSNBZeMLZcwoqQdAqWa1uVUgyQ8d3"
    QUERY_ID = 7412109  # Replace with your Stablecoin Market Share Query ID

    print("Fetching data from Dune Analytics server...")
    dune = DuneClient(DUNE_API_KEY)
    result = dune.get_latest_result(QUERY_ID)

    df = pd.DataFrame(result.result.rows)

    # ==========================================
    # 2. DATA WRANGLING & PIVOTING
    # ==========================================
    df['transfer_date'] = pd.to_datetime(df['transfer_date'])

    # Pivot data so USDC and USDT become separate columns for visualization
    df_pivot = df.pivot(index='transfer_date', columns='stablecoin_type', values='daily_transfer_volume_usd').fillna(0)

    # ==========================================
    # 3. DATA VISUALIZATION
    # ==========================================
    print("Building competitive landscape dashboard...")

    fig, ax = plt.subplots(figsize=(12, 6))

    # Draw two competing trend lines
    ax.plot(df_pivot.index, df_pivot['USDC'], label='USDC Volume (USD)', color='#2775CA', linewidth=2.5, marker='o')
    ax.plot(df_pivot.index, df_pivot['USDT'], label='USDT Volume (USD)', color='#26A17B', linewidth=2.5, marker='o')

    # Format Y-axis to display numbers in Billions/Millions format (B/M)
    formatter = ticker.FuncFormatter(lambda x, pos: f'${x*1e-9:.1f}B' if x >= 1e9 else f'${x*1e-6:.0f}M')
    ax.yaxis.set_major_formatter(formatter)

    # Basic layout design
    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel('Daily Transfer Volume (USD)', fontweight='bold')
    plt.title('Stablecoin Market Share: USDC vs USDT Daily Transfer Volume', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', frameon=True, shadow=True)
    ax.grid(True, linestyle='--', alpha=0.6)
    fig.autofmt_xdate()

    # Save the final output
    plt.savefig('stablecoin_market_share_dashboard.png', dpi=300, bbox_inches='tight')
    print("Success! Image saved as 'stablecoin_market_share_dashboard.png'")

    plt.show()
    return


if __name__ == "__main__":
    app.run()
