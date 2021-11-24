#=1======================\Чистим старые логи\====================================

$dl1 = Test-Path -Path "C:\scripts\ipTelAdmin\logdir\reserved.log"
$dl2 = Test-Path -Path "C:\scripts\ipTelAdmin\logdir\trueresults.log"
$dl3 = Test-Path -Path "C:\scripts\ipTelAdmin\logdir\falseresults.log"
$dl4 = Test-Path -Path "C:\scripts\ipTelAdmin\logdir\result.log"
if ($dl1 -or $dl2 -or $dl3 -or $dl4)
{
Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\reserved.log"
Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\trueresults.log"
Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\falseresults.log"
Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\result.log"
}
else
{
echo "no logs"
}

#=2========================\узнаем зарезервированные ip\===========================================

$iplist = Get-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String

#=3==============\внесение всех резервированных  ip в reserved.log\=========================

$res = "reserved.log"
$path = "C:\scripts\ipTelAdmin\logdir\"
$rp = $path + $res
Set-Content -Path $rp -Value $iplist -Force

#=5=================\удаление пустых строк\============================

$bl = Get-Content -Path $rp
$bl | Where-Object { $_ } | Set-Content -Path $rp


#=6=======================\цикл с проверкой доступности ip\======================

python "C:\scripts\ipTelAdmin\sysdir\4monitor\iptest.py"

#=7=====================\ сохранение логов \====================================

$logdir = Test-Path -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs"
$nameformat = Get-Date -Format "dd_MM_yyyy_HH_mm"
$infot = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\trueresults.log"
$infof = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\falseresults.log"
$infor = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\result.log"
if ($logdir)
{
New-Item -type "file" -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log"
Add-Content -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log" -Value $infor
Add-Content -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log" -Value $infof
}
else
{
New-Item -ItemType "directory" -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs"
New-Item -type "file" -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log"
Add-Content -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log" -Value $infor
Add-Content -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log" -Value $infof
}
$result = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\MonitorLogs\$nameformat.log"
echo $result

#=8=======================\конец\======================

python "C:\scripts\ipTelAdmin\sysdir\4monitor\monend.py"