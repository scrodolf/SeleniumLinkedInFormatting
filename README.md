# LinkedIn Post Formatter

This repository contains a simple utility to convert Markdown-style `**bold**` and `*italic*` text into the Unicode characters supported by LinkedIn posts. The formatted text is copied to the macOS clipboard and saved as a `.txt` file.

## Usage
1. Ensure you are running on macOS so the `pbcopy` command is available.
2. Edit `format_to_clipboard.py` and update `POST_DRAFT` with the content of your LinkedIn post.
3. Run the script:
   ```bash
   python3 format_to_clipboard.py
   ```
4. The formatted post will be placed in the system clipboard and saved in a text file. The filename is derived from the first paragraph of your post.

The conversion mappings are implemented in `linkedin_formatter.py`.
