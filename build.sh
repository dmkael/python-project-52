#!/usr/bin/env bash
# Exit on error
set -o errexit
set -o pipefail

# setup docker postgres database
docker-compose -f docker/compose.yml up -d

# Check if docker-compose up was successful
docker_compose_exit_code=$?
if [ $docker_compose_exit_code -ne 0 ]; then
    echo "Failed to start Docker containers. Exiting."
    exit $docker_compose_exit_code
fi

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate