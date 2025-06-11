import os, time
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_FROM_NUMBER")
customer_number = os.getenv("TWILIO_TO_NUMBER")

client = Client(account_sid, auth_token)

message_text = (
    "Hello. This is a liquor order call for account number 48761. "
    "Please process our monthly order. Thank you."
)

def make_call_with_retry(max_retries=3, wait_minutes=5):
    attempt = 1
    while attempt <= max_retries:
        print(f"[INFO] Attempt {attempt} to call {customer_number}")
        try:
            call = client.calls.create(
                twiml=f'<Response><Say voice="alice">{message_text}</Say></Response>',
                to=customer_number,
                from_=twilio_number
            )
            call_sid = call.sid
            time.sleep(10)
            call_status = client.calls(call_sid).fetch().status
            print(f"[INFO] Call status: {call_status}")
            with open("call_log.txt", "a") as f:
                f.write(f"Attempt {attempt} - Status: {call_status}\n")
            if call_status in ["completed", "in-progress", "ringing"]:
                break
        except Exception as e:
            print(f"[ERROR] Exception: {e}")
            with open("call_log.txt", "a") as f:
                f.write(f"Attempt {attempt} - Error: {e}\n")
        attempt += 1
        time.sleep(wait_minutes * 60)

scheduler = BlockingScheduler()
trigger = CronTrigger(day='last', hour=9, minute=0)
scheduler.add_job(make_call_with_retry, trigger)

print("[BOT ACTIVE] Waiting for the last day of the month at 9:00 AM...")
scheduler.start()