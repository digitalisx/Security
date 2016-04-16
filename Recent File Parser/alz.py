import os
import sys
import _winreg

_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
_key = _winreg.OpenKey(_reg, r"Software\\ESTsoft\\ALZip\\MRUOpen", 0, _winreg.KEY_ALL_ACCESS)

print "\nALZip MRU Viewer\n"

try:
	
	count = 0
	
	while 1:
		
		name, value, type = _winreg.EnumValue(_key, count)
		
		print name + ' : ' + value
		
		count = count + 1

except WindowsError:
	pass