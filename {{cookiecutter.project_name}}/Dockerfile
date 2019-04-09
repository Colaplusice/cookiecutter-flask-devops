FROM python:3.6
RUN adduser --disabled-login {{cookiecutter.app_name}}
WORKDIR /home/{{cookiecutter.app_name}}
COPY . .
# debian
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
RUN chmod -R +x .