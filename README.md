# LinkedIn Posting Automation

This repository contains simple Python scripts for publishing posts to LinkedIn
using Selenium. It was adapted to be easy to run on **macOS**.

## Quick start (macOS)

1. Install [Python 3](https://www.python.org/downloads/mac-osx/). The builtin
   version on macOS may work, but installing via [Homebrew](https://brew.sh/) is
   recommended:
   ```bash
   brew install python3
   ```
2. Clone the repository and create a virtual environment:
   ```bash
   git clone <repo-url>
   cd SeleniumLinkedInFormatting
   python3 -m venv env
   source env/bin/activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your LinkedIn credentials in environment variables:
   ```bash
   export LINKEDIN_USER="your_email@example.com"
   export LINKEDIN_PASS="your_password"
   ```
5. Run the script and paste the text for your post when prompted:
   ```bash
   python main.py
   ```

For scheduled posts run `python scheduler.py`. Posts are formatted from
Markdown before being sent to LinkedIn.
