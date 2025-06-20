
# Python WhatsApp Status Saver for Android (Manual & Automated)

A lightweight, terminal-based WhatsApp Status Saver script written in Python. Designed to run on Android devices using **Termux** or **Pydroid 3**. Supports both manual and automated saving modes. No GUI, no ads, no bloat.

---

## Features

- Saves WhatsApp statuses from the hidden `.Statuses` folder
- Manual or interval-based automated saving
- Deletes `.nomedia` to make statuses appear in gallery
- Android version–aware folder detection (supports both old and new WhatsApp structures)
- Offline, clean, and fast
- Graceful error handling

---

## Requirements

- Python **3.8+** (due to use of `dirs_exist_ok` in `shutil.copytree`)
- `colorama` module  
  Install via:
  ```bash
  pip install colorama
  ```
- Any Android version (tested on Android 6–15)
- Termux or Pydroid 3

---

## Setup Instructions (Termux Recommended)

1. Install **Termux** (preferably from F-Droid)
2. Open Termux and install Python:
   ```bash
   pkg update && pkg install python
   ```
3. Install required module:
   ```bash
   pip install colorama
   ```
4. Save the script to your device (e.g. `/sdcard/Download/status_saver.py`)
5. Navigate to the script’s location:
   ```bash
   cd /sdcard/Download
   ```
6. Run the script:
   ```bash
   python status_saver.py
   ```

You may also run it using Pydroid 3 if preferred.

---

## Output

Saved statuses are copied to:
```
/storage/emulated/0/Download/Status Saver/
```

If a `.nomedia` file is present, it will be deleted so statuses appear in your gallery.

---

## Contribution & Feedback

Contributions, suggestions, bug reports, and feature requests are welcome. This project is a personal learning milestone and open to refinement. Feel free to fork and improve.

---

# License
This is open-source — tweak it, break it, remix it, or ship it. Just use it with purpose.
---

**Maintainer:** Uzair_902  
**Script version:** v1.0  
**Date:** 20 June 2025
