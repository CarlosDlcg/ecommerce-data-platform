SELECT
    product_id,
    name,
    category,
    price,
    supplier,
    processed_at

FROM {{ source('staging', 'products') }}