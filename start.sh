#!/bin/sh

echo "waiting the database to be ready..."

until pg_isready -h "$POSTGRES_HOST" -p 5432 -U "$POSTGRES_USER" > /dev/null 2>&1; do
sleep 1
echo "waiting..."
done    

echo "database is ready!, inicializing backend system..."

echo "incializing backend system..."

echo "apllying database migrations..."
python manage.py migrate

echo "populating database"
python manage.py seed_global

echo "running server..."
python manage.py runserver 0.0.0.0:8000

echo "server initialized in the port 8000"
