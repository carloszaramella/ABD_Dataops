from __future__ import annotations

import pandas as pd


def validate_numeric_ranges(df: pd.DataFrame) -> dict:
    errors = []

    notas_cols = [f"NOTA_MAT_{i}" for i in range(1, 5)]
    for col in notas_cols:
        if col not in df.columns:
            continue
        validas = df[col].dropna()
        if not validas.empty and not validas.between(0, 10).all():
            errors.append(f"Valores fora do intervalo esperado em {col}: {validas.min()} a {validas.max()}")

    nao_negativas = [
        "REPROVACOES_MAT_1",
        "REPROVACOES_MAT_2",
        "REPROVACOES_MAT_3",
        "REPROVACOES_MAT_4",
        "H_AULA_PRES",
        "TAREFAS_ONLINE",
        "FALTAS",
    ]
    for col in nao_negativas:
        if col not in df.columns:
            continue
        valores = df[col].fillna(0)
        if (valores < 0).any():
            errors.append(f"Valores negativos encontrados em {col}.")

    summary = {}
    for col in notas_cols:
        if col in df.columns:
            summary[col] = {
                "min": float(df[col].min()) if df[col].notna().any() else None,
                "max": float(df[col].max()) if df[col].notna().any() else None,
            }

    return {
        "passed": not errors,
        "errors": errors,
        "summary": summary,
    }
