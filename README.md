# 🍾 Liquor Order Call Bot

This Python bot automatically calls **one customer** every month at **9:00 AM on the last day of the month** using the [Twilio API](https://www.twilio.com/docs/voice). It delivers a preset liquor order message and retries if the call fails.

---

## 🛠 Features

- ✅ Scheduled call every month at 9:00 AM
- 🔁 Retry logic if the call doesn’t connect
- 📞 Uses Twilio to make voice calls
- 📱 Works on Android (via Termux) or any PC
- 📝 Logs each call attempt to a local file

---

## 🔧 Setup Instructions

### 1. Install Python dependencies
Make sure you have Python installed (Termux: `pkg install python`)

`pip install -r requirements.txt`

### 2. Set environment variables
Before running the bot, set these environment variables with your Twilio credentials:

`
export TWILIO_ACCOUNT_SID=your_account_sid
export TWILIO_AUTH_TOKEN=your_auth_token
export TWILIO_FROM_NUMBER=+1xxxxxxxxxx
export TWILIO_TO_NUMBER=+1xxxxxxxxxx
`
> Replace the numbers with your actual Twilio and customer phone numbers.
---
### 3. Run the Bot

`bot.py`
>The bot will stay running and automatically call the customer at 9:00 AM on the last day of each month.

### 📋 Example Message
> “Hello. This is a liquor order call for account number 48761. Please process our monthly order. Thank you.”

---

### ⚠️ Important Notes

• Ensure your Twilio number is voice-enabled.

• If you run on Android via Termux, keep the session alive using `termux-wake-lock` or tools like Termux:Boot.

• This is a basic implementation for one number. You can extend it for multiple calls or advanced IVR flows.

---

### ✅ License

>Let me know if you want this auto-uploaded to your GitHub repo or want help customizing the message or expanding to multiple customers.
