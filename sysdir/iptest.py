import os

res = "C:\\scripts\\ipTelAdmin\\logdir\\reserved.log"
ttest = "C:\\scripts\\ipTelAdmin\\logdir\\trueresults.log"
ftest = "C:\\scripts\\ipTelAdmin\\logdir\\falseresults.log"
ipt = open(res, mode="r")
opt = open(ttest, mode="w")
opf = open(ftest, mode="w")
for l in ipt:
  ipadrs = l
  resp = os.system("ping -n 2 " + ipadrs)
  if resp == 0:
    opt.write(l)
  else:
    opf.write(l)

opt.close()
opf.close()
ipt.close()

rdr = open(res, mode="r")
rdf = open(ftest, mode="r")

info = "\nЗарезервовані IP: {rsts}\n\nOffline: " \
       "{fsts}\n\n".format(rsts = rdr.readlines().__len__(), 
                         fsts = rdf.readlines().__len__())

rdr.close()
rdf.close()

result = "C:\\scripts\\ipTelAdmin\\logdir\\result.log"
rslt = open(result, mode="w", encoding="latin-1")
rslt.write(info)
rslt.close()