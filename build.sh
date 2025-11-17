#!/usr/bin/env bash
# Exit on error
set -o errexit

# Apply any outstanding database migrations
python manage.py migrate

# Build static files
python manage.py collectstatic --noinput