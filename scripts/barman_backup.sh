#!/usr/bin/env bash
set -euo pipefail
docker exec -i barman barman check pg1 || true
docker exec -i barman barman backup pg1 || true
docker exec -i barman barman list-backup pg1 || true
