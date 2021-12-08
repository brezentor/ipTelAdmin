import subprocess

print("\n"
      "\n\t||============================================||"
      "\n\t||                       | Додавання нового   ||"
      "\n\t|| (1) ДОДАТИ IР-ТЕЛЕФОН | пристрою в БД,     ||"
      "\n\t||     ДО СИСТЕМИ        | DHCP та            ||"
      "\n\t||                       | TFTP Asterisk      ||"
      "\n\t||============================================||"
      "\n\t||                       | Реєстрацiя SIP     ||"
      "\n\t|| (2) ДОДАТИ / ЗМIНИТИ  | номеру на пристрої ||"
      "\n\t||      SIP НОМЕР        | в БД та на         ||"
      "\n\t||                       | TFTP Asterisk      ||"
      "\n\t||============================================||"
      "\n\t||                       | Монiторинг         ||"
      "\n\t||                       | актуального        ||"
      "\n\t|| (3) КОНТРОЛЬ ОНЛАЙН   | стану пристроїв    ||"
      "\n\t||                       | з можливiстю       ||"
      "\n\t||                       | актуалiзацiї       ||"
      "\n\t||                       | систем             ||"
      "\n\t||============================================||"
      "\n\t||                       | Отримання основної ||"
      "\n\t|| (4) IНФО ПРО ПРИСТРIЙ | iнфо про пристрiй  ||"
      "\n\t||                       | по SIP номеру,     ||"
      "\n\t||                       | МАС, IР або IНВ.№  ||"
      "\n\t||============================================||"
      "\n\t||                       | Повне очищення     ||"
      "\n\t||                       | та наповнення      ||"
      "\n\t|| (5) HARD АКТУАЛIЗАЦIЯ | актуальною iнфо БД.||"
      "\n\t||                       | !IНВЕНТАРНI НОМЕРА ||"
      "\n\t||                       | ДОВЕДЕТЬСЯ ВНОСИТИ ||"
      "\n\t||                       | В РУЧНУ!           ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||           (6) ВИЙТИ IЗ ПРОГРАМИ            ||"
      "\n\t||                                            ||"
      "\n\t||============================================||")

while True:
    mainq = input("\n||====================================================||"
                  "\n\nВведiть номер операцiї та натиснiть ENTER..")
    if (int(mainq) >= 1) and (int(mainq) <= 6):
        break
if (mainq == "1"):
    work1 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\add.py"])
    work1.communicate()
elif (mainq == "2"):
    work2 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\number.py"])
    work2.communicate()
elif (mainq == "3"):
    work3 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\monitor.py"])
    work3.communicate()
elif (mainq == "4"):
    work4 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\info.py"])
    work4.communicate()
elif (mainq == "5"):
    print("5")
elif (mainq == "6"):
    exit()