import smtplib
from auth import Auth
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class UpdateMe(Auth):

	def __init__(self, host='smtp.gmail.com', port=587):

		Auth.__init__(self, host, port)

		self.__subject = "Status Update by UpdateMe"

		self.__info = "Important Info"

		self.__rows = []

		self.__status_allowed = ['info', 'success', 'danger']

		self.rows_html_file = "row.html"

		self.body_html_file = "template.html"

	def addRow(self, section, status, details):

		if status not in self.__status_allowed:
			print(f"Allowed status values are : {self.__status_allowed}")
		else:
			row = {
				'section':section,
				'status':status,
				'details':details
			}
			self.__rows.append(row)

	def showRows(self):
		i = 0
		for row in self.__rows:
			i+=1
			for k, v in rows.items():
				print(f"Row {i} : \n")
				print(f"Section : {row.section}, Status : {row.status}, Details : {row.details}\n")

	def rows_html(self):

		row_html = open(self.rows_html_file, 'r').read()

		res = ""

		i = 0
		for r in self.__rows:
			i+=1
			res = res + r.format(id=i, section=r.section, status=r.status, details=r.details)

		return rows_html

	def message_html(self):

		body_html = open(self.body_html_file, 'r').read()

		rows_html = self.rows_html()

		msg_html = body_html.format(rows=rows_html)

		return msg_html

	def raw_message(self):

		body = f"{self.__info}\n\n"
		i = 0
		for row in rows:
			i+=1
			for k, v in rows.items():
				body += f"Row {i} : \n"
				body += f"Section : {row.section}, Status : {row.status}, Details : {row.details}\n"

		return body


	def send_update(self):
		message = MIMEMultipart("alternative")
		message["Subject"] = self.__subject
		message["From"] = self.__email
		message["To"] = self.__recipient

		plain_update = self.raw_message()
		pretty_update = self.message_html()

		# Turn these into plain/html MIMEText objects
		part1 = MIMEText(plain_update, "plain")
		part2 = MIMEText(pretty_update, "html")

		# Add HTML/plain-text parts to MIMEMultipart message
		# The email client will try to render the last part first
		message.attach(part1)
		message.attach(part2)

		self.__s.sendmail(self.__email, self.__recipient, message.as_string())

	def setSubject(self, subject):
		self.__subject = subject

	def getSubject(self):
		print(f"Subject is set to {self.__subject}")

	def setInfo(self, info):
		self.__info = info

	def getInfo(self):
		print(f"Info is set to {self.__info}")