import pyautogui, smtplib, ssl


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "smam.elliot@gmail.com"
receiver_email = "marc.lefevre@noos.fr"
password = "obcbfuncgjxzdvti"
message = pyautogui.prompt(text="", title="Quel message veux  tu t'envoyer ?", default="")

if __name__ == "__main__":
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted  
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)