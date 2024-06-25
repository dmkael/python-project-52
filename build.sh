#!/usr/bin/env bash
# setup docker postgres database
docker-compose -f docker/compose.yml up -d

# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
make install

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate