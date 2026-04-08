# To run this test file, use:
#   pytest tests/test_path_finder.py
import pytest

@pytest.mark.parametrize("adb_output,expected", [
    (['/sdcard/WhatsApp/Media/WhatsApp Images'], '/sdcard/WhatsApp/Media/WhatsApp Images'),
    (['/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images'], '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images'),
    ([], None),
])
def test_find_whatsapp_images_path(monkeypatch, adb_output, expected):
    """Test finding WhatsApp images path from possible adb shell find output."""
    def mock_run_find(*args, **kwargs):
        class Result:
            stdout = ('\n'.join(adb_output)).encode()
            returncode = 0
        return Result()
    import subprocess
    monkeypatch.setattr(subprocess, "run", mock_run_find)
    from src.path_finder import find_whatsapp_images_path
    assert find_whatsapp_images_path() == expected
