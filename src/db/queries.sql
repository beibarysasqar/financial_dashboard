WITH revenue AS (
    SELECT date_trunc('month', date::timestamp) AS month, SUM(revenue - discount) AS total_revenue
    FROM transactions
    GROUP BY month
),
expenses AS (
    SELECT date_trunc('month', date::timestamp) AS month, SUM(amount) AS total_expenses
    FROM expenses
    GROUP BY month 
)
SELECT
    r.month,
    r.total_revenue,
    e.total_expenses,
    r.total_revenue - e.total_expenses AS profit,
    ROUND(((r.total_revenue - e.total_expenses) / r.total_revenue) * 100, 2) AS profit_margin
FROM revenue r
LEFT JOIN expenses e USING (month)
ORDER BY r.month;
