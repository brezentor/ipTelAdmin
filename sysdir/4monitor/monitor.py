import os
import subprocess

mon = subprocess.Popen(["powershell", "C:\\scripts\\ipTelAdmin\\sysdir\\4monitor\\monitor.ps1"])
mon.communicate()