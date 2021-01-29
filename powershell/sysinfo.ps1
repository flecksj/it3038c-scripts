#$Hello="Hello, Powershell!"
#write-HOat($Hello)
#Display Computer Name, Date & Time, IP, and PowerSHell Version
#email self sysinfo
function getIP {
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}
function GetVersion {
(Get-Host) | Select-Oject Version
}
function GetDate {
(Get-Date -Format "dddd MM/dd/yyyy HH:mm K")
}
write-host(getIP)
$Version=GetVersion
$IP=getIP
$Date =GetDate
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. Powershell Version $HOST.Version.Major. Today's date is $Date"

write-host($Body)
 
#Send-MailMessage -To "flecksj@mail.uc.edu" -From "flecksj@mail.uc.edu" -Subject "IT3038C windows SysInfo" -Body $Body -SmtpServer smpt.google.com -port 587 -UseSSL -Credentials (Get-Credential)