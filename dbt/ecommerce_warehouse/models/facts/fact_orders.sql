SELECT

    order_id,
    customer_id,
    order_date,
    processed_at

FROM {{ ref('stg_orders') }}