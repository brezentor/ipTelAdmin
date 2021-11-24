# pip install pyodbc
import pyodbc
import re
import subprocess

def execresult(result):
      try:
          inforesult = result[0]
      except:
          print("\n\n\t||============================================||"
                "\n\t||  НЕ ЗНАЙДЕНО ІНФО В БД ІЗ ТАКИМИ ДАНИМИ "
                "\n\t||============================================||"
                "\n")
      else:
          infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
          print("\n\n\t||============================================||"
                "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - " + str(infores[2]).strip("'") + " "
                "\n\t||  МАС-АДРЕСА - " + str(infores[0]).strip("'") + " "
                "\n\t||  IНВЕНТАРНИЙ НОМЕР - " + str(infores[4]).strip("'") + " "
                "\n\t||  IP-АДРЕСА - " + str(infores[1]).strip("'") + " "
                "\n\t||  ПРИСВОЄНИЙ НОМЕР - " + str(infores[3]).strip("'") + " "
                "\n\t||  ЛОКАЦIЯ - " + str(infores[5]).strip("'") + " "
                "\n\t||============================================||"
                "\n")

def sqlconn(query):
      connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
      cursor = connect.cursor()
      cursor.execute(query)
      result = cursor.fetchall()
      connect.close()
      execresult(result)

print("\n\n\t||============================================||"
      "\n\t||  ЩОБ ОТРИМАТИ IНФО ПРО ПРИСТРIЙ            ||"
      "\n\t||  ВВЕДIТЬ НОМЕР ТЕЛЕФОНУ, IР АДРЕСУ,        ||"
      "\n\t||  МАС АДРЕСУ АБО IНВЕНТРАНИЙ НОМЕР          ||"
      "\n\t||============================================||"
      "\n")
quer = input("Введіть дані для пошуку та натиснiть ENTER..")
numbq = r'\d{3}'
macq = r'[\d\w]{12}'
ipq = r'\d{2}.\d{2}.\d{1}.\d{1,3}'
invq = r'[\w-]{5,8}'

# 1================================
resn = re.match(numbq, str(quer))
# 2================================
resm = re.match(macq, str(quer))
# 3================================
resip = re.match(ipq, str(quer))
# 4================================
resinv = re.match(invq, str(quer))

# умова + sql-query==================================
if (resm != None):
      resultmac = str(resm[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [MacAddress] = '{ma}'".format(ma=resultmac))
      sqlconn(query)
elif ((resm == None) and (resinv != None)):
      resultinv = str(resinv[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [InvNumber] = '{invn}'".format(invn=resultinv))
      sqlconn(query)
elif ((resm == None) and (resinv == None) and (resn != None)):
      resultnum = str(resn[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [PhoneNumber] = '{phn}'".format(phn=resultnum))
      sqlconn(query)
else:
      resultip = str(resip[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{ipa}'".format(ipa=resultip))
      sqlconn(query)

while True:
      endinfo = input("Натисніть 1, щоб вийти з програми або 2, щоб повернутись до головного меню..")
      if (int(endinfo) >= 1) and (int(endinfo) <= 2):
          break
print(endinfo)
if (endinfo == "1"):
      exit()
elif (endinfo == "2"):
      gotomain = subprocess.Popen(["python", "D:\\scripts\\git\\ipTelAdmin\\main.py"])
      gotomain.communicate()
else:
      print("else")