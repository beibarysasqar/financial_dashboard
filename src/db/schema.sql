CREATE TABLE IF NOT EXISTS accounts (
  account_id SERIAL PRIMARY KEY,
  account_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS categories (
  category_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

INSERT INTO accounts (account_id, account_name)
VALUES 
(1, 'Main Account'),
(2, 'Savings'),
(3, 'Corporate Card'),
(4, 'Cash');

INSERT INTO categories (category_id, name)
VALUES 
(1, 'Sales'),
(2, 'Consulting'),
(3, 'Investments'),
(4, 'Other Income'),
(5, 'Office Supplies'),
(6, 'Rent'),
(7, 'Marketing'),
(8, 'Utilities'),
(9, 'Salaries'),
(10, 'Travel'),
(11, 'Taxes');


-- queries
SELECT tx_date, SUM(amount) as total
FROM transactions
GROUP BY tx_date
ORDER BY tx_date;


SELECT c.name, SUM(t.amount) as total
FROM transactions t
JOIN categories c ON t.category_id = c.category_id
WHERE t.amount < 0
GROUP BY c.name
ORDER BY total ASC
LIMIT 10;
