# before using of paramiko - install it - "cmd -> $ pip install paramiko"
import paramiko
import iptelmethods
import subprocess

command_koza = 'touch /tftproot/Linksys/spa8000/{p}; chmod o+wx /tftproot/Linksys/spa8000/{p};' \
               ' printf "<flat-profile>\n <HostName ua=\\"rw\\">SPA8000</HostName>\n' \
               ' <User_ID_1_ ua=\\"na\\"></User_ID_1_>\n <Password_1_ ua=\\"na\\"></Password_1_>\n' \
               ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n <User_ID_2_ ua=\\"na\\"></User_ID_2_>\n' \
               ' <Password_2_ ua=\\"na\\"></Password_2_>\n <Use_Auth_ID_2_ ua=\\"na\\">No</Use_Auth_ID_2_>\n' \
               ' <User_ID_3_ ua=\\"na\\"></User_ID_3_>\n <Password_3_ ua=\\"na\\"></Password_3_>\n' \
               ' <Use_Auth_ID_3_ ua=\\"na\\">No</Use_Auth_ID_3_>\n <User_ID_4_ ua=\\"na\\"></User_ID_4_>\n' \
               ' <Password_4_ ua=\\"na\\"></Password_4_>\n <Use_Auth_ID_4_ ua=\\"na\\">No</Use_Auth_ID_4_>\n' \
               ' <User_ID_5_ ua=\\"na\\"></User_ID_5_>\n <Password_5_ ua=\\"na\\"></Password_5_>\n' \
               ' <Use_Auth_ID_5_ ua=\\"na\\">No</Use_Auth_ID_5_>\n <User_ID_6_ ua=\\"na\\"></User_ID_6_>\n' \
               ' <Password_6_ ua=\\"na\\"></Password_6_>\n <Use_Auth_ID_6_ ua=\\"na\\">No</Use_Auth_ID_6_>\n' \
               ' <User_ID_7_ ua=\\"na\\"></User_ID_7_>\n <Password_7_ ua=\\"na\\"></Password_7_>\n' \
               ' <Use_Auth_ID_7_ ua=\\"na\\">No</Use_Auth_ID_7_>\n <User_ID_8_ ua=\\"na\\"></User_ID_8_>\n' \
               ' <Password_8_ ua=\\"na\\"></Password_8_>\n <Auth_ID_8_ ua=\\"na\\">No</Auth_ID_8_>\n' \
               ' <Use_Auth_ID_8_ ua=\\"na\\">No</Use_Auth_ID_8_>\n</flat-profile>\n" > /tftproot/Linksys/spa8000/{p}'

iptelmethods.telconfadd(command_koza)

mon = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\add.ps1"])
mon.communicate()