"""TSK-B02: Actualizar modelo Usuario con campos requeridos

Revision ID: b2fb07593729
Revises: 0001
Create Date: 2026-06-11 02:39:45.200474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2fb07593729'
down_revision: Union[str, None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Agregar columnas nuevas al modelo Usuario
    op.add_column('usuarios', sa.Column('us_cedula', sa.String(length=20), nullable=True))
    op.add_column('usuarios', sa.Column('us_correo', sa.String(length=100), nullable=True))  # Temporalmente nullable
    op.add_column('usuarios', sa.Column('us_nombre', sa.String(length=50), nullable=True))  # Temporalmente nullable
    op.add_column('usuarios', sa.Column('us_apellido', sa.String(length=50), nullable=True))  # Temporalmente nullable
    op.add_column('usuarios', sa.Column('us_contrasena', sa.String(length=255), nullable=True))  # Temporalmente nullable
    
    # Copiar datos de las columnas antiguas a las nuevas
    op.execute("UPDATE usuarios SET us_correo = us_email")
    op.execute("UPDATE usuarios SET us_contrasena = us_contrasena_hash")
    
    # Hacer las nuevas columnas NOT NULL
    op.alter_column('usuarios', 'us_correo', nullable=False)
    op.alter_column('usuarios', 'us_nombre', nullable=False)
    op.alter_column('usuarios', 'us_apellido', nullable=False)
    op.alter_column('usuarios', 'us_contrasena', nullable=False)
    
    # Crear índices para las nuevas columnas
    op.create_index(op.f('ix_usuarios_us_cedula'), 'usuarios', ['us_cedula'], unique=True)
    op.create_index(op.f('ix_usuarios_us_correo'), 'usuarios', ['us_correo'], unique=True)
    
    # Eliminar las columnas antiguas
    op.drop_index('ix_usuarios_us_email', table_name='usuarios')
    op.drop_column('usuarios', 'us_email')
    op.drop_column('usuarios', 'us_nombre_usuario')
    op.drop_column('usuarios', 'us_contrasena_hash')


def downgrade() -> None:
    # Recrear las columnas antiguas
    op.add_column('usuarios', sa.Column('us_email', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('us_nombre_usuario', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('us_contrasena_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    
    # Copiar datos de las nuevas columnas a las antiguas
    op.execute("UPDATE usuarios SET us_email = us_correo")
    op.execute("UPDATE usuarios SET us_nombre_usuario = us_nombre || ' ' || us_apellido")
    op.execute("UPDATE usuarios SET us_contrasena_hash = us_contrasena")
    
    # Hacer las columnas antiguas NOT NULL
    op.alter_column('usuarios', 'us_email', nullable=False)
    op.alter_column('usuarios', 'us_nombre_usuario', nullable=False)
    op.alter_column('usuarios', 'us_contrasena_hash', nullable=False)
    
    # Crear índices para las columnas antiguas
    op.create_index('ix_usuarios_us_email', 'usuarios', ['us_email'], unique=True)
    op.create_index('ix_usuarios_us_nombre_usuario', 'usuarios', ['us_nombre_usuario'], unique=True)
    
    # Eliminar las nuevas columnas
    op.drop_index(op.f('ix_usuarios_us_correo'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_us_cedula'), table_name='usuarios')
    op.drop_column('usuarios', 'us_contrasena')
    op.drop_column('usuarios', 'us_apellido')
    op.drop_column('usuarios', 'us_nombre')
    op.drop_column('usuarios', 'us_correo')
    op.drop_column('usuarios', 'us_cedula')