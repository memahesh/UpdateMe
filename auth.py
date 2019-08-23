import smtplib
import getpass
import re

class Auth():

	def __init__(self, host='smtp.gmail.com', port=587):

		self.__host = host
		self.__port = port

		self.__s = smtplib.SMTP(self.__host, self.__port)

		self.login()

		self.recipient()

		return f"Emails will be sent from {self.__email} to {self.recipient}"

	def login(self):

		while(True):
			while(True):
				EMAIL = input("Your Email Address : ")
				if(self.check_email_address(EMAIL)):
					self.__email = EMAIL
					break

			self.__pass = getpass.getpass(prompt='Password : ')

			try:
				self.__s.login(self.__email, self.__pass)

			except Exception as e:
				print(f'Encountered the following error : \n {e}')
				
			else:
				print("Authentication Confirmed")
				break

	def recipient(self, email):
		while(True):
			EMAIL = input("Recipient Email Address : ")
			if(self.check_email_address(EMAIL)):
				self.__recipient = EMAIL
				break

	def check_email_address(self, address):
		# Checks if the address match regular expression
		is_valid = re.search('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', address)
		# If there is a matching group
		if is_valid:
			return True
		else:
			print('It looks that provided mail is not in correct format. \n'
			'Please make sure that you have "@" and "." in your address \n')
			return False

	def setHost(self, host):
		self.__host = host

	def getHost(self):
		return f"Host is set to {self.__host}"

	def setPort(self, port):
		self.__port = port

	def getPort(self):
		return f"Port is set to {self.__port}"

	def setRecipient(self, recipient):
		self.__recipient = recipient

	def getRecipient(self):
		return f"Recipient Email Address is set to {self.__recipient}"