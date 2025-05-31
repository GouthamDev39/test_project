#!/bin/bash
set -e

# host="$DATABASE_HOST"
# port="$DATABASE_PORT"

# echo "Waiting for PostgreSQL at $host:$port..."

# until pg_isready -h "$host" -p "$port" -U "$DATABASE_USER"; do
#   sleep 1
# done
#populate db

python manage.py migrate

#run server
python manage.py runserver 0.0.0.0:8000