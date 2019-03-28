CID=0
CFROM=1
CTO=2
CSPEED=3
CPLANTIME=4
RID=0
RLENGTH=1
RSPEED=2
RCHANNEL=3
RFROM=4
RTO=5
RISDUPLEX=6
XID=0
XUP=1
XRIGHT=2
XDOWN=3
XLEFT=4
global cars
global roads
global crosses
global crossxy
global crossid
cars={}
roads={}
crosses={}
crossxy={}
crossid={}
with open('car.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            cars[j[0]]=j
with open('road.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            roads[j[0]]=j
with open('cross.txt','r') as f:
    for i in f.readlines():
        if i[0]!='#':
            j=eval(i)
            crosses[j[0]]=j