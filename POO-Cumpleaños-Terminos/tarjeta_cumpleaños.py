from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import mysql.connector

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "naoreto3@gmail.com"
smtp_password = "mrhhoolaxryspyhs"
from_address = 'Nao Reto 3 <naoreto3@gmail.com>'
subject = "Feliz cumpleaños!"
body = ''
today = datetime.datetime.now()

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Grettel33",
    database="empleados"
)

nombres = []
direcciones_correo = []
cursor = conexion.cursor()
cursor.execute("SELECT nombre, correo, fecha_de_nacimiento FROM empleados2")
for nombre, direccion_correo, fecha_nacimiento in cursor:
    if fecha_nacimiento.month == today.month and fecha_nacimiento.day == today.day:
        nombres.append(nombre)
        direcciones_correo.append(direccion_correo)

mensaje_personalizado = """\
<!doctype html>
<html ⚡4email data-css-strict>
<head>
	<meta charset="utf-8">
	<style amp4email-boilerplate>
		body{visibility:hidden}
	</style>
	<script async src="https://cdn.ampproject.org/v0.js"></script>
	<style amp-custom>
		.es-desk-hidden { display:none; float:left; overflow:hidden; width:0; max-height:0; line-height:0;}s { text-decoration:line-through;}body { width:100%;}body { font-family:helvetica, "helvetica neue", arial, verdana, sans-serif;}table { border-collapse:collapse; border-spacing:0px;}table td, html, body, .es-wrapper { padding:0; Margin:0;}.es-content, .es-header, .es-footer { table-layout:fixed; width:100%;}p, hr { Margin:0;}h1, h2, h3, h4, h5 { Margin:0; line-height:120%; font-family:helvetica, "helvetica neue", arial, verdana, sans-serif;}.es-left { float:left;}.es-right { float:right;}.es-p5 { padding:5px;}.es-p5t { padding-top:5px;}.es-p5b { padding-bottom:5px;}.es-p5l { padding-left:5px;}.es-p5r { padding-right:5px;}.es-p10 { padding:10px;}.es-p10t { padding-top:10px;}.es-p10b { padding-bottom:10px;}.es-p10l { padding-left:10px;}.es-p10r { padding-right:10px;}.es-p15 { padding:15px;}.es-p15t { padding-top:15px;}.es-p15b { padding-bottom:15px;}.es-p15l { padding-left:15px;}.es-p15r { padding-right:15px;}.es-p20 { padding:20px;}.es-p20t { padding-top:20px;}.es-p20b { padding-bottom:20px;}.es-p20l { padding-left:20px;}.es-p20r { padding-right:20px;}.es-p25 { padding:25px;}.es-p25t { padding-top:25px;}.es-p25b { padding-bottom:25px;}.es-p25l { padding-left:25px;}.es-p25r { padding-right:25px;}.es-p30 { padding:30px;}.es-p30t { padding-top:30px;}.es-p30b { padding-bottom:30px;}.es-p30l { padding-left:30px;}.es-p30r { padding-right:30px;}.es-p35 { padding:35px;}.es-p35t { padding-top:35px;}.es-p35b { padding-bottom:35px;}.es-p35l { padding-left:35px;}.es-p35r { padding-right:35px;}.es-p40 { padding:40px;}.es-p40t { padding-top:40px;}.es-p40b { padding-bottom:40px;}.es-p40l { padding-left:40px;}.es-p40r { padding-right:40px;}.es-menu td { border:0;}a { text-decoration:underline;}p, ul li, ol li { font-family:helvetica, "helvetica neue", arial, verdana, sans-serif; line-height:150%;}ul li, ol li { Margin-bottom:15px; margin-left:0;}.es-menu td a { text-decoration:none; display:block; font-family:helvetica, "helvetica neue", arial, verdana, sans-serif;}.es-menu amp-img, .es-button amp-img { vertical-align:middle;}.es-wrapper { width:100%; height:100%;}.es-wrapper-color, .es-wrapper { background-color:#F6F6F6;}.es-header { background-color:transparent;}.es-header-body { background-color:transparent;}.es-header-body p, .es-header-body ul li, .es-header-body ol li { color:#999999; font-size:14px;}.es-header-body a { color:#999999; font-size:14px;}.es-content-body { background-color:#FFFFFF;}.es-content-body p, .es-content-body ul li, .es-content-body ol li { color:#040404; font-size:14px;}.es-content-body a { color:#040404; font-size:14px;}.es-footer { background-color:transparent;}.es-footer-body { background-color:#FFFFFF;}.es-footer-body p, .es-footer-body ul li, .es-footer-body ol li { color:#FFFFFF; font-size:14px;}.es-footer-body a { color:#FFFFFF; font-size:14px;}.es-infoblock, .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li { line-height:120%; font-size:12px; color:#CCCCCC;}.es-infoblock a { font-size:12px; color:#CCCCCC;}h1 { font-size:30px; font-style:normal; font-weight:bold; color:#040404;}h2 { font-size:24px; font-style:normal; font-weight:bold; color:#040404;}h3 { font-size:20px; font-style:normal; font-weight:bold; color:#040404;}.es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:30px;}.es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:24px;}.es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px;}a.es-button, button.es-button { display:inline-block; background:#38C2F1; border-radius:25px; font-size:18px; font-family:helvetica, "helvetica neue", arial, verdana, sans-serif; font-weight:bold; font-style:normal; line-height:120%; color:#FFFFFF; text-decoration:none; width:auto; text-align:center; padding:10px 30px 10px 30px;}.es-button-border { border-style:solid solid solid solid; border-color:#38C2F1 #38C2F1 #38C2F1 #38C2F1; background:#38C2F1; border-width:0px 0px 0px 0px; display:inline-block; border-radius:25px; width:auto;}@media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150% } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120% } h1 { font-size:28px; text-align:center } h2 { font-size:26px; text-align:center } h3 { font-size:20px; text-align:center } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:28px } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px } .es-menu td a { font-size:12px } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:12px } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:14px } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:14px } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:11px } *[class="gmail-fix"] { display:none } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left } .es-m-txt-r amp-img { float:right } .es-m-txt-c amp-img { margin:0 auto } .es-m-txt-l amp-img { float:left } .es-button-border { display:block } a.es-button, button.es-button { font-size:14px; display:block; border-left-width:0px; border-right-width:0px } .es-btn-fw { border-width:10px 0px; text-align:center } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100% } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%; max-width:600px } .es-adapt-td { display:block; width:100% } .adapt-img { width:100%; height:auto } td.es-m-p0 { padding:0px } td.es-m-p0r { padding-right:0px } td.es-m-p0l { padding-left:0px } td.es-m-p0t { padding-top:0px } td.es-m-p0b { padding-bottom:0 } td.es-m-p20b { padding-bottom:20px } .es-mobile-hidden, .es-hidden { display:none } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto; overflow:visible; float:none; max-height:inherit; line-height:inherit } tr.es-desk-hidden { display:table-row } table.es-desk-hidden { display:table } td.es-desk-menu-hidden { display:table-cell } .es-menu td { width:1% } table.es-table-not-adapt, .esd-block-html table { width:auto } table.es-social { display:inline-block } table.es-social td { display:inline-block } .es-desk-hidden { display:table-row; width:auto; overflow:visible; max-height:inherit } }
	</style>
</head>
<body>
	<div class="es-wrapper-color">
		<!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#f6f6f6"></v:fill> </v:background><![endif]-->
		<table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
			<tr>
				<td valign="top">
					<table cellpadding="0" cellspacing="0" class="es-content" align="center">
						<tr>
							<td align="center">
								<table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
									<tr>
										<td align="left" style="background-position: center top;background-color: #202447" bgcolor="#202447">
											<table cellpadding="0" cellspacing="0" width="100%">
												<tr>
													<td width="600" align="center" valign="top">
														<table cellpadding="0" cellspacing="0" width="100%" style="background-image:url(https://mwzezu.stripocdn.email/content/guids/CABINET_58bdfab47b91421ec71c0b7efc174ad6/images/3021564570245556.gif);background-position: left top;background-repeat: no-repeat" role="presentation">
															<tr>
																<td align="center" height="118"></td>
															</tr>
															<tr>
																<td align="center">
																	<h1 style="color: #ffffff">Un recordatorio importante<br></h1>
																	<h1 style="color: #ffffff">De una fecha más importante.<br></h1></td>
															</tr>
															<tr>
																<td align="center" height="118"></td>
															</tr>
														</table>
													</td>
												</tr>
											</table>
										</td>
									</tr>
									<tr>
										<td class="es-p20t es-p10b es-p20r es-p20l" align="left" style="background-position: center top">
											<table cellpadding="0" cellspacing="0" width="100%">
												<tr>
													<td width="560" align="center" valign="top">
														<table cellpadding="0" cellspacing="0" width="100%" style="background-position: left top" role="presentation">
															<tr>
																<td align="center" class="es-p10b es-m-txt-c">
																	<h2>El día de hoy, nuestro colega [NOMBRE DE LA PERSONA] celebra su cumpleaños.</h2></td>
															</tr>
															<tr>
																<td align="center" class="es-m-txt-c">
																	<h3>[NOMBRE DE LA PERSONA]</h3></td>
															</tr>
															<tr>
																<td align="center" class="es-p10b es-m-txt-l">
																	<p>Recibe una felicitación de parte de todos, esperamos que te la pases chido-NAO.</p>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
		</table>
	</div>
</body>
</html>
"""

for direccion_correo, nombre in zip(direcciones_correo, nombres):
    mensaje_personalizado_con_nombre = mensaje_personalizado.replace("[NOMBRE DE LA PERSONA]", nombre)
    mensaje = MIMEMultipart('related')
    mensaje['Subject'] = subject
    mensaje['From'] = from_address
    mensaje['To'] = direccion_correo
    mensaje.attach(MIMEText(mensaje_personalizado_con_nombre, 'html'))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_address, direccion_correo, mensaje.as_string())
            print(f"Correo enviado exitosamente a {direccion_correo}")
    except Exception as e:
        print(f"Error al enviar correo a {direccion_correo}: {e}")