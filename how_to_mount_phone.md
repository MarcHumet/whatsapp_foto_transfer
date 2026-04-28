# How to Mount an MTP Device (Android Phone) on Linux

## 1. Prerequisites

- Install `jmtpfs` (or `simple-mtpfs`):
  ```sh
  sudo apt install jmtpfs
  ```

## 2. Prepare a Mount Point

- Create a directory to use as the mount point:
  ```sh
  mkdir -p ~/myphone
  ```

## 3. Important Warning

> **Warning:**  
> Only one program can access your MTP device at a time.  
> **Before mounting with `jmtpfs`, make sure your file manager (Nautilus, Dolphin, etc.) is NOT browsing your phone.**  
> If your file manager is open to your phone, close those windows or eject/unmount the device from the file manager first.  
> Otherwise, you may see an error like:  
> `libusb_claim_interface() reports device is busy, likely in use by GVFS or KDE MTP device handling already`

## 4. Mount the Device

- Connect your phone via USB.
- Set the phone to “File Transfer” or “MTP” mode and unlock it.
- Mount the device:
  ```sh
  jmtpfs ~/myphone
  ```

## 5. Access Your Files

- Now you can access your phone’s files at `~/myphone` using the terminal or Python.

## 6. Unmount When Done

- When finished, unmount the device:
  ```sh
  fusermount -u ~/myphone
  ```

## 7. Troubleshooting

- If you see a “device is busy” error:
  - Close your file manager’s phone view.
  - Optionally, kill the interfering process:
    ```sh
    pkill -f gvfs-mtp-volume-monitor
    pkill -f kio_mtp
    ```
  - Then try mounting again.
