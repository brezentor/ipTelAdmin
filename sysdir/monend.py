import subprocess
import iptelmethods

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
         "\n\t||  КIЛ-СТЬ ПРИСТРОЇВ ONLINE: {onl}" \
         "\n\t||  КIЛ-СТЬ ПРИСТРОЇВ OFFLINE: {ofl}" \
         "\n\t||============================================||".format(rez = rsize, onl = tsize, ofl = fsize)
print(result)

iptelmethods.endofpage()