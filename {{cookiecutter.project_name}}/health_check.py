import sys
import requests


def check(checktype):
    host = "http://127.0.0.1:{port}".format(port=5000)
    health_api = host + "/{{cookiecutter.project_name}}/health?type=" + checktype
    result = requests.get(health_api)
    if result.status_code == 200:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(check(sys.argv[1]))
