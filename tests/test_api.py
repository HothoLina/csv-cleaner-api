from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_invalid_csv_upload():
    """
    Upload an invalid CSV file.
    """

    response = client.post(
        "/upload",
        files={
            "file": (
                "test.txt",
                b"This is not a CSV",
                "text/plain",
            )
        },
    )

    assert response.status_code == 400

    body = response.json()

    assert body["success"] is False

    assert body["error"]["type"] == "InvalidCSVError"