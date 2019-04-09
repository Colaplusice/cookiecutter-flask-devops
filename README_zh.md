#  cookiecutter template for Flask project

## feature



## install cookiecutter

pip install cookiecutter

## generate project

cookiecutter <https://github.com/Colaplusice/cookiecutter-flask-devops.git>
or
```
cd
```
项目的地址可以为 git 链接, 或者将项目放在 ~/.cookiecutter 路径下, 相当于全局变量, 可以 cookiecutter project_name 直接生成。或者用绝对路径来生成。

## 可选参数

- --no-input
- -f --overwrite-if-exists
- --config-file PATH

## 输入选项

输入命令后会出现一些配置选项, 如果不选择则执行默认的配置。这些选项用来生成定制的项目。目前 flask 模板提供的选项有:

- project_name  # 生成 project 的名称
- app_name      # flask app 的名称
- create_api  yes/no #是否生成带有 api 配置的模板