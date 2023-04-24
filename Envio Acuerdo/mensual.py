from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import mysql.connector
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "naoreto3@gmail.com"
smtp_password = "ppjeoueyukrvporx"
from_address = 'Nao Reto 3 <naoreto3@gmail.com>'
subject = "Acuerdo Confidencialidad"
body = ''

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Grettel33",
    database="empleados"
)

cursor = conexion.cursor()
cursor.execute("SELECT nombre, correo FROM empleados")
mensaje_personalizado = "Adjunto encontrarás un archivo PDF con el acuerdo de confidencialidad, leelo detalladamente ."



def crear_pdf(nombre_archivo, texto):
    """
    ACUERDO DE CONFIDENCIALIDAD Y NO DIVULGACIÓN DE INFORMACIÓN
En México, D.F. a __ de ____________ de 2014
Ambas partes se reconocen recíprocamente con capacidad para obligarse y, al efecto,
suscriben el presente Acuerdo de Confidencialidad y de No Divulgación de Información en base
a las siguientes ESTIPULACIONES:
PRIMERA.- Objeto. El presente Acuerdo se refiere a la información que EL DIVULGANTE
proporcione al RECEPTOR, ya sea de forma oral, gráfica o escrita y, en estos dos últimos casos,
ya esté contenida en cualquier tipo de documento, para identificar una(las) propuesta(s) de
innovación, o en su caso, para estructurar un(los) proyecto(s) de innovación, que se están
desarrollando / que se van a desarrollar.
SEGUNDA.- 1. EL RECEPTOR únicamente utilizará la información facilitada por EL DIVULGANTE
para el fin mencionado en la Estipulación anterior, comprometiéndose EL RECEPTOR a
mantener la más estricta confidencialidad respecto de dicha información, advirtiendo de dicho
deber de confidencialidad y secreto a sus empleados, asociados y a cualquier persona que, por
su relación con EL RECEPTOR, deba tener acceso a dicha información para el correcto
cumplimiento de las obligaciones del RECEPTOR para con EL DIVULGANTE.
2. EL RECEPTOR o las personas mencionadas en el párrafo anterior no podrán reproducir,
modificar, hacer pública o divulgar a terceros la información objeto del presente Acuerdo sin
previa autorización escrita y expresa del DIVULGANTE.
3. De igual forma, EL RECEPTOR adoptará respecto de la información objeto de este Acuerdo
las mismas medidas de seguridad que adoptaría normalmente respecto a la información
confidencial de su propia Empresa, evitando en la medida de lo posible su pérdida, robo o
sustracción.
TERCERA.- Sin perjuicio de lo estipulado en el presente Acuerdo, ambas partes aceptan que la
obligación de confidencialidad no se aplicará en los siguientes casos:
a) Cuando la información se encontrara en el dominio público en el momento de su
suministro al RECEPTOR o, una vez suministrada la información, ésta acceda al dominio
público sin infracción de ninguna de las Estipulaciones del presente Acuerdo.
b) Cuando la información ya estuviera en el conocimiento del RECEPTOR con anterioridad
a la firma del presente Acuerdo y sin obligación de guardar confidencialidad.
c) Cuando la legislación vigente o un mandato judicial exija su divulgación. En ese caso,
EL RECEPTOR notificará al DIVULGANTE tal eventualidad y hará todo lo posible por
garantizar que se dé un tratamiento confidencial a la información.
d) En caso de que EL RECEPTOR pueda probar que la información fue desarrollada o
recibida legítimamente de terceros, de forma totalmente independiente a su relación
con EL DIVULGANTE.
CUARTA.- Los derechos de propiedad intelectual de la información objeto de este Acuerdo
pertenecen al DIVULGANTE y el hecho de revelarla al RECEPTOR para el fin mencionado en la
Estipulación Primera no cambiará tal situación.
En caso de que la información resulte revelada o divulgada o utilizada por EL RECEPTOR de
cualquier forma distinta al objeto de este Acuerdo, ya sea de forma dolosa o por mera
negligencia, habrá de indemnizar al DIVULGANTE los daños y perjuicios ocasionados, sin
perjuicio de las acciones civiles o penales que puedan corresponder a este último.
QUINTA.- Las partes se obligan a devolver cualquier documentación, antecedentes facilitados
en cualquier tipo de soporte y, en su caso, las copias obtenidas de los mismos, que constituyan
información amparada por el deber de confidencialidad objeto del presente Acuerdo en el
supuesto de que cese la relación entre las partes por cualquier motivo.
SEXTA.- El presente Acuerdo entrará en vigor en el momento de la firma del mismo por ambas
partes, extendiéndose su vigencia hasta un plazo de 5 años después de finalizada la relación
entre las partes o, en su caso, la prestación del servicio.
SÉPTIMA.- En caso de cualquier conflicto o discrepancia que pueda surgir en relación con la
interpretación y/o cumplimiento del presente Acuerdo, las partes se someten expresamente a
los Juzgados y Tribunales del Distrito Federal, con renuncia a su fuero propio, aplicándose la
legislación vigente.
Y en señal de expresa conformidad y aceptación de los términos recogidos en el presente
Acuerdo, lo firman las partes por duplicado ejemplar y a un solo efecto en el lugar y fecha al
comienzo indicados.
POR EL RECEPTOR, POR EL DIVULGANTE,
Firma:__________________________
Nombre:________________________
______________________________
Domicilio:_______________________
______________________________
______________________________
______________________________
Empresa:_______________________
______________________________
Firma:__________________________
Nombre:________________________
______________________________
Domicilio:_______________________
______________________________
______________________________
______________________________

    """

    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=texto, ln=1)
    pdf.output(nombre_archivo)


for nombre, direccion_correo in cursor:
    mensaje_personalizado_con_nombre = mensaje_personalizado.replace("[NOMBRE DE LA PERSONA]", nombre)
    mensaje = MIMEMultipart('related')
    mensaje['Subject'] = subject
    mensaje['From'] = from_address
    mensaje['To'] = direccion_correo
    mensaje.attach(MIMEText(mensaje_personalizado_con_nombre))


nombre_archivo = f"Acuerdo Confidencialidad {nombre}.pdf"
texto_pdf = "Este es un texto de ejemplo que se enviará como archivo PDF."
crear_pdf(nombre_archivo, texto_pdf)

with open(nombre_archivo, "rb") as f:
    archivo_pdf = MIMEApplication(f.read(), _subtype="pdf")
    archivo_pdf.add_header('content-disposition', 'attachment', filename=nombre_archivo)
    mensaje.attach(archivo_pdf)

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_address, direccion_correo, mensaje.as_string())
        print(f"Correo enviado exitosamente a {direccion_correo}")
except Exception as e:
        print(f"Error al enviar correo a {direccion_correo}: {e}")
