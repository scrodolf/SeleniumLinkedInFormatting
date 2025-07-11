# Selenium LinkedIn Poster

This repo provides a very small script that logs in to LinkedIn and posts text
for you. It is aimed at macOS users who are new to Python and Selenium.

## Setup

1. **Install Python 3** – on macOS the easiest way is with [Homebrew](https://brew.sh):
   ```bash
   brew install python
   ```

2. **Install ChromeDriver** – download the version that matches your installed
   Google Chrome from <https://chromedriver.chromium.org/downloads> and place the
   `chromedriver` binary somewhere in your `PATH` (for example `/usr/local/bin`).

3. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Add your LinkedIn credentials** – copy `config_example.json` to
   `config.json` and edit it with your LinkedIn email and password.

## Posting

Run the script with:

```bash
python3 main.py
```

You will be asked to paste the text of your LinkedIn post. End input with an
empty line. The script converts basic `**bold**` and `*italic*` markdown to the
special unicode characters LinkedIn supports and then publishes the post using
Selenium.

## Scheduling (optional)

If you want to schedule posts in the future you can build on top of this script
using the `schedule` Python package. See `Scheduling with schedule` in this repo
for a minimal example.
