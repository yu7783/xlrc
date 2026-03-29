import re
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

# Regex to parse LRC tags and time tags
TIME_PATTERN = re.compile(r"\[(\d{2}):(\d{2}\.\d{2})\](.*)")
ARTIST_PATTERN = re.compile(r"\[ar:(.*)\]", re.IGNORECASE)
TITLE_PATTERN = re.compile(r"\[ti:(.*)\]", re.IGNORECASE)

def parse_lrc_content(lines):
    """Extracts metadata and lyrics from LRC lines."""
    metadata = {"artist": "Unknown", "title": "Converted Song"}
    lyrics_lines = []

    for line in lines:
        line = line.strip()
        # Check for Artist tag
        ar_match = ARTIST_PATTERN.match(line)
        if ar_match:
            metadata["artist"] = ar_match.group(1).strip()
            continue
        
        # Check for Title tag
        ti_match = TITLE_PATTERN.match(line)
        if ti_match:
            metadata["title"] = ti_match.group(1).strip()
            continue

        # Check for lyrics line
        if TIME_PATTERN.match(line):
            lyrics_lines.append(line)

    return metadata, lyrics_lines

def parse_lrc_line(line):
    match = TIME_PATTERN.match(line)
    if not match:
        return None
    
    mm = int(match.group(1))
    ss = float(match.group(2))
    text = match.group(3).strip()

    timestamp = mm * 60 + ss
    return timestamp, text

def format_timestamp(ts):
    mm = int(ts // 60)
    ss = ts % 60
    return f"[{mm:02d}:{ss:05.2f}]"

def convert_to_xlrc(lines, title, artist, language, singer="A"):
    xlrc_lines = []
    xlrc_lines.append(f"@title: {title}")
    xlrc_lines.append(f"@artist: {artist}")
    xlrc_lines.append(f"@language: {language}")
    xlrc_lines.append("")

    id_counter = 1
    last_ts = None

    for line in lines:
        parsed = parse_lrc_line(line)
        if not parsed:
            continue

        ts, text = parsed
        if last_ts == ts:
            xlrc_lines.append(
                f"{format_timestamp(ts)}{{ref={id_counter-1};singer={singer};lang=en}}{text}"
            )
        else:
            xlrc_lines.append(
                f"{format_timestamp(ts)}{{id={id_counter};singer={singer};lang={language}}}{text}"
            )
            id_counter += 1
        last_ts = ts

    return "\n".join(xlrc_lines)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("LRC to XLRC Converter")
        self.root.geometry("500x450")

        # Input File
        tk.Label(root, text="Step 1: Select Source LRC File", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.btn_browse = tk.Button(root, text="Browse File", command=self.browse_file)
        self.btn_browse.pack(pady=5)
        
        self.file_path = tk.StringVar()
        self.entry_file = tk.Entry(root, textvariable=self.file_path, width=60, state='readonly')
        self.entry_file.pack(pady=5)

        # Metadata (Title/Artist)
        tk.Label(root, text="Step 2: Song Information (Auto-filled if available)", font=("Arial", 10, "bold")).pack(pady=(15, 0))
        
        tk.Label(root, text="Title:").pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack(pady=2)

        tk.Label(root, text="Artist:").pack()
        self.artist_entry = tk.Entry(root, width=40)
        self.artist_entry.pack(pady=2)

        # Config
        tk.Label(root, text="Step 3: Configuration", font=("Arial", 10, "bold")).pack(pady=(15, 0))
        
        tk.Label(root, text="Output Filename:").pack()
        self.output_name = tk.Entry(root, width=40)
        self.output_name.insert(0, "output.xlrc")
        self.output_name.pack(pady=2)

        tk.Label(root, text="Language Code (e.g., en, ja):").pack()
        self.lang_code = tk.Entry(root, width=15)
        self.lang_code.insert(0, "en")
        self.lang_code.pack(pady=2)

        # Run
        self.btn_convert = tk.Button(
            root, text="CONVERT AND SAVE", command=self.run_conversion, 
            bg="#28a745", fg="white", font=("Arial", 11, "bold"), height=2, width=20
        )
        self.btn_convert.pack(pady=20)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("LRC files", "*.lrc"), ("All files", "*.*")])
        if filename:
            self.file_path.set(filename)
            # Auto-scan file for metadata
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                metadata, _ = parse_lrc_content(lines)
                
                # Update UI entries
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(0, metadata["title"])
                self.artist_entry.delete(0, tk.END)
                self.artist_entry.insert(0, metadata["artist"])
            except Exception as e:
                print(f"Metadata scan failed: {e}")

    def run_conversion(self):
        input_file = self.file_path.get()
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        output_file_name = self.output_name.get()
        lang = self.lang_code.get()

        if not input_file:
            messagebox.showerror("Error", "Please select an LRC file first!")
            return
        if not title or not artist:
            messagebox.showerror("Error", "Please enter Title and Artist!")
            return

        try:
            save_dir = Path(input_file).parent
            output_full_path = save_dir / output_file_name

            with open(input_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            _, lyrics = parse_lrc_content(lines)
            result = convert_to_xlrc(lyrics, title, artist, lang)

            with open(output_full_path, "w", encoding="utf-8") as f:
                f.write(result)

            messagebox.showinfo("Success", f"Done!\nSaved as: {output_full_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
