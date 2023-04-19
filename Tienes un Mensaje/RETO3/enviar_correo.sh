#!/bin/bash

echo "Enviando correo electrónico..."

while IFS=',' read -r col1 col2 col3 email
do
    echo "Enviando correo a $email..."
    echo "Feliz Lunes compañeritos" | mutt -s "Feliz Lunes a Todos" -a "C:/Users/clase/OneDrive/Escritorio/NAO Evidencias/correos.csv" -- "$email"
done < correos.csv