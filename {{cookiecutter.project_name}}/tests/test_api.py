def test_health(client):
    assert client.get("/health").status_code == 404
    assert client.get("/health?type=liveness").status_code == 200


def test_hello_view(client):
    res = client.get("/api/")
    assert res.status_code == 200
    assert res.json == "thanks for use my cookiecutter template !"
