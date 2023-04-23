from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import csv

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "naoreto3@gmail.com"
smtp_password = "mrhhoolaxryspyhs"
from_address = "naoreto3@gmail.com"
subject = "Feliz Lunes"
body = "Feliz lunes a todos"

today = datetime.today()

to_addresses = []
with open('C:\\Users\\clase\\OneDrive\\Escritorio\\NAO Evidencias\\RETO3\\correos.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        to_addresses.append(row['email'])


message = f"Subject: {subject}\n\n{body}"
msg = MIMEText(message)


msg['From'] = from_address
msg['To'] = ", ".join(to_addresses)

# Envia el mensaje
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login("naoreto3@gmail.com", "mrhhoolaxryspyhs" )
        server.send_message(msg)
        print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar correo: {e}")