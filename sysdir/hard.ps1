$rez = Get-DhcpServerv4Reservation -ComputerName "name.domain.local" -ScopeId "10.40.0.0" | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String

#=3==============\внесение всех резервированных  ip в reserved.log\=========================

$res = "hardres.log"
$path = "C:\scripts\ipTelAdmin\logdir\"
$rp = $path + $res
Set-Content -Path $rp -Value $rez -Force
