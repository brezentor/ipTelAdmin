# before using of paramiko - install it - "cmd -> $ pip install paramiko"
import paramiko

host = "10.30.0.6"
port = 22
username = "iptel"
password = "48qtnRXt"
u = open('C:\\scripts\\ipTelAdmin\\logdir\\iptel.tmp')
mac = u.readline()
u.close()
maccommand = mac + ".xml"

command_koza = 'touch /tftproot/Cisco/spa502g/{p}; chmod o+wx /tftproot/Cisco/spa502g/{p};' \
               ' printf "<flat-profile>\n <HostName ua=\\"rw\\"></HostName>\n' \
               ' <User_ID_1_ ua=\\"na\\"></User_ID_1_>\n <Password_1_ ua=\\"na\\"></Password_1_>\n' \
               ' <Use_Auth_ID_1_ ua=\\"na\\">No</Use_Auth_ID_1_>\n' \
               ' <Auth_ID_1_ ua=\\"na\\"></Auth_ID_1_>\n</flat-profile>\n" > /tftproot/Cisco/spa502g/{p}'
command = command_koza.format(p = maccommand)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
data = stdout.read() + stderr.read()

ssh.close()
