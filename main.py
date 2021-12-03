import subprocess

print("\n"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (1) ДОДАТИ IР-ТЕЛЕФОН ДО СИСТЕМИ          ||"
      "\n\t||                                            ||"
      "\n\t||   (додавання нового пристрою в БД, DHCP    ||"
      "\n\t||    та TFTP Asterisk)                       ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (2) ДОДАТИ / ЗМIНИТИ SIP НОМЕР В ТЕЛЕФОНI ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (3) КОНТРОЛЬ ОНЛАЙН                       ||"
      "\n\t||                                            ||"
      "\n\t||    (монiторинг актуального стану пристроїв ||"
      "\n\t||     з можливiстю актуалiзацiї систем)      ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (4) IНФО ПРО ПРИСТРIЙ                     ||"
      "\n\t||                                            ||"
      "\n\t||   (отримання основної iнфо про пристрiй    ||"
      "\n\t||   по SIP номеру, МАС, IР або IНВ.№)        ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (5) HARD АКТУАЛIЗАЦIЯ                     ||"
      "\n\t||                                            ||"
      "\n\t||   (очищення, а потiм наповнення актуальною ||"
      "\n\t||    iнформацiєю БД)                         ||"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (6) ВИЙТИ IЗ ПРОГРАМИ                     ||"
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