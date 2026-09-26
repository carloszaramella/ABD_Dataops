from __future__ import annotations

import pandas as pd


def validate_uniqueness(df: pd.DataFrame, column: str = "MATRICULA") -> dict:
    errors = []

    if column not in df.columns:
        return {
            "passed": False,
            "errors": [f"Coluna {column} não encontrada."],
            "summary": {"column": column, "unique_count": 0},
        }

    unique_count = int(df[column].nunique())
    total_rows = int(len(df))

    if not df[column].is_unique:
        errors.append(f"Existem valores duplicados em {column}.")

    return {
        "passed": not errors,
        "errors": errors,
        "summary": {"column": column, "unique_count": unique_count, "total_rows": total_rows},
    }
