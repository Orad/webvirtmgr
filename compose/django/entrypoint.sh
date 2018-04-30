#!/bin/bash
set -e
cmd="$@"

# Run migrations before getting going
if [ -f /app/manage.py ]; then
  python /app/manage.py syncdb --noinput
  python /app/manage.py migrate --noinput
fi

exec $cmd
