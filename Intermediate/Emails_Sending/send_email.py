import smtplib

SENDER_EMAIL = ""  # your sender email
SENDER_PASSWORD = ""  # your sender app password in https://myaccount.google.com/u/1/apppasswords


def send_email(receiver, email_context):
    print("EMAIL HAS BEEN SENT!!")
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(from_addr=SENDER_EMAIL, to_addrs=receiver,
                        msg=email_context)
        server.quit()
