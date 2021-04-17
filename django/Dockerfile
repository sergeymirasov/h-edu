FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential libpq-dev gettext libmagic-dev libjpeg-dev zlib1g-dev && \
    apt-get purge -y --auto-remove -o APT:AutoRemove:RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/base.txt && \
    rm -rf /requirements

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY  ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./ /app/
RUN python manage.py collectstatic --no-input

ENTRYPOINT ["/entrypoint"]
