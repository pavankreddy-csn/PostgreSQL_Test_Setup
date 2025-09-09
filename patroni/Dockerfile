FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends     postgresql-client     gcc     libpq-dev     python3-dev     make     curl  && rm -rf /var/lib/apt/lists/*
RUN pip install patroni[consul] psycopg2-binary
RUN useradd -ms /bin/bash patroni
USER patroni
WORKDIR /home/patroni
ENTRYPOINT ["patroni"]
CMD ["/etc/patroni.yml"]
