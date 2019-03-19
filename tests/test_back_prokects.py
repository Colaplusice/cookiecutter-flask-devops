import os
import shlex
import subprocess
from contextlib import contextmanager

import yaml
from cookiecutter.utils import rmtree


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
    result = cookies.bake(*args, **kwargs)
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


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "tests" in found_toplevel_files
        assert "Dockerfile" in found_toplevel_files
        assert "app" in found_toplevel_files
        assert "configs" in found_toplevel_files
        assert ".gitlab-ci.yml" in found_toplevel_files


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()


def test_bake_with_gitlab_ci_setup(cookies):
    with bake_in_temp_dir(cookies) as result:
        result_gitlab_config = yaml.load(result.project.join(".gitlab-ci.yml").open())
        assert result_gitlab_config["stages"]
        assert result_gitlab_config["test_all"]
        assert result_gitlab_config["deploy_integration"]


def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/conftest.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)


def test_create_api(cookies):
    with bake_in_temp_dir(cookies, extra_context={"create_api": "n"}) as result:
        test_path = os.path.join(str(result.project), "app/api")
        assert not os.path.isdir(test_path)

    with bake_in_temp_dir(cookies, extra_context={"create_api": "yes"}) as result:
        test_path = os.path.join(str(result.project), "app/api")
        assert os.path.isdir(test_path)
