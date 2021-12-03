$delfals = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\dlfls.tmp"

$d = $delfals.Split(",")

foreach ($el in $d) {
  Remove-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -IPAddress $el
}

Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\dlfls.tmp"