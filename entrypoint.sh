#!/bin/bash
set -e

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos esté lista..."
while ! pg_isready -h db -p 5432 -U postgres > /dev/null 2> /dev/null; do
    sleep 1
done

# Ejecutar migraciones
echo "Ejecutando migraciones..."
alembic upgrade head

# Iniciar la aplicación
echo "Iniciando la aplicación..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000