# Set credentials
import smtplib
import pandas

name_account = "Naoreto3"
email_account = "naoreto3@gmail.com"
password_account = "mrhhoolaxryspyhs" 

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_account, password_account)

email_df = pandas.read_csv("correos.csv", encoding="ISO-8859-1")

all_names = email_df['name']
all_emails = email_df['email']
all_subjects = email_df['asunto']
all_messages = email_df['mensaje']

for i in range(len(email_df)):

    name = all_names[i]
    email = all_emails[i]
    
    subject = all_subjects[i] + ', ' + all_names[i] + '!'

    message = ('Hey, ' + all_names[i] + '!\n\n' +
              all_messages[i] + '\n\n'
              'Te deseamos lo mejor,\n' +
              name_account)

    sent_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(name_account, email_account, name, email, subject, message))
    
    try:
        server.sendmail(email_account, [email], sent_email)
    except Exception:
        print('Could not send email to {}. Error: {}\n'.format(email, str(Exception)))

server.close()