SELECT

    customer_id,
    name,
    email,
    registration_date,
    status,

    dbt_valid_from,
    dbt_valid_to,

    CASE
        WHEN dbt_valid_to IS NULL
        THEN true
        ELSE false
    END AS is_current

FROM {{ ref('customers_snapshot') }}