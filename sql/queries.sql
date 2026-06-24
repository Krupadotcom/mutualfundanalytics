-- 1. View sample NAV records
SELECT * FROM fact_nav LIMIT 5;

-- 2. Average NAV by fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total transaction count
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- 4. SIP transactions
SELECT *
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 5. Redemption transactions
SELECT *
FROM fact_transactions
WHERE transaction_type = 'REDEMPTION';

-- 6. High value transactions
SELECT *
FROM fact_transactions
WHERE amount_inr > 50000;

-- 7. Scheme performance data
SELECT *
FROM fact_performance;

-- 8. Top funds by 1-year return
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 9. Lowest expense ratio funds
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 5;

-- 10. Risk and return comparison
SELECT amfi_code,
       return_1yr_pct,
       expense_ratio_pct
FROM fact_performance;