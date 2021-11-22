python C:\scripts\ipTelAdmin\sysdir\5info\info.py

#==========================================================================================================
do {$ex = Read-Host "Натисніть 1, щоб вийти з програми або 2, щоб повернутись до головного меню.."}
while (($ex -lt 1) -or ($ex -gt 2))
switch ($ex){
1 {exit}
2 {С:\scripts\git\ipTelAdmin\main.ps1}
}
