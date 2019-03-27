#  Flask template based on docker bootstrap4 for continuous integration & continuous delivery

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

## Changes

### v18.09.13

- 项目创建，初始化 flask 模版

### v18.09.20

- 添加 pre-commit, 在 commit 提交之前检查空格, 文件结束行和代码格式等问题

### v18.10.12

- 添加 isort, seed-isort-config 格式化导入
