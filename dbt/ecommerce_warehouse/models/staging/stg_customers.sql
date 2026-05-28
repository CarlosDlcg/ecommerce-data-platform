SELECT
    customer_id,
    name,
    email,
    registration_date,
    status,
    processed_at

FROM {{ source('staging', 'customers') }}