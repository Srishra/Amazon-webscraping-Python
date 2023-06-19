## Amazon Price Drop Alert Script
This script is designed to scrape the price of a product from Amazon and send an email notification if the price drops below a certain threshold.

## Prerequisites

Install the required dependencies using pip: pip install -r requirements.txt:

## Configuration

1. Open the script file in a text editor.

2. Update the `URL` variable with the URL of the Amazon product you want to track.

3. Configure the email settings in the `send_email` function:

   - `sender_email`: Your Gmail email address from which the alert email will be sent.
   - `receiver_email`: The email address where you want to receive the price drop alerts.

   **Note:** In order to send emails using Gmail, you need to enable two-step verification and create an app password. Follow the steps below to set it up:

   - Enable Two-Step Verification:
     1. Go to your Google Account settings (https://myaccount.google.com).
     2. Click on "Security" in the left sidebar.
     3. Under "Signing in to Google", click on "2-Step Verification".
     4. Follow the instructions to enable two-step verification and set it up for your account.

   - Create App Password:
     1. Go to your Google Account settings (https://myaccount.google.com).
     2. Click on "Security" in the left sidebar.
     3. Under "Signing in to Google", click on "App Passwords".
     4. Select "Mail" as the app and "Other" as the device.
     5. Click "Generate" and copy the generated app password.
     6. Replace the `password` variable in the script with the generated app password.

4. Customize the price threshold in the `if price_int < 50000` condition. You can change `50000` to the desired price at which you want to receive the alert.

5. Update the file name in the `with open('AmazonWebScraper_ipad.csv', 'a+', newline='', encoding='UTF8') as f` line to the desired name for the CSV file where the product details will be logged.

## Usage

1. Save the modified script file with a `.py` extension (e.g., `amazon_price_alert.py`).

2. Open the command line or terminal and navigate to the directory where the script file is located.

3. Run the script by executing the following command:python amazon_price_alert.py

4. The script will start scraping the Amazon product page and checking the price at regular intervals (every 24 hours).

5. If the price drops below the specified threshold, an email will be sent to the designated email address with the product information.

6. The script will also log the product details (title, price, date, and time) in the specified CSV file.

## Customization

- You can modify the scraping logic in the `check_price` function to extract additional product information if needed.

- Adjust the time interval in the `time.sleep` function to change how frequently the script checks for price drops (in seconds).

## Disclaimer

This script is for educational and personal use only. Use it responsibly and ensure compliance with any applicable terms of service and legal requirements. The script is not affiliated with Amazon and may be subject to changes in the Amazon website structure, which could affect its

