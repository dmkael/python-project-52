#!/usr/bin/env bash
# Exit on error
set -o errexit
set -o pipefail

# setup docker postgres database
docker run -d \
    --name task_manager_db \
    -e POSTGRES_USER="${DB_USER}" \
    -e POSTGRES_PASSWORD="${DB_PASSWORD}" \
    -e POSTGRES_DB="${DB_NAME}" \
    -p 5433:5432 \
    -v taskman_db:/var/lib/postgresql/data \
    --restart=on-failure \
    postgres:14-alpine

# Check if docker-compose up was successful
docker_run_exit_code=$?
if [ $docker_run_exit_code -ne 0 ]; then
    echo "Failed to start PostgreSQL container. Exiting."
    exit $docker_run_exit_code
fi

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate