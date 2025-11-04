CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    account_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    category_name SERIAL PRIMARY KEY,
    name TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS transactions(
    transactions_id BIGSERIAL PRIMARY KEY,
    tx_date DATE NOT NULL,
    account_id INT REFERENCES account(account_id),
    category_id INT REFERENCES categories(category_id),
    amount NUMERIC(12,2) NOT NULL, 
    currency TEXT DEFAULT 'USD',
    descrption TEXT
);

CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions (tx_date);