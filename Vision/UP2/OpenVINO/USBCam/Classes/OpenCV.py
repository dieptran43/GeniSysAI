############################################################################################
#
# Repository:    HIAS GeniSysAI
# Project:       OpenVINO USB Camera Security System
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
#
# Title:         OpenCV Class
# Description:   OpenCV Canera Class.
# License:       MIT License
# Last Modified: 2020-08-28
#
############################################################################################

import cv2
import time

import multiprocessing as mp

from Classes.Helpers import Helpers

class OpenCV():
	""" OpenCV Class

	OpenCV IP Canera Class.
	"""

	def __init__(self, stream):
		""" Initializes the class. """

		self.Helpers = Helpers("OpenCV")

		self.parent, child = mp.Pipe()
		self.p = mp.Process(target=self.update, args=(child, stream))
		self.p.daemon = True
		self.p.start()

		self.Helpers.logger.info("OpenCV class initialized.")

	def end(self):
		""" Initializes the class. """

		self.parent.send(2)

	def update(self, conn, stream):
		""" Initializes the class. """

		self.Helpers.logger.info("Connecting to USB camera.")
		cap = cv2.VideoCapture(stream)
		self.Helpers.logger.info("Connected to Foscam.")
		run = True

		while run:
			cap.grab()
			rec_dat = conn.recv()

			if rec_dat == 1:
				ret,frame = cap.read()
				conn.send(frame)

			elif rec_dat ==2:
				cap.release()
				run = False

		conn.close()
		self.Helpers.logger.info("USB camera connection closed.")

	def get(self,resize=None):
		""" Gets the frames. """

		self.parent.send(1)
		frame = self.parent.recv()
		self.parent.send(0)

		if resize == None:
			return frame
		else:
			return self.resize(frame, resize)

	def resize(self, frame, percent=65):

		return cv2.resize(frame,None,fx=percent,fy=percent)