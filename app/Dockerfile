FROM ubuntu:18.04

WORKDIR /root


# shellをbashに指定
SHELL ["/bin/bash", "-c"]


# 最新状態へ
RUN apt update
RUN apt -y upgrade


# 必要なコマンドのインストール
RUN apt -y install build-essential curl git zlib1g-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev


# nginxのインストール
RUN apt -y install nginx=1.14.0-0ubuntu1.1


# pyenvのインストールと設定
RUN apt -y install python3.6 python3-pip
# pipのアップグレード
RUN pip3 install --upgrade pip
# uWSGIのインストール
RUN pip3 install uwsgi

#コード転送
WORKDIR /app
COPY ./ ./

EXPOSE 80


# nginxの起動(フォアグラウンドで動かさないとすぐ終了してしまう)
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]


# RUN pip install pipenv
# WORKDIR /app
# EXPOSE 80
# WORKDIR /docker_build
# ADD ./Pipfile /docker_build (必要なファイルをhostからコピー配置)
# ADD ./Pipfile.lock /docker_build (同上)
#
# RUN pip install pipenv (pipenvのインストール)
# RUN pipenv install --system --deploy (Pipfile Pipfile.lockに記載されたライブラリをインストール)
#
# WORKDIR /app (作業ディレクトリを指定)
# EXPOSE 80 (80版ポートを開ける)

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ] (コンテナ起動時に実行するコマンド（djangoのプロジェクトがあれば起動時に開発用webサーバーを起動できる。）)