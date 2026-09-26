from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

from data_quality import validate_all


def resolve_dataset_path() -> Path:
    candidates = [
        Path("/opt/airflow/ml/curso.txt"),
        Path("/opt/airflow/project/ml/curso.txt"),
        Path("./ml/curso.txt"),
        Path("../ml/curso.txt"),
        Path("ml/curso.txt"),
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    raise FileNotFoundError("Arquivo ml/curso.txt não encontrado para a DAG do Airflow.")


def run_quality_checks():
    dataset_path = resolve_dataset_path()
    df = pd.read_csv(dataset_path)
    result = validate_all(df, min_rows=10)

    if not result["passed"]:
        raise ValueError(f"Data quality checks falharam: {result['failed_checks']}")

    print(f"Dataset validado em: {dataset_path}")
    print(result)


with DAG(
    dag_id="data_quality_checks",
    description="Valida qualidade dos dados usando as mesmas regras do notebook",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["data-quality", "fiap"],
) as dag:

    validate_task = PythonOperator(
        task_id="validate_data_quality",
        python_callable=run_quality_checks,
    )

    validate_task
