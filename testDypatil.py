from dypatil_fetch import getData_forbs, param

units = ["mg/Nm2", "Kg/Hr", "mg/Nm2", "mg/L", "mg/L", "mg/L", " ", "M3/Hr"]
paramNum = [0,1,3,4,5,6,7,8]
par = ["PM","Mass Flow","PM","COD","BOD","TSS", "PH","flow"]
line = ["PM : --","Mass Flow: --","PM:--","COD: --","BOD: --","TSS: --", "PH: --","flow: --"]
print(param)
data = getData_forbs()
for i in range(len(paramNum)):
    s = par[i] + ' ' + data[param[paramNum[i]]]+ ' '+ units[i]
    line[i] = s
    print(s)
line1 = ",".join(line[0:4])
line2 = ",".join(line[4:])
print(line)
print(line1)
print(line2)
