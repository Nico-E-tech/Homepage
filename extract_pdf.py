import pypdf
import os

files = ["Lebenslauf.pdf", "Fachliche_Projekte.pdf"]

with open("output.txt", "w", encoding="utf-8") as out:
    for f in files:
        out.write(f"--- EXTRACTING: {f} ---\n")
        print(f"--- EXTRACTING: {f} ---")
        if not os.path.exists(f):
            out.write(f"File not found: {f}\n")
            continue
        try:
            reader = pypdf.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                out.write(text + "\n")
        except Exception as e:
            out.write(f"Error reading {f}: {e}\n")
        out.write("\n\n")
