from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid

class Recuerdo(Base):
    __tablename__ = "recuerdos"
    
    re_codigo = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    us_codigo = Column(UUID(as_uuid=True), ForeignKey("usuarios.us_codigo"), nullable=False)
    re_titulo = Column(String(100), nullable=False)
    re_descripcion = Column(Text)
    re_fecha_creacion = Column(DateTime, default=datetime.utcnow)
    re_fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)