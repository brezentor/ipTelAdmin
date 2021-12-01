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
error = True
while (error == True):
      quer = input("Введiть данi для пошуку та натиснiть ENTER..")
      numbq = r'\d{3}'
      macq = r'[\d\w]{12}'
      ipq = r'10.30.\d{1}.\d{1,3}'
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
            if (len(quer) == 12):
                  resultmac = str(resm[0])
                  query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [MacAddress] = '{ma}'".format(ma=resultmac))
                  iptelmethods.sqlconninfo(query)
                  error = False
            else:
                  print("Ви невiрно ввели МАС-адресу. Потрiбно 12 символiв, а Ви ввели {maclen}".format(
                        maclen=len(quer)))
                  error = True
      elif ((resm == None) and (resinv != None)):
            if ((len(quer) < 5) or (len(quer) > 8)):
                  print("Ви невiрно ввели iнвентарний номер. Потрiбно не бiльше 8 символiв, а Ви ввели {invlen}".format(
                        invlen=len(quer)))
                  error = True
            else:
                  resultinv = str(resinv[0])
                  query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [InvNumber] = '{invn}'".format(invn=resultinv))
                  iptelmethods.sqlconninfo(query)
                  error = False
      elif ((resm == None) and (resinv == None) and (resn != None)):
            if (len(quer) == 3):
                  resultnum = str(resn[0])
                  query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [PhoneNumber] = '{phn}'".format(phn=resultnum))
                  iptelmethods.sqlconninfo(query)
                  error = False
            else:
                  print("Ви невiрно ввели SIP номер. Потрiбно 3 символи, а Ви ввели {maclen}".format(
                        maclen=len(quer)))
                  error = True
      elif (resip != None):
            resultip = str(resip[0])
            query = ("SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{ipa}'".format(ipa=resultip))
            iptelmethods.sqlconninfo(query)
            error = False
      else:
            print("Ви невiрно ввели ip адресу. Використовуйте ip адреси iз пулу 10.30.0.0")
            error = True

iptelmethods.endofpage()