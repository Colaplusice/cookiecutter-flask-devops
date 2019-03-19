#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == "__main__":
    if ("y" or "yes") not in "{{ cookiecutter.create_api}}":
        shutil.rmtree("app/api")
