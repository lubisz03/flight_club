# Flight Club App

## About:

This Python app automates the process of finding budget-friendly flights. It utilizes the Sheety API to fetch user-defined price thresholds from Google Sheets and the Tequila Kiwi API for real-time flight price tracking. When flight prices fall below these thresholds, the app sends instant email notifications via smtplib. Designed for simplicity and efficiency, it's an essential tool for cost-conscious travelers.

## config.py Set-Up:

![](/screenshots/config-py.png)

## Example Google Sheet:

![](/screenshots/example-google-sheet.png)

## Installation Guide:

1. Create virtual env
2. Run `pip install -r requirements.txt`
3. Set the `config.py` file
4. Run the code

## Technologies:

- Python :white_check_mark:
- Sheety API :white_check_mark:
- Tequila Kiwi API :white_check_mark:
- smtplib :white_check_mark:
