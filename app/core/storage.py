"""
Módulo de integración con Supabase Storage para almacenamiento multimedia.
Utiliza la librería oficial supabase-py para interactuar con el servicio cloud,
manejando credenciales de forma segura desde variables de entorno.
"""

from supabase import create_client, Client
from app.core.config import settings
import os

class SupabaseStorageClient:
    """Cliente para operaciones de almacenamiento multimedia en Supabase Storage."""
    
    def __init__(self):
        """Inicializa el cliente de Supabase usando credenciales del entorno."""
        if not settings.supabase_url or not settings.supabase_key:
            raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configuradas en .env")
            
        self.client: Client = create_client(
            settings.supabase_url, 
            settings.supabase_key
        )
        self.bucket_name = settings.supabase_bucket

    async def upload_file(self, file_path: str, object_name: str = None) -> dict:
        """
        Cargar archivo al bucket especificado.
        
        Args:
            file_path: Ruta local del archivo a cargar
            object_name: Nombre del objeto en el storage (opcional)
            
        Returns:
            dict: Resultado de la operación de carga
        """
        if not object_name:
            object_name = os.path.basename(file_path)
            
        with open(file_path, 'rb') as f:
            response = self.client.storage.from_(self.bucket_name).upload(
                file=f,
                path=object_name,
                file_options={"content-type": "application/octet-stream"}
            )
        return response

    async def download_file(self, object_name: str, destination_path: str) -> bool:
        """
        Descargar archivo desde el bucket.
        
        Args:
            object_name: Nombre del objeto en el storage
            destination_path: Ruta local donde guardar el archivo
            
        Returns:
            bool: True si la descarga fue exitosa
        """
        response = self.client.storage.from_(self.bucket_name).download(object_name)
        with open(destination_path, 'wb') as f:
            f.write(response)
        return True

    async def delete_file(self, object_name: str) -> dict:
        """
        Eliminar archivo del bucket.
        
        Args:
            object_name: Nombre del objeto a eliminar
            
        Returns:
            dict: Resultado de la operación de eliminación
        """
        response = self.client.storage.from_(self.bucket_name).remove([object_name])
        return response

    async def list_files(self) -> list:
        """
        Listar archivos disponibles en el bucket.
        
        Returns:
            list: Lista de objetos en el bucket
        """
        response = self.client.storage.from_(self.bucket_name).list()
        return response