import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Send_Email(receipents,subject):

    print("Email: Process Started")

    # Set your email credentials and details
    sender_email = "cesenthil@gmail.com"
    password = "xwgr jwlg qwlz mtfg"  # This App password has to be generated in Google Account to skip 2 Factor Authentication"
    receiver_email = receipents
    #subject = "Test from Python !!!"

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ",".join(receiver_email)
    message["Subject"] = subject

    # Add body to the email
    body = "This is email was sent form Python - by CS"
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server (for Gmail, use smtp.gmail.com)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email: Process Completed")