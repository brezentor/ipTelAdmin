
$free = Get-DhcpServerv4FreeIPAddress -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -StartAddress 10.30.0.70 -EndAddress 10.30.0.190 | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String
$fre = "free.log"
$fpath = "C:\scripts\ipTelAdmin\logdir\"
$freepath = $fpath + $fre
Set-Content -Path $freepath -Value $free -Force

$m = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\iptel.tmp" 

$mactel = Get-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m 

$mactel | Add-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -IPAddress $free

#Remove-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m


Remove-Item -Name "C:\scripts\ipTelAdmin\logdir\iptel.tmp"

#=8=======================\конец\======================

python "C:\scripts\ipTelAdmin\sysdir\addend.py"