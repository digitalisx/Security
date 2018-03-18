import os
import datetime

birthday = datetime.date.today()
birthday_convert = str(birthday.isoformat())

if(birthday_convert == "1999-01-08"):
  print("Congratulation, You are a good python student! :)")
  
else:
  print("Good Job!")
