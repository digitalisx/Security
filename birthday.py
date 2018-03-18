import os
import datetime

birthday = datetime.date.today()
birthday_convert = str(brithday.isoformat())

if(birthday_convert == "1999-01-08"):
  print("Congratulation, You are a good python student! :)")
  
else:
  print("Good Job!")
