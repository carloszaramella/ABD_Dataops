from __future__ import annotations

import pandas as pd

EXPECTED_COLUMNS = [
    "MATRICULA",
    "NOME",
    "REPROVACOES_MAT_1",
    "REPROVACOES_MAT_2",
    "REPROVACOES_MAT_3",
    "REPROVACOES_MAT_4",
    "NOTA_MAT_1",
    "NOTA_MAT_2",
    "NOTA_MAT_3",
    "NOTA_MAT_4",
    "INGLES",
    "H_AULA_PRES",
    "TAREFAS_ONLINE",
    "FALTAS",
    "PERFIL",
]

NUMERIC_COLUMNS = [
    "MATRICULA",
    "REPROVACOES_MAT_1",
    "REPROVACOES_MAT_2",
    "REPROVACOES_MAT_3",
    "REPROVACOES_MAT_4",
    "NOTA_MAT_1",
    "NOTA_MAT_2",
    "NOTA_MAT_3",
    "NOTA_MAT_4",
    "INGLES",
    "H_AULA_PRES",
    "TAREFAS_ONLINE",
    "FALTAS",
]


def validate_schema(df: pd.DataFrame) -> dict:
    errors = []

    if df is None or df.empty and len(df.columns) == 0:
        return {"passed": False, "errors": ["DataFrame vazio ou inexistente."], "summary": {}}

    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    unexpected = [col for col in df.columns if col not in EXPECTED_COLUMNS]

    if missing:
        errors.append(f"Colunas ausentes: {missing}")
    if unexpected:
        errors.append(f"Colunas inesperadas: {unexpected}")

    for col in NUMERIC_COLUMNS:
        if col in df.columns and not pd.api.types.is_numeric_dtype(df[col]):
            errors.append(f"Coluna {col} não é numérica.")

    if "NOME" in df.columns and not (
        pd.api.types.is_string_dtype(df["NOME"]) or pd.api.types.is_object_dtype(df["NOME"])
    ):
        errors.append("Coluna NOME não parece ser texto.")

    if "PERFIL" in df.columns and not (
        pd.api.types.is_string_dtype(df["PERFIL"]) or pd.api.types.is_object_dtype(df["PERFIL"])
    ):
        errors.append("Coluna PERFIL não parece ser texto.")

    summary = {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

    return {
        "passed": not errors,
        "errors": errors,
        "summary": summary,
    }
