import os
import datetime

birthday = datetime.date.today()
birthday_convert = str(brithday.isoformat())

if(birthday_convert == "2017-04-17"):
  print "Congratulation Hongbeom`s Birthday! :)"
  
else:
  print "Today is normal day! :("
  os.system("Pause")
