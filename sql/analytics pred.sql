CREATE OR REPLACE VIEW `streaming-data-weather.fintech_analysis_ds.prediction_view` AS
SELECT
  transaction_id,
  amount,
  city,
  transaction_time,
  is_anomaly_flag,
  -- Mengambil probabilitas spesifik untuk label 'TRUE'
  (SELECT prob FROM UNNEST(predicted_is_anomaly_flag_probs) WHERE label = true) AS probability_of_fraud
FROM
  ML.PREDICT(
    MODEL `streaming-data-weather.fintech_analysis_ds.anomaly_detection_model`,
    (SELECT * FROM `streaming-data-weather.fintech_analysis_ds.clean_transactions_view`)
  );