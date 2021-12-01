
$free = Get-DhcpServerv4FreeIPAddress -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -StartAddress 10.30.0.70 -EndAddress 10.30.0.190
$fre = "free.log"
$oi = "oldip.log"
$fpath = "C:\scripts\ipTelAdmin\logdir\"
$freepath = $fpath + $fre
$oldippath = $fpath + $oi
Set-Content -Path $freepath -Value $free -Force

$m = Get-Content -Path "C:\scripts\ipTelAdmin\logdir\iptel.tmp" 

$mactel = Get-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m

$oldip = Get-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m | sort IpAddress | Format-Table -Property IpAddress -auto -HideTableHeaders | Out-String
Set-Content -Path $oldippath -Value $oldip -Force
$oldip = [System.IO.File]::ReadAllText("C:\scripts\ipTelAdmin\logdir\oldip.log")
$oldip = $oldip.Trim()
[System.IO.File]::WriteAllText("C:\scripts\ipTelAdmin\logdir\oldip.log", $oldip)

Remove-DhcpServerv4Lease -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -ClientId $m

Add-DhcpServerv4Reservation -ComputerName "ad1.krayina.local" -ScopeId "10.30.0.0" -IPAddress $free -ClientId $m



Remove-Item -Path "C:\scripts\ipTelAdmin\logdir\iptel.tmp"

#=8=======================\конец\======================

python "C:\scripts\ipTelAdmin\sysdir\addend.py"