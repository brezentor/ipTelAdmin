import iptelmethods
import pyodbc
import json
from urllib import request


addlog = "C:\\scripts\\ipTelAdmin\\logdir\\add.log"
ar = open(addlog, mode="r")
data = json.load(ar)

ipinf = "C:\\scripts\\ipTelAdmin\\logdir\\free.log"
iw = open(ipinf, mode = "r")
ipinfo = iw.readline()

oldip = "C:\\scripts\\ipTelAdmin\\logdir\\oldip.log"
oi = open(oldip, mode = "r")
oip = oi.readline().rstrip("\n")
url = "http://{ipadd}/admin/reboot".format(ipadd = oip)
request.urlopen(url)

macn = data[0]['MacAddress']
model = data[0]['PhoneModel']
invn = data[0]['InvNumber']
num = "Nul"
loc = "HO"

conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
cursor = conn.cursor()
query = ("""
            INSERT INTO [dbo].[IpTelephony] ([MacAddress], [IpAddress], [PhoneName], [InvNumber], [PhoneNumber], [Location]) 
            VALUES ('{m}', '{i}', '{mod}', '{inv}', '{n}', '{l}')
            """).format(m = str(macn), i = str(ipinfo), mod = str(model), inv = str(invn), n = str(num), l = str(loc))
cursor.execute(query)
conn.commit()
conn.close()

print("\n"
      "\n\t||============================================||"
      "\n\t||  В СИСТЕМУ ЗАВЕДЕНО ПРИСТРIЙ {modell} "
      "\n\t||  ЙОГО ДАНI:"
      "\n\t||  ФIЗИЧНА АДРЕСА {macad}            "
      "\n\t||  IНВЕНТАРНИЙ НОМЕР - {inv}           "
      "\n\t||  IP-АДРЕСА - {ipad}         "
      "\n\t||  ЛОКАЦIЯ - ГОЛОВНИЙ ОФIС"
      "\n\t||============================================||".format(modell = model, macad = macn, inv = invn, ipad = ipinfo))

iw.close()
ar.close()
oi.close()

iptelmethods.endofpage()