{% snapshot customers_snapshot %}

{{
    config(
        target_schema='analytics',
        unique_key='customer_id',

        strategy='check',

        check_cols=[
            'name',
            'email',
            'status'
        ]
    )
}}

SELECT
    customer_id,
    name,
    email,
    registration_date,
    status,
    processed_at

FROM {{ ref('stg_customers') }}

{% endsnapshot %}