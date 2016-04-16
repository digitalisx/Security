import os
import sys

def Word():

	import _winreg

	_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
	_key = _winreg.OpenKey(_reg, r"Software\\Microsoft\\Office\\15.0\\Word\\User MRU\\LiveId_F49CAD07FDF54EB9E863875EAB231852FEEEEABB2E9910A91DC7FA2DB9D7ABD9\\File MRU", 0, _winreg.KEY_ALL_ACCESS)

	try:
		count = 0
		while 1:
			name, value, type = _winreg.EnumValue(_key, count)
			print name + ' : ' + value
			count = count + 1
	except WindowsError:
		pass

def Excel():

	import _winreg

	_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
	_key = _winreg.OpenKey(_reg, r"Software\\Microsoft\\Office\\15.0\\Excel\\User MRU\\LiveId_F49CAD07FDF54EB9E863875EAB231852FEEEEABB2E9910A91DC7FA2DB9D7ABD9\\File MRU", 0, _winreg.KEY_ALL_ACCESS)

	try:
		count = 0
		while 1:
			name, value, type = _winreg.EnumValue(_key, count)
			print name + ' : ' + value
			count = count + 1
	except WindowsError:
		pass

def Powerpoint():

	import _winreg

	_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
	_key = _winreg.OpenKey(_reg, r"Software\\Microsoft\\Office\\15.0\\PowerPoint\\User MRU\\LiveId_F49CAD07FDF54EB9E863875EAB231852FEEEEABB2E9910A91DC7FA2DB9D7ABD9\\File MRU", 0, _winreg.KEY_ALL_ACCESS)

	try:
		count = 0
		while 1:
			name, value, type = _winreg.EnumValue(_key, count)
			print name + ' : ' + value
			count = count + 1
	except WindowsError:
		pass

print "\nMicrosoft Office 2013 Artifact"

print "\nWord\n"
Word()

print "\nExcel\n"
Excel()

print "\nPowerpoint\n"
Powerpoint()