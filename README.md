## WhatsApp Photo Downloader for Android — Specifications

### Aims

- Automate the process of downloading all WhatsApp images from an Android phone to a computer.
- Provide a simple, reliable command-line tool for Linux users.
- Ensure user privacy by only accessing WhatsApp media directories.
- Support easy extension for additional features (e.g., filtering, other media types).

---

### Required Packages

- **adb (Android Debug Bridge):** For device connection and file transfer.
- **Python 3.8+**
- **Python packages:**
	- `subprocess` (standard library) — to run adb commands
	- `os`, `shutil` (standard library) — for file and directory operations
	- `argparse` (standard library) — for command-line arguments
	- `logging` (standard library) — for logging and error reporting
	- (Optional) `tqdm` — for progress bars

---

### Development Steps & Modularization

#### 1. Device Connection Module
- Detect connected Android devices using adb.
- Handle errors if no device is found or adb is not installed.

#### 2. WhatsApp Media Location Module
- Locate WhatsApp image directories on the device:
	- Typical path: `/sdcard/WhatsApp/Media/WhatsApp Images/`
- Optionally allow user to specify a custom path.

#### 3. Image Download Module
- List all image files in the WhatsApp Images directory.
- Copy/download images to a specified local folder on the computer.
- Support incremental downloads (skip already-downloaded files).

#### 4. Optional: Filtering & Organization Module
- Allow filtering by date, file type, or chat (if possible).
- Organize downloaded images into subfolders (e.g., by date).

#### 5. Logging & Error Handling Module
- Log all actions and errors to a file and/or console.
- Provide clear error messages for common issues (e.g., permission denied, device not found).

---

### Verification

- **Device Detection:** Run the tool with no device connected; confirm it reports the error.
- **File Transfer:** Connect a device with WhatsApp images; confirm images are copied to the local folder.
- **Incremental Download:** Run the tool twice; confirm it skips already-downloaded files.
- **Error Handling:** Test with missing permissions or disconnected device; confirm appropriate error messages.
- **Logging:** Check that logs are created and contain relevant information.

---

### Future Extensions

- Support for WhatsApp videos and other media types.
- GUI version for non-technical users.
- Cross-platform support (Windows, macOS).
- Advanced filtering (by chat, media type, etc.).

---

**Note:**  
This tool does not attempt to bypass WhatsApp security or encryption. It only accesses media files stored in standard WhatsApp directories on the device, as permitted by the user.
