from __future__ import annotations

import pandas as pd


def validate_volume(df: pd.DataFrame, min_rows: int = 10) -> dict:
    errors = []

    if df is None:
        return {"passed": False, "errors": ["DataFrame ausente."], "summary": {"rows": 0, "min_rows": min_rows}}

    rows = int(len(df))

    if rows == 0:
        errors.append("DataFrame vazio após a carga.")

    if rows < min_rows:
        errors.append(f"Volume abaixo do esperado: {rows} linhas (mínimo {min_rows}).")

    return {
        "passed": not errors,
        "errors": errors,
        "summary": {"rows": rows, "min_rows": min_rows},
    }
