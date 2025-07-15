# LinkedIn Post Formatter

This small script converts Markdown-style `**bold**` and `*italic*` (or `_italic_`) markers into the Unicode characters recommended in the [LinkedIn post formatting guide](https://reply.io/blog/linkedin-post-formatting/). After formatting, the post is copied to the macOS clipboard (requires `pyperclip`) and saved to a `.txt` file named after the first paragraph of the post.

## Setup

1. Install Python 3 if it's not already available.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Copy your LinkedIn post draft to the clipboard.
2. Run the script:

   ```bash
   python format_linkedin_post.py
   ```

The formatted post will be placed on your clipboard and saved to a `.txt` file in the same directory.
