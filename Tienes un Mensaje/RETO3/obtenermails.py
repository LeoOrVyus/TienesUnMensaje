import imaplib
import csv
import email
import os

# Configurar los detalles de la cuenta de Gmail
email_user = 'naoreto3@gmail.com'
email_pass = 'ascyodhcdfkfetwi'
imap_url = 'imap.gmail.com'

# Conectar con la cuenta de Gmail usando IMAP
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(email_user, email_pass)
mail.select('inbox')

# Buscar todos los correos electrónicos y obtener sus identificadores
status, data = mail.search(None, 'ALL')
mail_ids = data[0].split()

# Abrir un archivo CSV para escribir los datos
csv_file = open('correos4.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['name', 'email', 'asunto', 'mensaje'])

# Iterar a través de cada correo electrónico y extraer sus detalles
for mail_id in mail_ids:
    status, data = mail.fetch(mail_id, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extraer los detalles del correo electrónico
    email_from = email_message['From']
    email_subject = email_message['Subject']
    email_body = ''

    # Manejar el cuerpo del correo electrónico que puede estar en formato HTML o texto plano
    if email_message.is_multipart():
        for part in email_message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            if ctype == 'text/plain' and 'attachment' not in cdispo:
                email_body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
            elif ctype == 'text/html' and 'attachment' not in cdispo:
                continue  # saltar partes de HTML
    else:
        email_body = email_message.get_payload(decode=True).decode('utf-8', errors='ignore')

    # Escribir los detalles del correo electrónico en el archivo CSV
    writer.writerow([email_from.split("<")[0].strip(), email_from.split("<")[1].strip().replace(">",""), email_subject, email_body])

# Cerrar el archivo CSV y desconectar de la cuenta de Gmail
csv_file.close()
mail.close()
mail.logout()