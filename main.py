import subprocess

print("\n"
             "\n\t||============================================||"
             "\n\t||  (1) ДОДАТИ IР-ТЕЛЕФОН ДО СИСТЕМИ          ||"
             "\n\t||   (ДЛЯ НОВОГО ПРИСТРОЮ)                    ||"
             "\n\t||============================================||"
             "\n\t||  (2) ДОДАТИ / ЗМIНИТИ / ВИДАЛИТИ           ||"
             "\n\t||   НОМЕР В ТЕЛЕФОНI                         ||"
             "\n\t||============================================||"
             "\n\t||  (3) ДОДАТИ / ЗМIНИТИ / ВИДАЛИТИ           ||"
             "\n\t||   ПРIЗВИЩЕ / ЛОКАЦIЮ                       ||"
             "\n\t||============================================||"
             "\n\t||  (4) КОНТРОЛЬ ОНЛАЙН                       ||"
             "\n\t||============================================||"
             "\n\t||  (5) IНФО ПРО ПРИСТРIЙ                     ||"
             "\n\t||   (ПО НОМЕРУ, МАС, IР, IНВ.№)              ||"
             "\n\t||============================================||"
             "\n\t||  (6) HARD АКТУАЛIЗАЦIЯ - СКИДАННЯ БД       ||"
             "\n\t||   (АКТУАЛIЗАЦIЯ ОФЛАЙН ПРИСТРОЇВ У РУЧНУ)  ||"
             "\n\t||============================================||")

while True:
    mainq = input("Введiть номер операцiї та натиснiть ENTER..")
    if (int(mainq) >= 1) and (int(mainq) <= 6):
        break
if (mainq == "1"):
    work1 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\add.py"])
    work1.communicate()
elif (mainq == "2"):
    print("2")
elif (mainq == "3"):
    print("3")
elif (mainq == "4"):
    work4 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\monitor.py"])
    work4.communicate()
elif (mainq == "5"):
    work5 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\info.py"])
    work5.communicate()
elif (mainq == "6"):
    print("6")