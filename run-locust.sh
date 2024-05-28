docker compose build

WORKERS=$1 docker compose up db sync -d
sleep 5
./env/bin/locust --endpoint "/ninja/employees" --n 100 --data data.json --html results/ninja-sync-w"$1"-"$(date '+%F-%T')".html
docker compose down

WORKERS=$1 docker compose up db async -d
sleep 5
./env/bin/locust --endpoint "/ninja/aemployees" --n 100 --data data.json --html results/ninja-async-w"$1"-"$(date '+%F-%T')".html
docker compose down

WORKERS=$1 docker compose up db sync -d
sleep 5
./env/bin/locust --endpoint "/drf/employees" --n 100 --data data.json --html results/drf-sync-w"$1"-"$(date '+%F-%T')".html
docker compose down