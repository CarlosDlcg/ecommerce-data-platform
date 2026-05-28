CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    status VARCHAR(20)
);

INSERT INTO customers (
    name,
    email,
    registration_date,
    status
)
VALUES
('Alice Johnson', 'alice@example.com', '2024-01-10', 'active'),
('Bob Smith', 'bob@example.com', '2024-02-15', 'inactive'),
('Charlie Brown', 'charlie@example.com', '2024-03-20', 'active');