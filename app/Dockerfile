FROM ubuntu:18.04

WORKDIR /root

# ロケール設定(pipenvでPipfile.lockを作るときにエラーで怒られた為)
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# shellをbashに指定
SHELL ["/bin/bash", "-c"]

# 最新状態へ
RUN apt update
RUN apt -y upgrade

# 必要なコマンドのインストール
RUN apt -y install build-essential curl git zlib1g-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev

# nginxのインストール
RUN apt -y install nginx

# pythonまわりのインストール
RUN apt -y install python3.6 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

#コード転送
WORKDIR /app
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./uwsgi.ini ./uwsgi.ini

#ライブラリのインストール(pipenv syncではNGらしい https://github.com/pypa/pipenv/issues/2650)
RUN pipenv install --deploy --system

EXPOSE 80

CMD uwsgi uwsgi.ini & nginx -g "daemon off;"

