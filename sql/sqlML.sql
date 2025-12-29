CREATE OR REPLACE MODEL `streaming-data-weather.fintech_analysis_ds.anomaly_detection_model`
OPTIONS(
  model_type='logistic_reg',
  input_label_cols=['is_anomaly_flag']
) AS
SELECT
  amount,
  city,
  mcc_code,
  is_anomaly_flag
FROM
  `streaming-data-weather.fintech_analysis_ds.clean_transactions_view`
WHERE
  transaction_time IS NOT NULL;