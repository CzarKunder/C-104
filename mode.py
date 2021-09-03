import csv
from collections import Counter
with open("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))
data=Counter(newdata)
modedataforrange={
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,
}
for weight,occurence in data.items():
    if 110<float(weight)<120:
        modedataforrange["110-120"]+=occurence
    elif 120<float(weight)<130:
        modedataforrange["120-130"]+=occurence
    elif 130<float(weight)<140:
        modedataforrange["130-140"]+=occurence
    elif 140<float(weight)<150:
        modedataforrange["140-150"]+=occurence
moderange,modeoccurence=0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((moderange[0]+moderange[1])/2),

print(mode)