#!/usr/bin/env bash

uwsgi --socket :8000 --wsgi-file uwsgi_test.py & nginx -g "daemon off;"