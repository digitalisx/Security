import os
import sys
import _winreg

_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
_key = _winreg.OpenKey(_reg, r"Software\\HNC\\Hwp\\9.0\\HwpFrame_KOR\\RecentFile", 0, _winreg.KEY_ALL_ACCESS)

print ("\nHWP RecentFile Viewer")

try:
	count = 0
	
	while 1:
		
		name, value, type = _winreg.EnumValue(_key, count)
		
		if isinstance(value, int):
			
			print ""
		
		else :

			print name + " : " + value.decode('UTF-16').encode('cp949')

		count = count + 1

except WindowsError:
	pass