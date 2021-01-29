#$Hello="Hello, Powershell!"
#write-HOat($Hello)
function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}
write-host(getIP)
$IP=getIP
write-Host("This machine IP is $IP")
write-Host("This machine's IP is {0}" -f $IP)