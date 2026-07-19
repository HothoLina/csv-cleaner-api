def calculate_quality_score(report):
    """
    Calculate an overall data quality score (0-100) from a report generated
    by `app.services.report.generate_report`.

    The function returns a dict with:
    - `score`: integer overall score 0-100
    - `components`: breakdown of sub-scores
    - `warnings`: list of human-readable warnings
    """
    if not isinstance(report, dict):
        raise TypeError("report must be a dict as returned by generate_report")

    rows = int(report.get("rows", 0) or 0)
    columns = int(report.get("columns", 0) or 0)
    column_names = report.get("column_names", []) or []
    missing_values = report.get("missing_values", {}) or {}
    duplicate_rows = int(report.get("duplicate_rows", 0) or 0)

    warnings = []

    if rows == 0 or columns == 0:
        return {
            "score": 0,
            "components": {
                "completeness": 0,
                "uniqueness": 0,
                "structure": 0,
            },
            "warnings": ["Empty dataset (0 rows or 0 columns)."],
        }

    total_cells = rows * columns
    missing_total = sum(int(v or 0) for v in missing_values.values())
    missing_ratio = min(1.0, missing_total / total_cells)

    completeness_score = (1.0 - missing_ratio) * 50.0

    duplicate_ratio = min(1.0, duplicate_rows / rows)
    uniqueness_score = (1.0 - duplicate_ratio) * 30.0

    bad_name_count = 0
    for name in column_names:
        if not name or (" " in name) or any(c.isupper() for c in str(name)):
            bad_name_count += 1
    structure_score = (1.0 - (bad_name_count / columns)) * 20.0

    total_score = completeness_score + uniqueness_score + structure_score
    total_score = max(0.0, min(100.0, total_score))
    score = int(round(total_score))

    if missing_ratio > 0.2:
        warnings.append(f"High missing values: {missing_ratio:.0%} of cells are missing.")
    if duplicate_ratio > 0.05:
        warnings.append(f"High duplicate rows: {duplicate_ratio:.0%} of rows are duplicates.")
    if bad_name_count > 0:
        warnings.append(f"{bad_name_count} column name(s) look non-standard.")

    return {
        "score": score,
        "components": {
            "completeness": int(round(completeness_score)),
            "uniqueness": int(round(uniqueness_score)),
            "structure": int(round(structure_score)),
        },
        "warnings": warnings,
    }
