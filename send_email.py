from load_data import get_config
import smtplib


def send_email(subject, body):
    config = get_config()

    gmail_user = config.get("gmailUSER")
    gmail_pwd = config.get("gmailPASS")
    FROM = gmail_user
    TO = gmail_user
    CC = [config.get("ian"), config.get("andrew"), config.get("alfredo")]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nCC: %s\nSubject: %s\n\n%s
    """ % (FROM, TO, ", ".join(CC), SUBJECT, TEXT)
    TO = [TO] + CC
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
