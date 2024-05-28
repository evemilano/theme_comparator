import os
import zipfile
import difflib
from pathlib import Path
from datetime import datetime

def extract_zip_files(input_folder):
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if zipfile.is_zipfile(item_path):
            with zipfile.ZipFile(item_path, 'r') as zip_ref:
                extract_path = os.path.join(input_folder, os.path.splitext(item)[0])
                zip_ref.extractall(extract_path)

def get_all_files(folder):
    file_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), folder))
    return set(file_list)

def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8', errors='ignore') as f1:
        f1_lines = f1.readlines()
    with open(file2, 'r', encoding='utf-8', errors='ignore') as f2:
        f2_lines = f2.readlines()

    diff = difflib.unified_diff(f1_lines, f2_lines, fromfile=file1, tofile=file2, lineterm='')
    return [line for line in diff if line.startswith(('---', '+++', '@@', '-', '+'))]

def generate_report(theme1, theme2):
    theme1_files = get_all_files(theme1)
    theme2_files = get_all_files(theme2)

    missing_files = theme1_files - theme2_files
    added_files = theme2_files - theme1_files
    common_files = theme1_files & theme2_files

    report = []
    report.append("Formato delle differenze:\n"
                  "@@ -a,b +c,d @@\n"
                  "a: Numero di riga iniziale nel file originale\n"
                  "b: Numero di righe del blocco nel file originale\n"
                  "c: Numero di riga iniziale nel file modificato\n"
                  "d: Numero di righe del blocco nel file modificato\n"
                  "-: Righe rimosse dal file originale\n"
                  "+: Righe aggiunte al file modificato\n")

    if missing_files:
        report.append(f"File mancanti in {os.path.basename(theme2)}:\n" + "\n".join(missing_files) + "\n")
    if added_files:
        report.append(f"File aggiunti in {os.path.basename(theme2)}:\n" + "\n".join(added_files) + "\n")

    modified_files = []
    for file in common_files:
        file1_path = os.path.join(theme1, file)
        file2_path = os.path.join(theme2, file)

        if not Path(file1_path).read_text(errors='ignore') == Path(file2_path).read_text(errors='ignore'):
            diff = compare_files(file1_path, file2_path)
            if diff:
                modified_files.append(file)
                report.append(f"File modificato: {file}\n" + "\n".join(diff) + "\n")

    return "\n\n".join(report), modified_files

def main():
    input_folder = "input"
    extract_zip_files(input_folder)

    themes = [os.path.join(input_folder, d) for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]

    if len(themes) != 2:
        raise ValueError("Devono esserci esattamente 2 temi da confrontare.")

    theme1, theme2 = themes
    report, modified_files = generate_report(theme1, theme2)

    theme1_name = os.path.basename(theme1)
    theme2_name = os.path.basename(theme2)
    current_time = datetime.now().strftime("%Y%m%d_%H%M")
    report_filename = f"report_{theme1_name}_vs_{theme2_name}_{current_time}.txt"

    with open(report_filename, 'w', encoding='utf-8') as report_file:
        report_file.write(report)

    print(f"Report generato: {report_filename}")
    if modified_files:
        print("File modificati:\n" + "\n".join(modified_files))
    else:
        print("Nessun file modificato.")

if __name__ == "__main__":
    main()
