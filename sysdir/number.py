from urllib import request
import iptelmethods
import pyodbc
import re
import subprocess
import paramiko

print("\n\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t|| ЩОБ ВСТАНОВИТИ НОМЕР ТЕЛЕФОНУ НА ПРИСТРIЙ  ||"
      "\n\t|| ВВЕДIТЬ ЙОГО IР, МАС АБО IНВЕНТАРНИЙ НОМЕР ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n")
error = True
while (error == True):
      asknum = input("\n||====================================================||"
                     "\n\nВведiть данi та натиснiть ENTER..")
      macq = r'[\d\w]{12}'
      ipq = r'10.30.\d{1,3}.\d{1,3}'
      invq = r'[\w-]{5,8}'

      # 1================================
      resm = re.match(macq, str(asknum))
      # 2================================
      resip = re.match(ipq, str(asknum))
      # 3================================
      resinv = re.match(invq, str(asknum))

      if (resm != None):
            if (len(asknum) == 12):
                  inputinfo = resm[0]
                  error = False
            else:
                  print("\n||====================================================||"
                        "\n\nВи невiрно ввели МАС-адресу. Потрiбно 12 символiв, а Ви ввели {maclen}".format(
                        maclen=len(asknum)))
                  error = True
      elif ((resm == None) and (resinv != None)):
            if ((len(asknum) < 5) or (len(asknum) > 8)):
                  print("\n||====================================================||"
                        "\n\nВи невiрно ввели iнвентарний номер. Потрiбно не бiльше 8 символiв, а Ви ввели {invlen}".format(
                        invlen=len(asknum)))
                  error = True
            else:
                  inputinfo = resinv[0]
                  error = False
      elif (resip != None):
            inputinfo = resip[0]
            print(inputinfo)
            error = False
      else:
            print("\n||====================================================||"
                  "\n\nВи невiрно ввели ip адресу. Використовуйте ip адреси iз пулу 10.30.0.0")
            error = True


# умова + sql-query==================================
query1 = ("SELECT [MacAddress] FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{inin}' OR [InvNumber] = '{inin}' OR "
         "[MacAddress] = '{inin}'".format(inin = str(inputinfo)))
query2 = ("SELECT [PhoneName] FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{inin}' OR [InvNumber] = '{inin}' OR "
         "[MacAddress] = '{inin}'".format(inin = str(inputinfo)))
query3 = ("SELECT [IpAddress] FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{inin}' OR [InvNumber] = '{inin}' OR "
         "[MacAddress] = '{inin}'".format(inin = str(inputinfo)))
connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')

try:
      # query1
      cursor = connect.cursor()
      cursor.execute(query1)
      result1 = cursor.fetchall()
      resmac = str(result1[0]).lstrip("('").rstrip(", )").rstrip("'").lower()
      # query2
      cursor.execute(query2)
      result2 = cursor.fetchall()
      resmod = str(result2[0]).lstrip("('").rstrip(", )").rstrip("'")
      # query3
      cursor.execute(query3)
      result3 = cursor.fetchall()
      resip = str(result3[0]).lstrip("('").rstrip(", )").rstrip("'")
except:
      print("\n\n\t||============================================||"
            "\n\t||                                            ||"
            "\n\t||  НЕ ЗНАЙДЕНО IНФО В БД З ТАКИМИ ДАНИМИ    ||"
            "\n\t||                                            ||"
            "\n\t||============================================||"
            "\n")
      herewegoagain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
      herewegoagain.communicate()

# введення номеру
askerror = True
while (askerror == True):
      asksip = input("\n||====================================================||"
                     "\n\nВведiть 3-значний SIP номер та натиснiть ENTER..")
      try:
            asksip = int(asksip)
      except:
            print("\n||====================================================||"
                  "\n\nВикористовуйте тiльки цифри!")
            askerror = True
      else:
            if (len(str(asksip)) != 3):
                  print("\n||====================================================||"
                        "\n\nВи ввели {er} цифри. Введiть 3-значне число!".format(er=len(str(asksip))))
                  askerror = True
            else:
                  askerror = False
asksip = str(asksip)

# введення номеру в бд
queryend = ("UPDATE [dbo].[IpTelephony] SET [PhoneNumber]='{innum}' WHERE [IpAddress] = '{inin}' OR [InvNumber] = "
            "'{inin}' OR [MacAddress] = '{inin}'".format(innum = str(asksip), inin = str(inputinfo)))
# queryend
cursor.execute(queryend)
resultfin = cursor.commit()
connect.close()
# присвоєння номеру

if (resmod == "SPA502G"):
      command_koza = ' printf "<flat-profile>\n <HostName ua=\\"rw\\"></HostName>\n' \
                     ' <User_ID_1_ ua=\\"na\\">{sip}</User_ID_1_>\n <Password_1_ ua=\\"na\\">{sip}</Password_1_>\n' \
                     ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n <Auth_ID_1_ ua=\\"na\\">' \
                     '</Auth_ID_1_>\n</flat-profile>\n" > /tftproot/Cisco/spa502g/{mac}.xml'.format(sip = asksip, mac = resmac)
      iptelmethods.telconfedit(command_koza)
      url = "http://{ipadd}/admin/reboot".format(ipadd=resip)
      request.urlopen(url)
elif (resmod == "SPA-922"):
      command_koza = ' printf "<flat-profile>\n <HostName ua=\\"rw\\"></HostName>\n' \
               ' <User_ID_1_ ua=\\"na\\">{sip}</User_ID_1_>\n <Password_1_ ua=\\"na\\">{sip}</Password_1_>\n' \
               ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n' \
               ' <Auth_ID_1_ ua=\\"na\\"></Auth_ID_1_>\n</flat-profile>\n" > /tftproot/Linksys/spa922/{mac}.xml'.format(sip=asksip,
                                                                                                    mac=resmac)
      iptelmethods.telconfedit(command_koza)
      url = "http://{ipadd}/admin/reboot".format(ipadd=resip)
      request.urlopen(url)
elif (resmod == "SPA-962"):
      command_koza = ' printf "<flat-profile>\n\n  <HostName ua=\\"rw\\"></HostName>\n  <User_ID_1_ ua=\\"na\\">{sip}</User_ID_1_>\n' \
               '  <Password_1_ ua\\"na\\">{sip}</Password_1_>\n  <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n' \
               '  <Auth_ID_1_ ua=\\"na\\"></Auth_ID_1_>\n\n</flat-profile>\n" > /tftproot/Linksys/spa962/{mac}.xml'.format(
            sip=asksip,
            mac=resmac)
      iptelmethods.telconfedit(command_koza)
      url = "http://{ipadd}/admin/reboot".format(ipadd=resip)
      request.urlopen(url)

print("\n\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  SIP номер вдало додано/змiнено            ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||==============| ПОДАЛЬШI ДIЇ |=============||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (1) ПОВЕРНУТИСЬ В ГОЛОВНЕ МЕНЮ            ||"
      "\n\t||--------------------------------------------||"
      "\n\t||  (2) ВИЙТИ IЗ ПРОГРАМИ                     ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n")

iptelmethods.endofpage()