import os
import shlex
import subprocess
from contextlib import contextmanager
import pytest
import yaml
from cookiecutter.utils import rmtree
from pytest_cases import pytest_fixture_plus

YN_CHOICES = ["y", "n"]


@pytest.fixture
def context():
    return {
        "project_name": "flask_project",
        "app_name": "app",
        "create_api": "y",
        "vps_ssh": "username@vps_ip",
        "database_username": "root",
        "database_password": "newpass"
    }


@pytest_fixture_plus
@pytest.mark.parametrize("create_api", YN_CHOICES, ids=lambda yn: f"create_api:{yn}")
def context_combination(create_api):
    # test input condition
    return {"api": create_api}


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its
     temporal files will be removed
    """
    result = cookies.bake(*args, extra_context=kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies, context, context_combination):
    with bake_in_temp_dir(cookies, **context, **context_combination) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        # assert "api" in found_toplevel_files
        # assert result.project.exists("api") == context['create_api']
        assert "tests" in found_toplevel_files
        assert "Dockerfile" in found_toplevel_files
        assert "{{cookiecutter.app_name}}" in found_toplevel_files
        assert "configs" in found_toplevel_files
        assert ".gitlab-ci.yml" in found_toplevel_files


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()


def test_bake_with_gitlab_ci_setup(cookies):
    with bake_in_temp_dir(cookies) as result:
        result_gitlab_config = yaml.load(result.project.join(".gitlab-ci.yml").open())
        assert result_gitlab_config["test"]
        assert result_gitlab_config["deploy"]


def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/conftest.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)


def test_create_api(cookies):
    with bake_in_temp_dir(cookies, extra_context={"create_api": "n"}) as result:
        test_path = os.path.join(str(result.project), "{{cookiecutter.app_name}}/api")
        assert not os.path.isdir(test_path)

    with bake_in_temp_dir(cookies, extra_context={"create_api": "yes"}) as result:
        test_path = os.path.join(str(result.project), "{{cookiecutter.app_name}}/api")
        assert os.path.isdir(test_path)
