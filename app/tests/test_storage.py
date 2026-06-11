import pytest
from unittest.mock import patch, MagicMock
from app.core.storage import SupabaseStorageClient

@pytest.mark.asyncio
async def test_storage_client_initialization():
    """Test de inicialización del cliente de almacenamiento."""
    with patch('app.core.storage.settings') as mock_settings:
        mock_settings.supabase_url = "https://test.supabase.co"
        mock_settings.supabase_key = "test-key"
        mock_settings.supabase_bucket = "test-bucket"
        
        client = SupabaseStorageClient()
        assert client.bucket_name == "test-bucket"

@pytest.mark.asyncio
async def test_storage_client_missing_credentials():
    """Test que verifica error cuando faltan credenciales."""
    with patch('app.core.storage.settings') as mock_settings:
        mock_settings.supabase_url = ""
        mock_settings.supabase_key = ""
        
        with pytest.raises(ValueError, match="SUPABASE_URL y SUPABASE_KEY deben estar configuradas"):
            SupabaseStorageClient()