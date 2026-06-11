from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid

class Usuario(Base):
    __tablename__ = "usuarios"
    
    us_codigo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    us_cedula = Column(String(20), unique=True, index=True, nullable=True)  # Campo opcional
    us_correo = Column(String(100), unique=True, index=True, nullable=False)
    us_nombre = Column(String(50), nullable=False)
    us_apellido = Column(String(50), nullable=False)
    us_contrasena = Column(String(255), nullable=False)  # Cambiado a us_contrasena
    us_fecha_registro = Column(DateTime, default=datetime.utcnow)
    us_fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)