FROM alpine:3.12

#Install all required packages, add user for executing mailman and set execution rights for startup script
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev \
       libffi-dev \
  # psutil needs linux-headers to compile on musl c library.
    && apk add --no-cache bash su-exec postgresql-client mysql-client curl python3 py3-pip linux-headers \
    && python3 -m pip install -U pip setuptools wheel \
        && python3 -m pip install psycopg2 \
                   gunicorn==19.9.0 \
                   mailman==3.3.4 \
                   mailman-hyperkitty==1.1.0 \
                   pymysql \
                   'sqlalchemy<1.4.0' \
 # Also install nano for easy text editing
    && apk add nano \
    && apk del build-deps \
    && adduser -S mailman

#Add startup script to container
COPY docker-entrypoint.sh /usr/local/bin/
COPY assets/scripts /usr/mailman_scripts

# Change the working directory.
WORKDIR /opt/mailman

#Expose the ports for the api (8001) and lmtp (8024)
EXPOSE 8001 8024

ENV MAILMAN_CONFIG_FILE /etc/mailman.cfg

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["master", "--force"]
