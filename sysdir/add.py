import subprocess
import iptelmethods
import json

addlog = "C:\\scripts\\ipTelAdmin\\logdir\\add.log"
aw = open(addlog, mode="w")
mactmp = "C:\\scripts\\ipTelAdmin\\logdir\\iptel.tmp"
mw = open(mactmp, mode = "w")

print("\n"
      "\n\t||============================================||"
      "\n\t||  ЗАРАЗ ВИ БУДЕТЕ ЗАВОДИТИ НОВИЙ            ||"
      "\n\t||  IP-ТЕЛЕФОН ДО СИСТЕМ ДОМЕНУ               ||"
      "\n\t||============================================||"
      "\n\t||  ДIЗНАЙТЕСЬ МАС-АДРЕСУ ПРИСТРОЮ            ||"
      "\n\t||  (НАТИСНIТЬ КНОПКУ НАЛАШТУВАНЬ =>          ||"
      "\n\t||  10. СВЕДЕНИЯ О ПРОДУКТЕ => 5. МАС-АДРЕС)  ||"
      "\n\t||============================================||")

while True:
      macn = input("Введiть MAC-адресу пристрою (тiльки 12 символiв): ")
      lm = len(macn)
      if (int(lm) == 12):
            break
mw.write(macn)
mw.close()
adlo = []
invn = input("Введiть iнвентарний номер пристрою: ")
print("\n"
      "\n\t||============================================||"
      "\n\t||  ВИБЕРIТЬ МОДЕЛЬ ПРИСТРОЮ:                 ||"
      "\n\t||                                            ||"
      "\n\t||  1) Cisco SPA502g                          ||"
      "\n\t||  2) Linksys SPA962                         ||"
      "\n\t||  3) Linksys SPA922                         ||"
      "\n\t||  4) Linksys SPA8000                        ||"
      "\n\t||============================================||")
while True:
      modn = input("Введiть номер вибору: ")
      if ((int(modn) == 1) or (int(modn) == 2) or (int(modn) == 3) or (int(modn) == 4)):
            break
if (int(modn) == 1):
      model = "SPA502G"
      info = {"MacAddress": macn, "PhoneModel": model, "InvNumber": invn}
      adlo.append(info)
      json.dump(adlo, aw)
      aw.close()
      scr1 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\spa502g.py"])
      scr1.communicate()

elif (int(modn) == 2):
      model = "SPA-962"
      info = {"MacAddress": macn, "PhoneModel": model, "InvNumber": invn}
      adlo.append(info)
      json.dump(adlo, aw)
      aw.close()
      scr2 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\spa962.py"])
      scr2.communicate()

elif (int(modn) == 3):
      model = "SPA-922"
      info = {"MacAddress": macn, "PhoneModel": model, "InvNumber": invn}
      adlo.append(info)
      json.dump(adlo, aw)
      aw.close()
      scr3 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\spa922.py"])
      scr3.communicate()

elif (int(modn) == 4):
      model = "SPA8000"
      info = {"MacAddress": macn, "PhoneModel": model, "InvNumber": invn}
      adlo.append(info)
      json.dump(adlo, aw)
      aw.close()
      scr4 = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\sysdir\\spa8000.py"])
      scr4.communicate()




