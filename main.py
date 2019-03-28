CAR_FROM=1
CAR_TO=2
CAR_SPEED=3
CAR_PLANTIME=4
car={}
road={}
cross={}
crossxy={}
crosxy={}
with open('car.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            car[j[0]]=j[1:]
with open('road.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            road[j[0]]=j[1:]
with open('cross.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            cross[j[0]]=j
for i,j in cross.items():
    print (road,i)
    if not crossxy:
        crossxy[(0,0)]=j
        crosxy[j[0]]=[(0,0),j[1:]]
    elif j[0] in road and road[j[0]][5]==i and road[j[0]][4] in crosxy:
        a=(crossxy[road[j[0]][4]][0][0],crossxy[road[j[0]][4]][0][1]+road[j[0]][1])
        crossxy[a]=j
        crosxy[j[0]]=[a,j[1:]]
    elif j[1] in road and road[j[1]][5]==i and road[j[1]][4] in crosxy:
        a=(crossxy[road[j[1]][4]][0][0]+road[j[1]][1],crossxy[road[j[1]][4]][0][1])
        crossxy[a]=j
        crosxy[j[0]]=[a,j[1:]]
    elif j[2] in road and road[j[2]][5]==i and road[j[2]][4] in crosxy:
        a=(crossxy[road[j[2]][4]][0][0],crossxy[road[j[2]][4]][0][1]-road[j[2]][1])
        crossxy[a]=j
        crosxy[j[0]]=[a,j[1:]]
    elif j[3] in road and road[j[3]][5]==i and road[j[3]][4] in crosxy:
        a=(crossxy[road[j[3]][4]][0][0]-road[j[3]][1],crossxy[road[j[3]][4]][0][1])
        crossxy[a]=j
        crosxy[j[0]]=[a,j[1:]]
print (crossxy)
