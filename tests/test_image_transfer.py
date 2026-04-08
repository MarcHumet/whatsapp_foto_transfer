# To run this test file, use:
#   pytest tests/test_image_transfer.py
import pytest

class DummyADB:
    def __init__(self, files):
        self.files = files
        self.copied = []
        self.deleted = []
    def list_images(self, path):
        return self.files
    def copy_image(self, src, dst):
        self.copied.append((src, dst))
        return True
    def delete_image(self, src):
        self.deleted.append(src)
        return True

def test_copy_and_delete_images():
    files = ["img1.jpg", "img2.jpg"]
    adb = DummyADB(files)
    from src.image_transfer import copy_and_optionally_delete_images
    copied, deleted = copy_and_optionally_delete_images(adb, "/device/path", "/local/path", delete_after=True)
    assert copied == ["img1.jpg", "img2.jpg"]
    assert deleted == ["img1.jpg", "img2.jpg"]

def test_copy_without_delete():
    files = ["img1.jpg", "img2.jpg"]
    adb = DummyADB(files)
    from src.image_transfer import copy_and_optionally_delete_images
    copied, deleted = copy_and_optionally_delete_images(adb, "/device/path", "/local/path", delete_after=False)
    assert copied == ["img1.jpg", "img2.jpg"]
    assert deleted == []
