#!/usr/bin/python
# -*- coding: UTF-8 -*-
class WorkBreakDownStructure(object):
	def getName(self):
		return self.___name

	def setName(self, aName):
		"""@ReturnType void"""
		self.___name = aName

	def getTheTasks(self):
		return self.___theTasks

	def setTheTasks(self, aTheTasks):
		"""@ReturnType void"""
		self.___theTasks = aTheTasks

	def __init__(self):
		self.___name = None
		self.___theTasks = None

