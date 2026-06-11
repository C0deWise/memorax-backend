#!/bin/bash
set -e

echo "=== ENTRYPOINT EJECUTADO ==="
echo "DATABASE_URL=$DATABASE_URL"
echo "ALEMBIC_DATABASE_URL=$ALEMBIC_DATABASE_URL"

# Ejecutar migraciones
echo "Ejecutando migraciones..."
alembic upgrade head

# Iniciar la aplicación
echo "Iniciando la aplicación..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1