SELECT

    id AS order_id,

    "userId" AS customer_id,

    date AS order_date,

    products,

    processed_at

FROM {{ source('staging', 'orders') }}