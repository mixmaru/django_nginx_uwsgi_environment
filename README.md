# django_nginx_uwsgi_environment
Nginx -> uWSGI -> Django で動作するDjangoプロジェクトの初期状態環境

# 使い方
```
$ cd your_work_dir
$ git clone https://github.com/mixmaru/django_nginx_uwsgi_environment.git
$ cd django_nginx_uwsgi_environment
$ docker-compose up
```

ブラウザでlocalhostにアクセスすると、Djangoの初期画面が表示される。

# DB
postgreSQL

user_name: foo  
password: foobar  
db_name: baz  

localhost:5432でアクセス可能。

# DjangoによるDB初期化

docker exec -it (appのコンテナ名) /bin/bash
でappサーバー内に入って、

```
$ cd project/
$ python3 ./manage.py migrate
```
