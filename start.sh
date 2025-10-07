#!/bin/sh

echo "Esperando o banco de dados..."

until pg_isready -h "$POSTGRES_HOST" -p 5432 -U "$POSTGRES_USER" > /dev/null 2>&1; do
  sleep 1
  echo "Esperando"
done

echo "Banco de dados pronto! Iniciando backend..."

echo "Inicializando backend"

echo "Aplicando migrações"
python manage.py migrate

echo "Populando banco de dados"
python manage.py seed_global

echo "Rodando o servidor"
python manage.py runserver 0.0.0.0:8000

echo "Servidor rodando na porta 8000!"