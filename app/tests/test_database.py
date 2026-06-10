import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.database import Base, engine, AsyncSessionLocal
from app.core.config import settings

@pytest.mark.asyncio
async def test_database_connection():
    """Test básico de conexión a la base de datos."""
    try:
        async with engine.begin() as conn:
            # Si llegamos hasta aquí, la conexión fue exitosa
            assert True
    except Exception as e:
        pytest.fail(f"Failed to connect to database: {e}")

@pytest.mark.asyncio  
async def test_create_tables():
    """Verifica que se puedan crear tablas usando metadatos."""
    temp_engine = create_async_engine(settings.database_url)
    try:
        async with temp_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            # Limpiar después de la prueba
            await conn.run_sync(Base.metadata.drop_all)
        assert True
    except Exception as e:
        pytest.fail(f"Failed to create/drop tables: {e}")
    finally:
        await temp_engine.dispose()