# pip install pyodbc
import pyodbc
import re
import subprocess
import iptelmethods

print("\n\n\t||============================================||"
      "\n\t||  ЩОБ ОТРИМАТИ IНФО ПРО ПРИСТРIЙ            ||"
      "\n\t||  ВВЕДIТЬ НОМЕР ТЕЛЕФОНУ, IР АДРЕСУ,        ||"
      "\n\t||  МАС АДРЕСУ АБО IНВЕНТРАНИЙ НОМЕР          ||"
      "\n\t||============================================||"
      "\n")
quer = input("Введiть данi для пошуку та натиснiть ENTER..")
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
      iptelmethods.sqlconn(query)
elif ((resm == None) and (resinv != None)):
      resultinv = str(resinv[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [InvNumber] = '{invn}'".format(invn=resultinv))
      iptelmethods.sqlconn(query)
elif ((resm == None) and (resinv == None) and (resn != None)):
      resultnum = str(resn[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [PhoneNumber] = '{phn}'".format(phn=resultnum))
      iptelmethods.sqlconn(query)
else:
      resultip = str(resip[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{ipa}'".format(ipa=resultip))
      iptelmethods.sqlconn(query)

iptelmethods.endofpage()