#!/bin/bash
# Entrypoint script for Django application

# Exit immediately if a command exits with a non-zero status
set -e

# Print commands and their arguments as they are executed
set -x

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Generate dummy data (optional, remove in production)
echo "Generating dummy data..."
python manage.py genarate_dummy_data



# Create a superuser if not exists (optional)
echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
"

# Start Gunicorn server
echo "Starting Gunicorn server..."
gunicorn --config gunicorn.config.py e_wallet_backend.wsgi:application