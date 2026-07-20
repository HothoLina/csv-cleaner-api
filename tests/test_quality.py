from app.services.quality import calculate_quality_score


def test_quality_score_returns_valid_result():
    """
    Test quality score generation.
    """

    report = {
        "rows": 100,
        "columns": 4,
        "column_names": [
            "id",
            "name",
            "price",
            "date"
        ],
        "missing_values": {
            "id": 0,
            "name": 5,
            "price": 2,
            "date": 0,
        },
        "duplicate_rows": 3,
    }

    result = calculate_quality_score(report)

    assert "score" in result
    assert "components" in result
    assert "warnings" in result
    
    assert 0 <= result["score"] <= 100