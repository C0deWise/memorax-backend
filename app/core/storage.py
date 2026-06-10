"""
Módulo de integración con Supabase Storage para almacenamiento multimedia.
Este archivo encapsula todas las operaciones necesarias con el servicio cloud,
manteniendo separación clara entre lógica de aplicación y detalles específicos del proveedor.
"""

# TODO: Implementar cliente real de Supabase Storage aquí
# Se utilizarán variables de entorno desde config.py para obtener credenciales seguras

class SupabaseStorageClient:
    """Cliente abstracto para operaciones de almacenamiento multimedia."""
    
    def __init__(self):
        pass

    async def upload_file(self, file_path: str, bucket_name: str, object_name: str):
        """Cargar archivo al bucket especificado."""
        raise NotImplementedError("Implementar método de carga.")

    async def download_file(self, bucket_name: str, object_name: str, destination_path: str):
        """Descargar archivo desde el bucket."""
        raise NotImplementedError("Implementar método de descarga.")

    async def delete_file(self, bucket_name: str, object_name: str):
        """Eliminar archivo del bucket."""
        raise NotImplementedError("Implementar método de eliminación.")

    async def list_files(self, bucket_name: str):
        """Listar archivos disponibles en el bucket."""
        raise NotImplementedError("Implementar método de listado.")