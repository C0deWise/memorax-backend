#!/bin/bash
set -e

# Ejecutar migraciones
echo "Ejecutando migraciones..."
alembic upgrade head

# Iniciar la aplicación
echo "Iniciando la aplicación..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1