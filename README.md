# PDFX Tool - Termux Version

**Author**: Krishna Dogra  
**Tool Name**: PDFX  
**Function**: Convert any `.txt` file in your phone storage into a styled `.pdf` file using Termux.

---

## Features

- Green hacker-style terminal UI
- Automatic permission handling using `termux-setup-storage`
- Searches for `.txt` files recursively in `/storage/emulated/0/`
- Creates `/storage/emulated/0/PDFX/` folder if not exists
- Converts `.txt` to `.pdf` using FPDF
- Clean, bold, animated terminal output

---

## Setup in Termux

```bash
pkg update
pkg install python termux-api
pip install fpdf
termux-setup-storage
