# django_nginx_uwsgi_environment
Nginx -> uWSGI -> Django で動作するDjangoプロジェクトの初期状態環境

# 使い方
```
$ cd your_work_dir
$ git clone https://github.com/mixmaru/django_nginx_uwsgi_environment.git
$ cd django_nginx_uwsgi_environment/app
$ docker build -t django_env .
$ docker run -d -p 80:80 -v /abstract_path_to_django_nginx_uwsgi_environment/app/logs:/var/log/nginx django_init
```

ブラウザでlocalhostにアクセスすると、Djangoの初期画面が表示される。

## 今後予定
docker-composeを使ってpostgreSQLでデータベースも含めた環境構築を設定する予定
