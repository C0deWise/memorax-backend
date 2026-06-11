# MemoraX Backend

## DescripciÃ³n
Backend modular para el proyecto MemoraX basado en FastAPI.

## TecnologÃ­as
- FastAPI
- PostgreSQL (conectado via asyncpg y SQLAlchemy 2.x)
- Alembic (gestiÃ³n de migraciones)
- Pytest (entorno de pruebas)

## InstalaciÃ³n
1. Clonar el repositorio
2. Crear ambiente virtual: `python -m venv venv`
3. Activar ambiente virtual: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Copiar `.env.example` a `.env` y ajustar valores segÃºn corresponda

## EjecuciÃ³n
```bash
uvicorn app.main:app --reload
```

## Pruebas
Para ejecutar pruebas unitarias:

```bash
pytest
```