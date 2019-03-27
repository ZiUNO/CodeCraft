CAR_FROM=1
CAR_TO=2
CAR_SPEED=3
CAR_PLANTIME=4
car={}
road={}
cross={}
crossxy={}
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
            cross[j[0]]=j[1:]
print (car)
#for i,j in cross[1:]:
#    if j[0] in road and road[j[0]][4]==i and road[j[0]][5] in cross

    
