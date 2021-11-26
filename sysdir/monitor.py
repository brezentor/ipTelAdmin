import subprocess

mon = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\monitor.ps1"])
mon.communicate()