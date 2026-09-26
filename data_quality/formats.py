from __future__ import annotations

import pandas as pd


def validate_formats(df: pd.DataFrame) -> dict:
    errors = []

    if "MATRICULA" in df.columns:
        matriculas = df["MATRICULA"].astype(str)
        if not matriculas.str.fullmatch(r"\d+").all():
            errors.append("Existem valores de MATRICULA não numéricos ou com formato inesperado.")

    if "NOME" in df.columns:
        nomes_vazios = df["NOME"].fillna("").astype(str).str.strip()
        if (nomes_vazios == "").any():
            errors.append("Existem nomes vazios ou preenchidos apenas com espaços.")

    return {
        "passed": not errors,
        "errors": errors,
        "summary": {
            "matriculas_validas": bool("MATRICULA" in df.columns and df["MATRICULA"].astype(str).str.fullmatch(r"\d+").all()),
            "nomes_validos": bool("NOME" in df.columns and not (df["NOME"].fillna("").astype(str).str.strip() == "").any()),
        },
    }
