# before using of paramiko - install it - "cmd -> $ pip install paramiko"
import paramiko
import iptelmethods
import subprocess

command_koza = 'touch /tftproot/Cisco/spa502g/{p}; chmod o+wx /tftproot/Cisco/spa502g/{p};' \
               ' printf "<flat-profile>\n <HostName ua=\\"rw\\"></HostName>\n' \
               ' <User_ID_1_ ua=\\"na\\"></User_ID_1_>\n <Password_1_ ua=\\"na\\"></Password_1_>\n' \
               ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n' \
               ' <Auth_ID_1_ ua=\\"na\\"></Auth_ID_1_>\n</flat-profile>\n" > /tftproot/Cisco/spa502g/{p}'

iptelmethods.telconfadd(command_koza)

mon = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\add.ps1"])
mon.communicate()