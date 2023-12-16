# Python News Alert Application v1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-white.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9-gold.svg)](https://www.python.org/downloads/release/python-390/)
[![Version](https://img.shields.io/badge/version-1.0-silver.svg)](https://github.com/your-username/your-repo)

## Overview

This Python script is a simple news alert application that fetches the latest news articles related to "apple" using the News API, processes the data, and sends a test email with the headlines and briefs.

## Prerequisites

- Python 3.8 or higher
- News API key (replace `API_KEY` in the script with your actual API key)
- Gmail account and app password for sending emails

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/akumarm23/Day36-NewsAlert.git
   ```

2. Install the required packages:

   ```bash
   pip install requests
   ```

3. Configure the script:

   - Replace `API_KEY`, `MY_EMAIL`, `PASSWORD`, and `APP_PASS` in the script with your actual values.

## Usage

Run the script:

```bash
python main.py
```

The script will fetch the latest news, process the data, and send a test email to the specified Gmail account.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
