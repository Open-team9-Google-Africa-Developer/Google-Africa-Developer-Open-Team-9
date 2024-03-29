#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    ( cd safeguard; python manage.py createsuperuser --no-input)
fi
(cd safeguard; gunicorn core.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"