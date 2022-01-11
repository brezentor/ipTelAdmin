import subprocess
import pyodbc
import paramiko
import os

# for redirecting on a main.py
def endofpage():
    while True:
        endinfo = input("\n||====================================================||"
                        "\n\nВведiть номер та натиснiть ENTER:")
        if (int(endinfo) >= 1) and (int(endinfo) <= 2):
            break
    if (endinfo == "1"):
        gotomain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
        gotomain.communicate()
    elif (endinfo == "2"):
        exit()
    else:
        print("Введіть 1 або 2")

# for info.py
def sqlconninfo(query):
    connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=90.0.0.1; PORT=1433; DATABASE=db; UID=usr; PWD=pwd;')
    cursor = connect.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connect.close()
    try:
        inforesult = result[0]
    except:
        print("\n\n\t||============================================||"
              "\n\t||                                            ||"
              "\n\t||  НЕ ЗНАЙДЕНО IНФО В БД IЗ ТАКИМИ ДАНИМИ    ||"
              "\n\t||                                            ||"
              "\n\t||============================================||"
              "\n")
    else:
        infores = str(inforesult).lstrip("(").rstrip(")").split(", ")
        ad = str(infores[1]).strip("'")
        adp = os.system("ping -n 1 " + ad)
        print(adp)
        if adp == 0:
            cond = "ONLINE"
        else:
            cond = "OFFLINE"
        print(cond)
        print("\n\n\t||============================================||"
              "\n\t||                                            ||"
              "\n\t||  МОДЕЛЬ ТЕЛЕФОНУ - {modtel}"
              "\n\t||  МАС-АДРЕСА - {mactel}"
              "\n\t||  IНВЕНТАРНИЙ НОМЕР - {invtel}"
              "\n\t||  IP-АДРЕСА - {iptel}"
              "\n\t||  ПРИСВОЄНИЙ НОМЕР - {numtel}"
              "\n\t||  ЛОКАЦIЯ - {loctel}"
              "\n\t||  СТАН - {condition}"
              "\n\t||                                            ||"
              "\n\t||============================================||"
              "\n".format(modtel = infores[2].strip("'"), mactel = infores[0].strip("'"),
                          invtel = infores[4].strip("'"), iptel = infores[1].strip("'"),
                          numtel = infores[3].strip("'"), loctel = infores[5].strip("'"),
                          condition = cond))

# for spq922,962,502g,8000.py
def telconfadd(command_koza):
    host = "20.40.0.4"
    port = 22
    username = "usr"
    password = "pwd"
    u = open('C:\\scripts\\ipTelAdmin\\logdir\\iptel.tmp')
    mac = u.readline()
    u.close()
    maccommand = mac + ".xml"
    command = command_koza.format(p=maccommand)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    """data = stdout.read() + stderr.read()"""
    ssh.close()

# for number.py
def telconfedit(command_koza):
    host = "20.40.0.4"
    port = 22
    username = "usr"
    password = "pwd"
    command = command_koza
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    """data = stdout.read() + stderr.read()"""
    ssh.close()

# for monend.py

class action():
    def __init__(self, fsize, finfo):
        self.fsize = fsize
        self.finfo = finfo
    def showfalse(self):
        print("\n||====================================================||"
              "\n\nIP адреси пристроїв offline:\n")
        for i in range(0, int(self.fsize)):
            print(self.finfo[i])
        print("\n\n\t||============================================||"
              "\n\t||==============| ПОДАЛЬШI ДIЇ |=============||"
              "\n\t||============================================||"
              "\n\t||                                            ||"
              "\n\t||           (1) ПОВЕРНУТИСЬ НАЗАД            ||"
              "\n\t||--------------------------------------------||"
              "\n\t||      (2) ПОВЕРНУТИСЬ В ГОЛОВНЕ МЕНЮ        ||"
              "\n\t||--------------------------------------------||"
              "\n\t||           (3) ВИЙТИ IЗ ПРОГРАМИ            ||"
              "\n\t||                                            ||"
              "\n\t||============================================||")
        while True:
            endq = input("\n||====================================================||"
                          "\n\nВведiть номер операцiї та натиснiть ENTER..")
            if (int(endq) >= 1) and (int(endq) <= 3):
                break
        if (endq == "1"):
            back = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\monend.py"])
            back.communicate()
        elif (endq == "2"):
            gotomain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
            gotomain.communicate()
        elif (endq == "3"):
            exit()
    def actualize(self):
        ipdelpath = "C:\\scripts\\ipTelAdmin\\logdir\\dlfls.tmp"
        ip4del = open(ipdelpath, mode = "a")
        connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=90.0.0.1; PORT=1433; DATABASE=db; UID=usr; PWD=pwd;')
        for i in range(0, int(self.fsize)):
            delip = self.finfo[i].rstrip(" ").rstrip("\n")
            if (i == (int(self.fsize)-1)):
                ip4del.write("{iii}".format(iii=delip))
            else:
                ip4del.write("{iii},".format(iii=delip))
            try:
                cursor = connect.cursor()
                query = ("""SELECT * FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{fip}'""".format(fip=delip))
                cursor.execute(query)
                result = cursor.fetchall()
                macraw = str(result[0]).lstrip("(").rstrip(")").split(", ")
                macfin = macraw[0].strip("'").lower()
                modraw = str(result[0]).lstrip("(").rstrip(")").split(", ")
                modfin = modraw[2].strip("'").upper()
            except:
                print("{falip} відсутня в БД".format(falip=delip))
            else:
                host = "10.30.0.6"
                port = 22
                username = "iptel"
                password = "48qtnRXt"
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port, username, password)

                if (modfin == "SPA502G"):
                    commanddel = 'rm -f /tftproot/Cisco/spa502g/{delmac}.xml'.format(delmac=macfin.lower())
                    command = commanddel
                    stdin, stdout, stderr = ssh.exec_command(command)
                    """data = stdout.read() + stderr.read()"""
                    ssh.close()
                elif (modfin == "SPA-922"):
                    commanddel = 'rm -f /tftproot/Linksys/spa922/{delmac}.xml'.format(delmac=macfin.lower())
                    command = commanddel
                    stdin, stdout, stderr = ssh.exec_command(command)
                    """data = stdout.read() + stderr.read()"""
                    ssh.close()
                elif (modfin == "SPA-962"):
                    commanddel = 'rm -f /tftproot/Linksys/spa962/{delmac}.xml'.format(delmac=macfin.lower())
                    command = commanddel
                    stdin, stdout, stderr = ssh.exec_command(command)
                    """data = stdout.read() + stderr.read()"""
                    ssh.close()
            try:
                cursor = connect.cursor()
                querydel = ("""DELETE FROM [dbo].[IpTelephony] WHERE [IpAddress] = '{fip}'""".format(fip=delip))
                cursor.execute(querydel)
                cursor.commit()
            except:
                print("В БД НЕМА IP {fip}".format(fip=delip))

        ip4del.close()
        delres = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\delreserv.ps1"])
        delres.communicate()
        connect.close()
