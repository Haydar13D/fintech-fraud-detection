CREATE OR REPLACE TABLE `streaming-data-weather.fintech_analysis_ds.transactions_stream` (
  data STRING,
  publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);