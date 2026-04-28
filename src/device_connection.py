import shutil
import os
from loguru import logger
import time


def is_device_accessible(media_path: str = "~/myphone") -> bool:
    """
    Returns True if the provided media_path exists and is accessible, else False.
    """
    start=time.time()
    media_path = os.path.expanduser(media_path)
    time_exploring_media_path = time.time() - start
    logger.debug(f"Time taken to explore media path: {round(time_exploring_media_path,5)} seconds")
    
    try:
        
        if not os.path.exists(media_path):
            logger.warning(f"Media path does not exist: {media_path}")
            return False
        if not os.path.isdir(media_path):
            logger.warning(f"Media path is not a directory: {media_path}")
            return False
        start=time.time()
        if not os.access(media_path, os.R_OK | os.X_OK):
            logger.warning(f"Media path is not readable or accessible: {media_path}")
            return False
        time_checking_access = time.time() - start
        logger.debug(f"Time taken to os.access: {round(time_checking_access  ,5)} seconds")
        try:
            start=time.time()
            entries = os.listdir(media_path)
            time_exploring_files = time.time() - start
            logger.debug(f"Time taken to explore files: {round(time_exploring_files,5)} seconds >>> {len(entries)} files detected")
        
        except Exception as e:
            logger.error(f"Error listing directory contents: {e}")
            return False
        if not entries:
            logger.warning(f"Media path is accessible but empty (possible mount failure): {media_path}")
            return False
        logger.debug(f"Media path accessible and contains files: {media_path}")
        return True
    except Exception as e:
        logger.error(f"Error checking media path: {e}")
        return False
    time_exploring_media_path = time.time() - start 
    
    time_exploring_media_path = time.time() - start 
    logger.debug(f"Time taken to explore media path: {round(time_exploring_media_path,3)} seconds")
   
def classify_file_types(path_to_check: str, extension: str) -> None:
    """
    Finds all files in the given path with the specified extension, creates a folder for them,
    and moves the files into that folder.
    Args:
        path_to_check (str): Directory to search for files.
        extension (str): File extension to filter (e.g., 'pdf').
    """
    if not os.path.isdir(path_to_check):
        logger.error(f"Provided path is not a directory: {path_to_check}")
        return

    ext = extension.lower().lstrip('.')
    target_folder = os.path.join(path_to_check, f"{ext}_files")

    # List all files with the given extension
    files = [f for f in os.listdir(path_to_check)
             if os.path.isfile(os.path.join(path_to_check, f)) and f.lower().endswith(f".{ext}")]

    if not files:
        logger.info(f"No .{ext} files found in {path_to_check}")
        return

    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        logger.debug(f"Created folder: {target_folder}")

    # Move files
    for filename in files:
        src = os.path.join(path_to_check, filename)
        dst = os.path.join(target_folder, filename)
        try:
            shutil.move(src, dst)
            logger.info(f"Moved {filename} to {target_folder}")
        except Exception as e:
            logger.error(f"Failed to move {filename}: {e}")



def classify_file_types_2(path_to_check: str, extension: str) -> None:
    if not os.path.isdir(path_to_check):
        logger.error(f"Provided path is not a directory: {path_to_check}")
        return

    ext = extension.lower().lstrip(".")
    target_folder = os.path.join(path_to_check, f"{ext}_files")

    try:
        os.makedirs(target_folder, exist_ok=True)
    except OSError as e:
        logger.error(f"Could not create target folder {target_folder}: {e}")
        return

    moved = 0

    try:
        with os.scandir(path_to_check) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.lower().endswith(f".{ext}"):
                    src = entry.path
                    dst = os.path.join(target_folder, entry.name)
                    try:
                        shutil.move(src, dst)
                        moved += 1
                    except Exception as e:
                        logger.error(f"Failed to move {entry.name}: {e}")
    except OSError as e:
        logger.error(f"Failed to scan directory {path_to_check}: {e}")
        return

    if moved == 0:
        logger.info(f"No .{ext} files found in {path_to_check}")
    else:
        logger.info(f"Moved {moved} .{ext} files to {target_folder}")






if __name__ == "__main__":
    path = "~/myphone"
    user_path = os.path.expanduser(path)
    if is_device_accessible(path):
        logger.success(f"Media path is accessible: {path}")
    else:
        logger.warning(f"Media path is not accessible: {path}")

    for filename in os.listdir(os.path.expanduser('~/myphone')):
        print(filename)  
    for extension in ['pdf', 'jpg', 'png', 'docx', 'gpx','mp4','mp3']:  
        start =time.time()  
        classify_file_types(path_to_check=user_path+"/Emmagatzematge intern/Download", extension=extension)
        time_classifying_files = time.time() - start
        logger.debug(f"Time taken to classify {extension} files: {round(time_classifying_files,2)} seconds for {extension=}")