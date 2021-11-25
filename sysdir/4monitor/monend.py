import subprocess


"""def sqlpurge():
    for 
"""

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

result = "\n\t||============================================||" \
         "\n\t||  ВСЬОГО ЗАРЕЗЕРВОВАНО ПРИСТРОЇВ: {rez}" \
         "\n\t||  КІЛ-СТЬ ПРИСТРОЇВ ONLINE: {onl}" \
         "\n\t||  КІЛ-СТЬ ПРИСТРОЇВ OFFLINE: {ofl}" \
         "\n\t||============================================||".format(rez = rsize, onl = tsize, ofl = fsize)
print(result)

while True:
      endinfo = input("Виберіть номер та натисніть ENTER:\n1) Вийти з програми\n2) Повернутись до головного меню..")
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