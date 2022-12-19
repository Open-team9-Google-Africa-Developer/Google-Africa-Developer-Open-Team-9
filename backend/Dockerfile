FROM python:3.9-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /opt/app
RUN mkdir -p ./pip_cache \
  && mkdir -p ./safeguard 

COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache ./pip_cache/



RUN pip install -r requirements.txt --cache-dir ./pip_cache

COPY . ./safeguard/

RUN chown -R www-data:www-data /opt/app

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]


