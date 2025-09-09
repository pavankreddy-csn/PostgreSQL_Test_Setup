FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends     barman     postgresql-client     rsync     openssh-client     cron  && rm -rf /var/lib/apt/lists/*
VOLUME ["/etc/barman","/var/lib/barman"]
USER barman
ENTRYPOINT ["barman"]
CMD ["--help"]
