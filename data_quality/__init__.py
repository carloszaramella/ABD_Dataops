from .schema import validate_schema
from .volume import validate_volume
from .values import validate_values
from .numeric_dates import validate_numeric_ranges
from .formats import validate_formats
from .uniqueness import validate_uniqueness
from .referential_integrity import validate_referential_integrity


def validate_all(df, min_rows=10):
    results = {
        "schema": validate_schema(df),
        "volume": validate_volume(df, min_rows=min_rows),
        "values": validate_values(df),
        "numeric_ranges": validate_numeric_ranges(df),
        "formats": validate_formats(df),
        "uniqueness": validate_uniqueness(df, column="MATRICULA"),
        "referential_integrity": validate_referential_integrity(df),
    }

    failed = [name for name, result in results.items() if not result.get("passed", False)]
    return {
        "passed": not failed,
        "failed_checks": failed,
        "results": results,
    }


__all__ = [
    "validate_all",
    "validate_schema",
    "validate_volume",
    "validate_values",
    "validate_numeric_ranges",
    "validate_formats",
    "validate_uniqueness",
    "validate_referential_integrity",
]
