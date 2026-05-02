-- =========================================================================
-- Query Name: Competitive Intelligence - USDC vs USDT Market Share
-- Description: Tracks daily transfer volume and transaction count to evaluate
--              stablecoin dominance on the Ethereum Mainnet.
-- =========================================================================

SELECT 
    DATE_TRUNC('day', evt_block_time) AS transfer_date,
    CASE 
        -- USDC Smart Contract Address
        WHEN contract_address = 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 THEN 'USDC'
        -- USDT Smart Contract Address
        WHEN contract_address = 0xdac17f958d2ee523a2206206994597c13d831ec7 THEN 'USDT'
    END AS stablecoin_type,
    COUNT(evt_tx_hash) AS daily_transaction_count,
    -- Divide by 1e6 because both USDC and USDT use 6 decimal places
    SUM(value) / 1e6 AS daily_transfer_volume_usd
FROM erc20_ethereum.evt_Transfer
WHERE evt_block_time >= NOW() - INTERVAL '30' DAY
  AND contract_address IN (
      0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48, 
      0xdac17f958d2ee523a2206206994597c13d831ec7  
  )
GROUP BY 1, 2
ORDER BY 1 DESC, 2;