#!/usr/bin/env bash
set -euo pipefail
echo "Patroni roles:"
docker exec -i pg1 curl -s http://pg1:8008/role || true
docker exec -i pg2 curl -s http://pg2:8008/role || true
docker exec -i pg3 curl -s http://pg3:8008/role || true
echo "Primary replication info (if leader):"
docker exec -i pg1 psql -U postgres -c "SELECT * FROM pg_stat_replication;" || true
