#==============================\Making a temp.tmp\======================================

$name = "iptel.tmp"
$path = "C:\scripts\ipTelAdmin\logdir\" + $name
if (Test-Path -Path $path)
{
continue
}
else
{
New-Item -Type "file" -Path "C:\scripts\ipTelAdmin\logdir\" -Name "iptel.tmp"
}

echo "`n
`n`t||============================================||
`n`t||      ЗАРАЗ ВИ БУДЕТЕ ЗАВОДИТИ НОВИЙ        ||
`n`t||       IP-ТЕЛЕФОН ДО СИСТЕМ ДОМЕНУ:         ||
`n`t||============================================||
"

$free = Get-DhcpServerv4FreeIPAddress -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -StartAddress 10.30.0.70 -EndAddress 10.30.0.190 | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String
$fre = "free.log"
$fpath = "C:\scripts\ipTelAdmin\logdir\"
$freepath = $fpath + $fre
Set-Content -Path $freepath -Value $free -Force
echo '`n==========================================================================================='
echo '`n`t'
$inv = Read-Host 'Введіть інвентарний номер пристрою: '
echo '`n==========================================================================================='
echo "`n
`n`t||============================================||
`n`t||      ДІЗНАЙТЕСЬ МАС-АДРЕСУ ПРИСТРОЮ        ||
`n`t||       (НАТИСНІТЬ КНОПКУ НАЛАШТУВАНЬ =>     ||
`n`t||       10. СВЕДЕНИЯ О ПРОДУКТЕ =>           ||
`n`t||       5. МАС-АДРЕС)                        ||
`n`t||============================================||
"
echo '`n==========================================================================================='
echo '`n`t'
do {$mac = Read-Host 'Введіть MAC-адресу пристрою (тільки 12 символів): '} 
while (($mac.length -gt 12) -or ($mac.length -lt 12)) 
Set-Content -Path 'C:\scripts\ipTelAdmin\logdir\iptel.tmp' -Value $mac
$content = [System.IO.File]::ReadAllText("C:\scripts\ipTelAdmin\logdir\iptel.tmp")
$content = $content.Trim()
[System.IO.File]::WriteAllText("C:\scripts\ipTelAdmin\logdir\iptel.tmp", $content)
#==================================\Updating MAC.xml on Asterisk server\============================================
echo '`n==========================================================================================='
echo '`n`t'
$model = Read-Host 'Виберіть модель пристрою: 
1) Cisco SPA502g 
2) Linksys SPA962 
3) Linksys SPA922 
4) Linksys SPA8000
Введіть номер вибору: '

if ($model -eq 4)
{
python C:\scripts\ipTelAdmin\sysdir\1add\spa8000.py
$model = 'SPA8000'
} 
elseif ($model -eq 2)
{
python C:\scripts\ipTelAdmin\sysdir\1add\spa962.py
$model = 'SPA-962'
} 
elseif ($model -eq 3)
{
python C:\scripts\ipTelAdmin\sysdir\1add\spa922.py
$model = 'SPA-922'
} 
elseif ($model -eq 1)
{
python C:\scripts\ipTelAdmin\sysdir\1add\spa502g.py
$model = 'SPA502g'
} 

#===========================\Resarvating of IP and MAC\=======================================


$m = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\iptel.tmp" 

$mactel = Get-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m 

$mactel | Add-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -IPAddress $free

#Remove-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m





echo '`n==========================================================================================='
echo "`n
`n`t||============================================||
`n`t||      ІР-ТЕЛЕФОН БУВ ЗАРЕЄСТРОВАНИЙ В       ||
`n`t||      СИСТЕМІ З ТАКИМИ ДАНИМИ:              ||
`n`t||      ІНВЕНТАРНИЙ НОМЕР - "$inv"    ||
`n`t||      МОДЕЛЬ - "$model"              ||
`n`t||      ІР-АДРЕСА - "$free"               ||
`n`t||      МАС-АДРЕСА - "$m"             ||
`n`t||============================================||
"
echo '`n==========================================================================================='
echo '`n`t'

#==============================\deleting a temp.tmp\======================================

Remove-Item -Name "C:\scripts\ipTelAdmin\logdir\iptel.tmp"

#==========================================================================================================
do {$ex = Read-Host "Натисніть 1, щоб вийти з програми або 2, щоб повернутись до головного меню.."}
while (($ex -lt 1) -or ($ex -gt 2))
switch ($ex){
1 {exit}
2 {С:\scripts\git\ipTelAdmin\main.ps1}
}
