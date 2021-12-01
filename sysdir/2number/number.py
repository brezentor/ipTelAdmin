import iptelmethods
import pyodbc
import re
import subprocess

print("\n\n\t||============================================||"
      "\n\t|| ЩОБ ВСТАНОВИТИ НОМЕР ТЕЛЕФОНУ НА ПРИСТРIЙ  ||"
      "\n\t|| ВВЕДIТЬ ЙОГО IР, МАС АБО ІНВЕНТАРНИЙ НОМЕР ||"
      "\n\t||============================================||"
      "\n")
asknum = input("Введiть данi та натиснiть ENTER..")
macq = r'[\d\w]{12}'
ipq = r'\d{2}.\d{2}.\d{1}.\d{1,3}'
invq = r'[\w-]{5,8}'

# 1================================
resm = re.match(macq, str(asknum))
# 2================================
resip = re.match(ipq, str(asknum))
# 3================================
resinv = re.match(invq, str(asknum))

print(resm)
print(resip)
print(resinv)


# умова + sql-query==================================
"""if (resm != None):
      resultmac = str(resm[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [MacAddress] = '{ma}'".format(ma=resultmac))
      iptelmethods.sqlconn(query)
elif ((resm == None) and (resinv != None)):
      resultinv = str(resinv[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [InvNumber] = '{invn}'".format(invn=resultinv))
      iptelmethods.sqlconn(query)
else:
      resultip = str(resip[0])
      query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{ipa}'".format(ipa=resultip))
      iptelmethods.sqlconn(query)"""