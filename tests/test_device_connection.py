# To run this test file, use:
#   pytest tests/test_device_connection.py
import subprocess
import pytest

def test_adb_device_connected(monkeypatch):
    """Test that adb detects a connected device."""
    def mock_run(*args, **kwargs):
        class Result:
            stdout = b'List of devices attached\n1234567890abcdef\tdevice\n'
            returncode = 0
        return Result()
    monkeypatch.setattr(subprocess, "run", mock_run)
    from src.device_connection import is_device_connected
    assert is_device_connected() is True

def test_adb_device_not_connected(monkeypatch):
    """Test that adb reports no device connected."""
    def mock_run(*args, **kwargs):
        class Result:
            stdout = b'List of devices attached\n\n'
            returncode = 0
        return Result()
    monkeypatch.setattr(subprocess, "run", mock_run)
    from src.device_connection import is_device_connected
    assert is_device_connected() is False
