import subprocess
import iptelmethods
import paramiko


rip = "C:\\scripts\\ipTelAdmin\\logdir\\reserved.log"
tip = "C:\\scripts\\ipTelAdmin\\logdir\\trueresults.log"
fip = "C:\\scripts\\ipTelAdmin\\logdir\\falseresults.log"
rs = open(rip, mode="r")
ts = open(tip, mode="r")
fs = open(fip, mode="r")
rinfo = rs.readlines()
tinfo = ts.readlines()
finfo = fs.readlines()
rsize = len(rinfo)
tsize = len(tinfo)
fsize = len(finfo)
rs.close()
ts.close()
fs.close()

print("\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  ВСЬОГО ЗАРЕЗЕРВОВАНО ПРИСТРОЇВ: {rez}"
      "\n\t||--------------------------------------------||"
      "\n\t||  КIЛ-СТЬ ПРИСТРОЇВ ONLINE: {onl}"
      "\n\t||--------------------------------------------||"
      "\n\t||  КIЛ-СТЬ ПРИСТРОЇВ OFFLINE: {ofl}"
      "\n\t||                                            ||"
      "\n\t||============================================||"
      "\n\t||==============| ДОДАТКОВI ДIЇ |=============||"
      "\n\t||============================================||"
      "\n\t||                                            ||"
      "\n\t||  (1) ПОКАЗАТИ ПРИСТРОЇ OFFLINE             ||"
      "\n\t||--------------------------------------------||"
      "\n\t||  (2) АКТУАЛIЗУВАТИ СИСТЕМИ                 ||"
      "\n\t||  (видалення offline пристроїв iз систем)   ||"
      "\n\t||--------------------------------------------||"
      "\n\t||  (3) ПОВЕРНУТИСЬ ДО ГОЛОВНОГО МЕНЮ         ||"
      "\n\t||--------------------------------------------||"
      "\n\t||  (4) ВИЙТИ IЗ ПРОГРАМИ                     ||"
      "\n\t||                                            ||"
      "\n\t||============================================||".format(rez = rsize, onl = tsize, ofl = fsize))


while True:
    q = input("\n||====================================================||"
                  "\n\nВведiть номер операцiї та натиснiть ENTER..")
    if (int(q) >= 1) and (int(q) <= 4):
        break
if (q == "1"):
    ans = iptelmethods.action(fsize, finfo)
    ans.showfalse()
elif (q == "2"):
    ans = iptelmethods.action(fsize, finfo)
    ans.actualize()
    print("\n\n\t||============================================||"
          "\n\t||                                            ||"
          "\n\t||        OFFLINE ПРИСТРОЇ ВИДАЛЕНI           ||"
          "\n\t||                                            ||"
          "\n\t||==============| ПОДАЛЬШI ДIЇ |=============||"
          "\n\t||============================================||"
          "\n\t||                                            ||"
          "\n\t||  (1) ПОВЕРНУТИСЬ В ГОЛОВНЕ МЕНЮ            ||"
          "\n\t||--------------------------------------------||"
          "\n\t||  (2) ВИЙТИ IЗ ПРОГРАМИ                     ||"
          "\n\t||                                            ||"
          "\n\t||============================================||")
    iptelmethods.endofpage()
elif (q == "3"):
    gotomain = subprocess.Popen(["python", "C:\\scripts\\ipTelAdmin\\main.py"])
    gotomain.communicate()
elif (q == "4"):
    exit()

