import serial
import time
import logging



class MySerial():
	def __init__(self, portName, baudRate = 9600, timeout = 1):
		self.portName = portName
		self.baudRate = baudRate
		self.timeout = timeout
		logging.basicConfig(level=logging.INFO, format="[%(name)s] %(levelname)s \t|\t %(message)s")
		self.logger = logging.getLogger("bluetooth")

	def connect(self):
		self.logger.info("Connecting to " + str(self.portName) + " at " + str(self.baudRate) + " baud rate")
		try:
			self.serialInstance = serial.Serial(self.portName, self.baudRate, timeout=self.timeout)
		except Exception as E:
			self.logger.error("Failed to connect. " + str(E))
			quit()
		self.logger.info("Connected.")

	def write(self, stuff):
		self.logger.info("Writing '" + str(stuff)+"'")
		self.serialInstance.write(stuff)

	def read(self):
		self.logger.info("Reading...")
		data = self.serialInstance.readline()
		if data == "":
			self.logger.error("No response. Timed out.")
			return ""
		else:
			return data

	def setDebugLevel(self, level):
		if level == "debug":
			self.logger.setLevel(logging.DEBUG)
		elif level == "info":
			self.logger.setLevel(logging.INFO)
		elif level == "warning":
			self.logger.setLevel(logging.WARNING)
		elif level == "error":
			self.logger.setLevel(logging.ERROR)