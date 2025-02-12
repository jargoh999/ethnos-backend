#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Generate dummy data
python manage.py genarate_dummy_data

# Collect static files
python manage.py collectstatic --noinput