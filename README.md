Real-Time Log Analytics & Anomaly Detection

A Python and PySpark-based log analytics project that simulates server log generation, processes structured log data using Apache Spark, performs request and error analysis, detects unusual server activity using rule-based conditions, and provides an interactive Streamlit dashboard.

## Overview

This project simulates server/application logs and processes them using PySpark.

Each generated log contains:

- Timestamp
- IP address
- Endpoint
- HTTP status code
- Response time

The processed data is analyzed to understand request patterns, errors, response times, and potential anomalies.

## Features

- Simulated server log generation
- Structured log data processing with PySpark
- Request count analysis
- Successful and failed request analysis
- Error-rate calculation
- Endpoint usage analysis
- HTTP status-code distribution
- Response-time statistics
- Slow-request detection
- Rule-based anomaly detection
- Anomaly reason classification
- CSV export of processed logs
- CSV export of detected anomalies
- Streamlit dashboard for interactive analysis
- Matplotlib-based visualizations

## Technology Stack

- Python
- Apache Spark
- PySpark
- Pandas
- Streamlit
- Matplotlib

## Log Data

The project generates structured log records containing:

| Field | Description |
|---|---|
| `timestamp` | Time at which the log was generated |
| `ip_address` | Simulated client IP address |
| `endpoint` | Requested application endpoint |
| `status_code` | HTTP response status code |
| `response_time_ms` | Response time in milliseconds |

Example endpoints:

```text
/
 /products
 /cart
 /checkout
 /login
 /contact
