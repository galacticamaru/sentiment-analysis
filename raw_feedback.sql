SELECT
    customer_feedback
    , customer_feedback_timestamp
FROM {{table_name}}
WHERE customer_feedback_timestamp BETWEEN {{input_start_date}} AND {{input_end_date}} and
(
    {{sql_keywords|sqlsafe}}
);
