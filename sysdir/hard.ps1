$rez = Get-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String

#=3==============\внесение всех резервированных  ip в reserved.log\=========================

$res = "hardres.log"
$path = "C:\scripts\ipTelAdmin\logdir\"
$rp = $path + $res
Set-Content -Path $rp -Value $rez -Force