from __future__ import annotations

import pandas as pd


def validate_referential_integrity(df: pd.DataFrame) -> dict:
    errors = []

    for i in range(1, 5):
        nota_col = f"NOTA_MAT_{i}"
        repro_col = f"REPROVACOES_MAT_{i}"

        if nota_col not in df.columns or repro_col not in df.columns:
            continue

        subset = df[[nota_col, repro_col]].dropna()
        problema = subset[(subset[nota_col] < 4) & (subset[repro_col] == 0)]
        if not problema.empty:
            errors.append(
                f"Há inconsistência entre {nota_col} e {repro_col}: notas baixas sem reprovação na matéria {i}."
            )

    return {
        "passed": not errors,
        "errors": errors,
        "summary": {"checked_subjects": list(range(1, 5))},
    }
