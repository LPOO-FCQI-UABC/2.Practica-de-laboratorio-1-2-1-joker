#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Project(object):
	def getName(self):
		return self.___name

	def setName(self, aName) -> None:
		self.___name = aName

	def getTheResources(self):
		return self.___theResources

	def setTheResources(self, aTheResources) -> None:
		self.___theResources = aTheResources

	def getTheEmployees(self):
		return self.___theEmployees

	def setTheEmployees(self, aTheEmployees) -> None:
		self.___theEmployees = aTheEmployees

	def getTheWorkBreakdownStructure(self):
		return self.___theWorkBreakdownStructure

	def setTheWorkBreakdownStructure(self, aTheWordBreakdownStructure) -> None:
		self.___theWorkBreakdownStructure = aTheWordBreakdownStructure

	def __init__(self):
		self.___name = None
		self.___theResources = None
		self.___theEmployees = None
		self.___theWorkBreakdownStructure = None

