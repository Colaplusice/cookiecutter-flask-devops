def test_health(client):
    assert client.get("/{{cookiecutter.project_name}}/health").status_code == 404
    assert client.get("/{{cookiecutter.project_name}}/health?type=liveness").status_code == 200
