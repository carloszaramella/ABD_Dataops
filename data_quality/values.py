from __future__ import annotations

import pandas as pd

PERFIL_ESPERADO = {"EXCELENTE", "MUITO BOM", "MUITO_BOM", "BOM", "REGULAR", "DIFICULDADE"}


def normalize_profile(value):
    return str(value).replace("_", " ").strip()


def validate_values(df: pd.DataFrame) -> dict:
    errors = []

    if "PERFIL" in df.columns:
        perfis_normalizados = df["PERFIL"].dropna().astype(str).map(normalize_profile)
        perfis_invalidos = set(perfis_normalizados.unique()) - {"EXCELENTE", "MUITO BOM", "BOM", "REGULAR", "DIFICULDADE"}
        if perfis_invalidos:
            errors.append(f"Valores inválidos em PERFIL: {sorted(perfis_invalidos)}")

    if "INGLES" in df.columns:
        ingles_validos = set(df["INGLES"].dropna().unique())
        if not ingles_validos.issubset({0.0, 1.0}):
            errors.append(f"Valores inesperados em INGLES: {sorted(ingles_validos)}")

    return {
        "passed": not errors,
        "errors": errors,
        "summary": {
            "perfis_unicos": sorted(df["PERFIL"].dropna().astype(str).map(normalize_profile).unique()) if "PERFIL" in df.columns else [],
            "ingles_unicos": sorted(df["INGLES"].dropna().unique()) if "INGLES" in df.columns else [],
        },
    }
