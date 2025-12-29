CREATE OR REPLACE VIEW `streaming-data-weather.fintech_analysis_ds.clean_transactions_view` AS
SELECT
  JSON_VALUE(data, '$.transaction_id') AS transaction_id,
  CAST(JSON_VALUE(data, '$.amount') AS FLOAT64) AS amount,
  CAST(JSON_VALUE(data, '$.is_anomaly_flag') AS BOOL) AS is_anomaly_flag,
  JSON_VALUE(data, '$.city') AS city,
  JSON_VALUE(data, '$.mcc_code') AS mcc_code,
  -- Logika SUBSTR untuk menghapus milidetik/zona waktu agar casting aman
  SAFE_CAST(SUBSTR(JSON_VALUE(data, '$.timestamp'), 1, 19) AS TIMESTAMP) AS transaction_time
FROM
  `streaming-data-weather.fintech_analysis_ds.transactions_stream`;