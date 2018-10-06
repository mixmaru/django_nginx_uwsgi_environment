FROM python:3.6.6

RUN pip install pipenv
WORKDIR /app
EXPOSE 80
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