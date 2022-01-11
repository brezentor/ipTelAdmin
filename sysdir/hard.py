import subprocess
import iptelmethods
import pyodbc
import sys

print("\n\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  ОТРИМАННЯ СПИСКУ ЗАРЕЗЕРВОВАНИХ IP        ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n")
getres = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\hard.ps1"])
getres.communicate()

print("\n\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||             ОЧИЩЕННЯ БАЗИ ДАНИХ            ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n")


try:
      conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=90.0.0.1; PORT=1433; DATABASE=db; UID=usr; PWD=pwd;')

except:
      print(sys.exc_info()[1])
else:
      cursor = conn.cursor()
      query = ("""TRUNCATE TABLE [dbo].[IpTelephony]""")
      try:
            cursor.execute(query)
      except:
            print(sys.exc_info()[1])
      else:
            cursor.execute(query)
            conn.commit()
            conn.close()

