import pyautogui, smtplib, ssl


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "erabaroust@gmail.com"
receiver_email = "marc.lefevre@noos.fr"
password = "cmymrwjcfmqsaoxr"
message = pyautogui.prompt(text="", title="Quel message veux  tu t'envoyer ?", default="")

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)