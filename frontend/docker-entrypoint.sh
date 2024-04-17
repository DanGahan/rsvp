#!/bin/bash
# Generate a random DJANGO_SECRET_KEY if not already set
if [ -z "$DJANGO_SECRET_KEY" ]; then
    export DJANGO_SECRET_KEY=$(openssl rand -base64 32)
fi

# Execute the command provided as arguments
exec "$@"
