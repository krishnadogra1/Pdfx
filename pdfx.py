import os
import time
from fpdf import FPDF
from termcolor import colored

# Hacker-style printing
def printx(text, color="green", delay=0.03):
    for char in text:
        print(colored(char, color), end='', flush=True)
        time.sleep(delay)
    print()

# Ask Termux permission
def ask_storage_permission():
    printx("[*] Checking Termux storage permission...", 'cyan')
    if not os.path.exists("/data/data/com.termux/files/home/storage"):
        printx("[!] Requesting permission using: termux-setup-storage", 'yellow')
        os.system("termux-setup-storage")
        printx("[*] Please ALLOW storage and run script again!", 'magenta')
        exit()
    printx("[✓] Storage permission granted!", 'green')

# Get all txt files from shared storage
def find_txt_files():
    storage_paths = [
        "/data/data/com.termux/files/home/storage/downloads",
        "/data/data/com.termux/files/home/storage/shared",
        "/data/data/com.termux/files/home/storage/dcim",
        "/data/data/com.termux/files/home/storage/documents"
    ]
    txt_files = []
    for path in storage_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    txt_files.append(os.path.join(root, file))
    return txt_files

# Convert .txt to PDF
def convert_to_pdf(txt_file, save_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    filename = os.path.basename(txt_file).replace(".txt", ".pdf")
    output_path = os.path.join(save_path, filename)
    pdf.output(output_path)
    printx(f"[✓] PDF created: {output_path}", 'green')

# Create folder in Downloads
def create_output_folder(folder_name):
    folder_path = f"/data/data/com.termux/files/home/storage/downloads/{folder_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        printx(f"[+] Folder created: {folder_path}", 'blue')
    return folder_path

# Main logic
def main():
    ask_storage_permission()

    printx("[*] Scanning for .txt files in shared storage...", "cyan")
    files = find_txt_files()

    if not files:
        printx("[X] No .txt files found!", 'red')
        return

    printx(f"\n[✓] Found {len(files)} .txt files:\n", 'green')
    for i, file in enumerate(files):
        printx(f"{i+1}. {file}", 'yellow')

    choice = int(input(colored("\nEnter file number to convert: ", 'cyan')))
    if 1 <= choice <= len(files):
        selected_file = files[choice - 1]
    else:
        printx("[X] Invalid selection.", 'red')
        return

    folder_name = input(colored("\nEnter folder name to save PDF (in Downloads): ", 'cyan')).strip()
    output_folder = create_output_folder(folder_name)

    printx("[*] Converting TXT to PDF...", 'cyan')
    convert_to_pdf(selected_file, output_folder)

    printx("\n[✓] Done! Open your Downloads folder to view the PDF.", 'green')

if __name__ == "__main__":
    main()
