FROM tiangolo/uwsgi-nginx:python3.5

MAINTAINER Ashish Trehan <ashishtrehan10@gmail.com>

LABEL appname=tsp

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
	&& pip install -r /tmp/requirements.txt

COPY nginx.conf /etc/nginx/conf.d/