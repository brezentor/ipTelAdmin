import subprocess
import pyodbc


def endofpage():
    while True:
        endinfo = input("Виберiть номер та натиснiть ENTER:\n1) Вийти iз програми\n2) Повернутись до головного меню..")
        if (int(endinfo) >= 1) and (int(endinfo) <= 2):
            break
    print(endinfo)
    if (endinfo == "1"):
        exit()
    elif (endinfo == "2"):
        gotomain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
        gotomain.communicate()
    else:
        print("else")


def execresult(result):
    try:
        inforesult = result[0]
    except:
        print("\n\n\t||============================================||"
              "\n\t||  НЕ ЗНАЙДЕНО IНФО В БД IЗ ТАКИМИ ДАНИМИ "
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