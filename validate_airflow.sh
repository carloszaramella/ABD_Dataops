#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

docker compose -f docker-compose-airflow.yml up -d --build

echo "Airflow iniciado em http://localhost:8080"
echo "Usuário: admin"
echo "Senha: admin"
