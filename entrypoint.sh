#!/bin/bash

set -e

# Check if the MySQL server is running

if ! systemctl status mysql | grep -q "Active: active (running)"; then
    echo "MySQL server is not running. Starting..."
    systemctl start mysql
fi

# Create the Django database
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run the Django development server
python manage.py runserver 0.0.0.0:8000