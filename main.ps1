echo "`n
`n`t||============================================||
`n`t||  (1) ДОДАТИ ІР-ТЕЛЕФОН ДО СИСТЕМИ          ||
`n`t||   (ДЛЯ НОВОГО ПРИСТРОЮ)                    ||
`n`t||============================================||
`n`t||  (2) ДОДАТИ / ЗМІНИТИ / ВИДАЛИТИ           ||
`n`t||   НОМЕР В ТЕЛЕФОНІ                         ||
`n`t||============================================||
`n`t||  (3) ДОДАТИ / ЗМІНИТИ / ВИДАЛИТИ           ||
`n`t||   ПРІЗВИЩЕ / ЛОКАЦІЮ                       ||
`n`t||============================================||
`n`t||  (4) КОНТРОЛЬ ОНЛАЙН                       ||
`n`t||============================================||
`n`t||  (5) ІНФО ПРО ПРИСТРІЙ                     ||
`n`t||   (ПО НОМЕРУ, МАС, ІР, ІНВ.№)              ||
`n`t||============================================||
`n`t||  (6) HARD АКТУАЛІЗАЦІЯ - СКИДАННЯ БД       ||
`n`t||   (АКТУАЛІЗАЦІЯ ОФЛАЙН ПРИСТРОЇВ У РУЧНУ)  ||
`n`t||============================================||
"
do {$q = Read-Host "Виберіть номер операції.."}
while (($q -lt 1) -or ($q -gt 6))
switch ($q){
1 {Invoke-Command -Filepath C:\scripts\git\ipTelAdmin\sysdir\1add\add.ps1}
2 {"2"}
3 {"3"}
4 {Invoke-Command -Filepath C:\scripts\git\ipTelAdmin\sysdir\4monitor\monitor.ps1}
5 {Invoke-Command -Filepath C:\scripts\git\ipTelAdmin\sysdir\4monitor\info.ps1}
6 {"6"}
}