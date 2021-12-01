import subprocess
import pyodbc
import paramiko

# for redirecting on a main.py
def endofpage():
    while True:
        endinfo = input("\n||============================================"
                        "\n\nВиберiть номер та натиснiть ENTER:\n1) Вийти iз програми\n2) Повернутись до головного меню..")
        if (int(endinfo) >= 1) and (int(endinfo) <= 2):
            break
    if (endinfo == "1"):
        exit()
    elif (endinfo == "2"):
        gotomain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
        gotomain.communicate()
    else:
        print("else")


# for info.py
def sqlconninfo(query):
    connect = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.0.0.9; PORT=1433; DATABASE=IpTele; UID=sa; PWD=123456;')
    cursor = connect.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connect.close()
    try:
        inforesult = result[0]
    except:
        print("\n\n\t||============================================||"
              "\n\t||  НЕ ЗНАЙДЕНО IНФО В БД IЗ ТАКИМИ ДАНИМИ    ||"
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

# for spq922,962,502g,8000.py
def telconfadd(command_koza):
    host = "10.30.0.6"
    port = 22
    username = "iptel"
    password = "48qtnRXt"
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
    host = "10.30.0.6"
    port = 22
    username = "iptel"
    password = "48qtnRXt"
    command = command_koza
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    """data = stdout.read() + stderr.read()"""
    ssh.close()