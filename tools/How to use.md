## LRC to XLRC Converter
This is a simple GUI-based Python tool to convert standard LRC lyrics files into the XLRC format. It automatically extracts song metadata (Artist and Title) and allows for easy customization of output settings.

### 🚀 Features
Automatic Metadata Extraction: Scans .lrc files for [ar:Artist] and [ti:Title] tags.

User-Friendly GUI: Simple interface built with Tkinter (no extra dependencies required).

Customizable: Manually edit Title, Artist, and Language codes before conversion.

Batch Ready: Saves the converted file in the same directory as the source.

### 🛠 How to Use
1. Prerequisites
Make sure you have Python 3.x installed on your system.

2. Running the Application
Download the lrc2xlrc_gui_pro.py file and run it via terminal or command prompt:

Bash
python lrc2xlrc.py

3. Steps to Convert
Select Source LRC File: Click the "Browse File" button and pick your .lrc file.

Verify Information:

The app will automatically fill in the Title and Artist if they exist in the file.

If they are missing or incorrect, you can type them in manually.

Configure Settings:

Set the Output Filename (default is output.xlrc).

Set the Language Code (e.g., en for English, ja for Japanese).

Convert: Click "CONVERT AND SAVE". The new file will be created in the same folder as your original file.
