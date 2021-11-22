# pip install pyodbc
import pyodbc
import re

quer = input("\n\n\t||============================================||"
      "\n\t||  ЩОБ ОТРИМАТИ ІНФО ПРО ПРИСТРІЙ            ||"
      "\n\t||  ВВЕДІТЬ НОМЕР ТЕЛЕФОНУ, ІР АДРЕСУ,        ||"
      "\n\t||  МАС АДРЕСУ АБО ІНВЕНТРАНИЙ НОМЕР          ||"
      "\n\t||============================================||"
      "\n")
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
      connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
      cursor = connect.cursor()
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [MacAddress] = '{ma}'".format(ma = resultmac))
      cursor.execute(query)
      result = cursor.fetchall()
      connect.close()
      inforesult = result[0]
      infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
      print("\n\n\t||============================================||"
            "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - " + str(infores[2]).strip("'") + " "
            "\n\t||  МАС-АДРЕСА - " + str(infores[0]).strip("'") + " "
            "\n\t||  ІНВЕНТАРНИЙ НОМЕР - " + str(infores[4]).strip("'") + " "
            "\n\t||  IP-АДРЕСА - " + str(infores[1]).strip("'") + " "
            "\n\t||  ПРИСВОЄНИЙ НОМЕР - " + str(infores[3]).strip("'") + " "
            "\n\t||  ЛОКАЦІЯ - " + str(infores[5]).strip("'") + " "
            "\n\t||============================================||"
            "\n")


elif ((resm == None) and (resinv != None)):
      resultinv = str(resinv[0])
      connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
      cursor = connect.cursor()
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [InvNumber] = '{invn}'".format(invn = resultinv))
      cursor.execute(query)
      result = cursor.fetchall()
      connect.close()
      inforesult = result[0]
      infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
      print("\n\n\t||============================================||"
            "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - " + str(infores[2]).strip("'") + " "
            "\n\t||  МАС-АДРЕСА - " + str(infores[0]).strip("'") + " "
            "\n\t||  ІНВЕНТАРНИЙ НОМЕР - " + str(infores[4]).strip("'") + " "
            "\n\t||  IP-АДРЕСА - " + str(infores[1]).strip("'") + " "
            "\n\t||  ПРИСВОЄНИЙ НОМЕР - " + str(infores[3]).strip("'") + " "
            "\n\t||  ЛОКАЦІЯ - " + str(infores[5]).strip("'") + " "
            "\n\t||============================================||"
            "\n")



elif ((resm == None) and (resinv == None) and (resn != None)):
      resultnum = str(resn[0])
      connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
      cursor = connect.cursor()
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [PhoneNumber] = '{phn}'".format(phn = resultnum))
      cursor.execute(query)
      result = cursor.fetchall()
      connect.close()
# answer===============================================================================================================
      inforesult = result[0]
      infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
      print("\n\n\t||============================================||"
      "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - " + str(infores[2]).strip("'") + " "
      "\n\t||  МАС-АДРЕСА - " + str(infores[0]).strip("'") + " "
      "\n\t||  ІНВЕНТАРНИЙ НОМЕР - " + str(infores[4]).strip("'") + " "
      "\n\t||  IP-АДРЕСА - " + str(infores[1]).strip("'") + " "
      "\n\t||  ПРИСВОЄНИЙ НОМЕР - " + str(infores[3]).strip("'") + " "
      "\n\t||  ЛОКАЦІЯ - " + str(infores[5]).strip("'") + " "
      "\n\t||============================================||"
      "\n")


else:
      resultip = str(resip[0])
      connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
      cursor = connect.cursor()
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{ipa}'".format(ipa = resultip))
      cursor.execute(query)
      result = cursor.fetchall()
      connect.close()
      inforesult = result[0]
      infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
      print("\n\n\t||============================================||"
            "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - " + str(infores[2]).strip("'") + " "
            "\n\t||  МАС-АДРЕСА - " + str(infores[0]).strip("'") + " "
            "\n\t||  ІНВЕНТАРНИЙ НОМЕР - " + str(infores[4]).strip("'") + " "
            "\n\t||  IP-АДРЕСА - " + str(infores[1]).strip("'") + " "
            "\n\t||  ПРИСВОЄНИЙ НОМЕР - " + str(infores[3]).strip("'") + " "
            "\n\t||  ЛОКАЦІЯ - " + str(infores[5]).strip("'") + " "
            "\n\t||============================================||"
            "\n")