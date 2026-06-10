from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Crear el motor asÃ­ncrono
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    future=True
)

# Crear la sesiÃ³n asÃ­ncrona
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base para modelos
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# Dependencia para obtener la sesiÃ³n
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session