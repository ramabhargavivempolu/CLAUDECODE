# Airflow Project

A data pipeline orchestration project using Apache Airflow that demonstrates modern asset-based DAG orchestration. The project implements a weather data pipeline with cross-DAG dependencies.

---

## Project Overview

This project implements a two-stage data pipeline:
1. **Data Fetch DAG** - Fetches weather data from an API, transforms it, and materializes it as an asset
2. **Data Report DAG** - Consumes the materialized asset and performs analysis

The DAGs use **Asset-based orchestration**, a modern Airflow feature that allows DAGs to depend on asset outputs rather than explicit task dependencies, enabling loosely coupled workflows.

---

## Project Structure

```
Airflow_Project/
├── dags/
│   ├── data_fetch.py       # Producer DAG - fetches and materializes weather data
│   ├── data_report.py      # Consumer DAG - analyzes materialized data
│   └── __pycache__/        # Python cache (auto-generated)
├── .env                    # Environment configuration
└── README.md               # This file
```

---

## DAGs Overview

### 1. **data_fetch.py** (Producer DAG)

**Purpose**: Fetches weather data, transforms it, and materializes it as an Asset.

**Workflow**:
```
prepare_storage → fetch_api_data → transform_data → materialize_asset
```

**Tasks**:
- **prepare_storage**: Creates the storage directory (`/opt/airflow/data`) where data will be stored
- **fetch_api_data**: Simulates an API call and returns weather data (city, temperature, unit)
- **transform_data**: Adds metadata to the raw data:
  - `processed_at`: ISO timestamp of processing
  - `status`: "cleansed"
- **materialize_asset**: Writes the transformed data to a JSON file and registers it as an Asset
  - Outlet: `weather_data_asset` (URI: `file:///opt/airflow/data/weather_report.json`)

**Output**: JSON file with weather data at `/opt/airflow/data/weather_report.json`

---

### 2. **data_report.py** (Consumer DAG)

**Purpose**: Consumes the asset produced by `data_fetch` DAG and performs analysis.

**Schedule**: Triggered automatically when the `weather_data_asset` is materialized (Asset-based trigger)

**Tasks**:
- **read_asset**: Reads the weather data from the asset file and prints analysis

**Input**: Depends on `weather_data_asset` produced by `data_fetch` DAG

---

## Key Features

### Asset-Based Orchestration
- **Modern Approach**: Uses Airflow's Asset objects for cross-DAG dependencies
- **Loose Coupling**: DAGs don't know about each other directly; they communicate through Assets
- **Automatic Triggering**: `data_report` is automatically triggered when `weather_data_asset` is materialized

### Data Pipeline Pattern
- **Extract**: Fetch data from external API (simulated)
- **Transform**: Enrich data with metadata
- **Load**: Materialize data as a persistent Asset

---

## Configuration

### Environment Variables
- `AIRFLOW_UID`: Set to `50000` in `.env` (used for container/permission management)

### Asset Definition
```python
weather_data_asset = Asset(uri="file:///opt/airflow/data/weather_report.json")
```

This asset is:
- **Produced** by: `data_fetch` DAG (in the `materialize_asset` task)
- **Consumed** by: `data_report` DAG (as a schedule trigger)

---

## Sample Data Flow

1. **data_fetch DAG executes**:
   - Simulates fetching: `{"city": "New York", "temp": 22, "unit": "C"}`
   - Transforms to:
     ```json
     {
       "city": "New York",
       "temp": 22,
       "unit": "C",
       "processed_at": "2026-03-13T12:30:45.123456",
       "status": "cleansed"
     }
     ```
   - Materializes to: `/opt/airflow/data/weather_report.json`

2. **data_report DAG triggers automatically**:
   - Reads the JSON file
   - Prints analysis: `"Analyzing data for New York: 22°C"`

---

## How to Run

### Prerequisites
- Apache Airflow installed and configured
- Python 3.8+
- Required permissions for `/opt/airflow/data` directory

### Setup
1. Place this project in your Airflow `DAGS_FOLDER`
2. Load the `.env` file for environment configuration
3. Initialize or refresh the Airflow database

### Execution
```bash
# Trigger the producer DAG
airflow dags trigger data_fetch

# The consumer DAG will automatically trigger after the asset is materialized
# Or manually trigger:
airflow dags trigger data_report
```

### Monitoring
```bash
# View DAG runs
airflow dags list
airflow dags show data_fetch
airflow dags show data_report

# View task logs
airflow tasks logs data_fetch prepare_storage
```

---

## Architecture Diagram

```
┌─────────────────────────────────┐
│      data_fetch DAG             │
├─────────────────────────────────┤
│  prepare_storage                │
│         ↓                       │
│  fetch_api_data                 │
│         ↓                       │
│  transform_data                 │
│         ↓                       │
│  materialize_asset ─→ Asset     │
└─────────────────────────────────┘
          │
          │ (Asset-based trigger)
          ↓
┌─────────────────────────────────┐
│      data_report DAG            │
├─────────────────────────────────┤
│  read_asset                     │
└─────────────────────────────────┘
```

---

## Future Enhancements

- Replace simulated API call with real weather API (e.g., OpenWeatherMap)
- Add data validation and error handling
- Implement logging and monitoring with Prometheus/Grafana
- Add multiple data sources and assets
- Create scheduling for periodic data fetches
- Add data quality checks before materialization
- Implement data archival and retention policies

---

## Notes

- The simulated API returns hardcoded weather data for New York
- Asset files are stored locally; for production, consider cloud storage (S3, GCS, etc.)
- The project uses Airflow's modern `@dag` and `@task` decorators (TaskFlow API)

---

## References

- [Airflow TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
- [Airflow Asset-Based Orchestration](https://airflow.apache.org/docs/apache-airflow/stable/concepts/datasets.html)
- [Airflow Documentation](https://airflow.apache.org/docs/)

---

**Last Updated**: 2026-03-13
