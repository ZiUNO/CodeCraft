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
XXY=0
XUP=1
XRIGHT=2
XDOWN=3
XLEFT=4
X=0
Y=1
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
t=True
while t:
    t=False
    for i,j in crosses.items():
        if not j:
            pass
        elif not crossxy:
            crossxy[(0,0)]=j
            crossid[j[XID]]=[(0,0),j[XUP:]]
            crosses[i]=None
            t=True
        elif j[XUP] in roads and roads[j[XUP]][RTO]==i and roads[j[XUP]][RFROM] in crossid:
            a=(crossid[roads[j[XUP]][RFROM]][XXY][X],crossid[roads[j[XUP]][RFROM]][XXY][Y]-roads[j[XUP]][RLENGTH])
            crossxy[a]=j
            crossid[j[XID]]=[a,j[XUP:]]
            crosses[i]=None
            t=True
        elif j[XRIGHT] in roads and roads[j[XRIGHT]][RTO]==i and roads[j[XRIGHT]][RFROM] in crossid:
            a=(crossid[roads[j[XRIGHT]][RFROM]][XXY][X]-roads[j[XRIGHT]][RLENGTH],crossid[roads[j[XRIGHT]][RFROM]][XXY][Y])
            crossxy[a]=j
            crossid[j[XID]]=[a,j[XUP:]]
            crosses[i]=None
            t=True
        elif j[XDOWN] in roads and roads[j[XDOWN]][RTO]==i and roads[j[XDOWN]][RFROM] in crossid:
            a=(crossid[roads[j[XDOWN]][RFROM]][XXY][X],crossid[roads[j[XDOWN]][RFROM]][XXY][Y]+roads[j[XDOWN]][RLENGTH])
            crossxy[a]=j
            crossid[j[XID]]=[a,j[XUP:]]
            crosses[i]=None
            t=True
        elif j[XLEFT] in roads and roads[j[XLEFT]][RTO]==i and roads[j[XLEFT]][RFROM] in crossid:
            a=(crossid[roads[j[XLEFT]][RFROM]][XXY][X]+roads[j[XLEFT]][RLENGTH],crossid[roads[j[XLEFT]][RFROM]][XXY][Y])
            crossxy[a]=j
            crossid[j[XID]]=[a,j[XUP:]]
            crosses[i]=None
            t=True
