import subprocess

print("\n"
             "\n\t||============================================||"
             "\n\t||  (1) ДОДАТИ ІР-ТЕЛЕФОН ДО СИСТЕМИ          ||"
             "\n\t||   (ДЛЯ НОВОГО ПРИСТРОЮ)                    ||"
             "\n\t||============================================||"
             "\n\t||  (2) ДОДАТИ / ЗМІНИТИ / ВИДАЛИТИ           ||"
             "\n\t||   НОМЕР В ТЕЛЕФОНІ                         ||"
             "\n\t||============================================||"
             "\n\t||  (3) ДОДАТИ / ЗМІНИТИ / ВИДАЛИТИ           ||"
             "\n\t||   ПРІЗВИЩЕ / ЛОКАЦІЮ                       ||"
             "\n\t||============================================||"
             "\n\t||  (4) КОНТРОЛЬ ОНЛАЙН                       ||"
             "\n\t||============================================||"
             "\n\t||  (5) ІНФО ПРО ПРИСТРІЙ                     ||"
             "\n\t||   (ПО НОМЕРУ, МАС, ІР, ІНВ.№)              ||"
             "\n\t||============================================||"
             "\n\t||  (6) HARD АКТУАЛІЗАЦІЯ - СКИДАННЯ БД       ||"
             "\n\t||   (АКТУАЛІЗАЦІЯ ОФЛАЙН ПРИСТРОЇВ У РУЧНУ)  ||"
             "\n\t||============================================||")

while True:
    mainq = input("Введiть номер операцiї та натиснiть ENTER..")
    if (int(mainq) >= 1) and (int(mainq) <= 6):
        break
print(mainq)
if (mainq == "1"):
    print("C:\\scripts\\ipTelAdmin\\sysdir\\1add\\add.ps1")
elif (mainq == "2"):
    print("2")
elif (mainq == "3"):
    print("3")
elif (mainq == "4"):
    work4 = subprocess.Popen(["python", "D:\\scripts\\git\\ipTelAdmin\\sysdir\\4monitor\\monitor.py"])
    work4.communicate()
elif (mainq == "5"):
    work5 = subprocess.Popen(["python", "D:\\scripts\\git\\ipTelAdmin\\sysdir\\5info\\info.py"])
    work5.communicate()
elif (mainq == "6"):
    print("6")