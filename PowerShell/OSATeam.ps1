Get-ADGroupMember -identity "DLIST-Allegis_IS_OSA_ALL" | 
Get-AdUser -Properties EmployeeID, name | 
Select-Object name, EmployeeID 