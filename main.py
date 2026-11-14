import json,os,sys,urllib.request as u
E=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("x")
def P(p,b):
 r=u.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 with u.urlopen(r) as x:return json.load(x)
V=[0,100,320,330,500,900,20000];M=100000;N=40000
S=["KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKK","ACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECA","GIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIG","KKKKKKKKLMMMMMMLJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJKKKLLKKK","GIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIG","ECCAACCEECCAACCEECCAACCEECCAACCEGEECCEEGIGGGGGGIOOKKKKOOOQMKKMQO"]
T=[]
for s in S:
 a=[0]*128
 for r in range(8):
  for f in range(8):a[(7-r)*16+f]=(ord(s[r*8+f])-75)*5
 T.append(a)
Z=[];x=1
for i in range(1600):
 x=(x*6364136223846793005+1442695040888963407)%(1<<64);Z.append(x)
def zi(p,q):return Z[((p-1) if p>0 else (5-p))*128+q]
nd=0;ab=False;TT={};KL=[[0,0] for _ in range(128)];HS=set()
class B:
 def __init__(s):
  s.b=[0]*128;s.t=1;s.c=15;s.e=-1;s.h=0;s.k=[4,116];s.s=[]
 def F(s,f):
  p=f.split();r=7;fl=0
  for ch in p[0]:
   if ch=='/':r-=1;fl=0
   elif ch.isdigit():fl+=int(ch)
   else:
    q=r*16+fl;v="PNBRQK".index(ch.upper())+1
    if ch.islower():v=-v
    s.b[q]=v;s.h^=zi(v,q)
    if abs(v)==6:s.k[0 if v>0 else 1]=q
    fl+=1
  s.t=1 if p[1]=='w' else -1
  if s.t<0:s.h^=Z[1536]
  s.c=0
  for ch in p[2]:
   if ch=='K':s.c|=1
   if ch=='Q':s.c|=2
   if ch=='k':s.c|=4
   if ch=='q':s.c|=8
  s.h^=Z[1537+s.c]
  if p[3]!='-':
   s.e=(8-int(p[3][1]))*16+"abcdefgh".index(p[3][0]);s.h^=Z[1553+(s.e&7)]
 def A(s,q,w):
  b=s.b
  for d in(33,31,18,14,-14,-18,-31,-33):
   o=q+d
   if o&136==0 and b[o]==(2 if w else -2):return 1
  for d in(-16,-1,1,16):
   o=q+d
   while o&136==0:
    v=b[o]
    if v:
     if v==(4 if w else -4) or v==(5 if w else -5):return 1
     break
    o+=d
  for d in(-17,-15,15,17):
   o=q+d
   while o&136==0:
    v=b[o]
    if v:
     if v==(3 if w else -3) or v==(5 if w else -5):return 1
     break
    o+=d
  for d in(-17,-16,-15,-1,1,15,16,17):
   o=q+d
   if o&136==0 and b[o]==(6 if w else -6):return 1
  for d in((-17,-15) if w else (17,15)):
   o=q+d
   if o&136==0 and b[o]==(1 if w else -1):return 1
  return 0
 def C(s):return s.A(s.k[0 if s.t>0 else 1],s.t<0)
 def G(s,cp=False):
  b=s.b;m=[];t=s.t
  for q in range(128):
   if q&136:continue
   p=b[q]
   if p*t<=0:continue
   a=abs(p)
   if a==1:
    d=16*t;to=q+d
    if not(to&136) and not b[to] and not cp:
     if to>>4 in(0,7):
      for pr in(2,3,4,5):m.append(q|to<<7|pr<<14)
     else:
      m.append(q|to<<7)
      if q>>4==(1 if t>0 else 6):
       o=q+2*d
       if not b[o]:m.append(q|o<<7|2<<17)
    for f in(-1,1):
     to=q+d+f
     if to&136:continue
     v=b[to]
     if v*t<0:
      if to>>4 in(0,7):
       for pr in(2,3,4,5):m.append(q|to<<7|pr<<14|1<<20)
      else:m.append(q|to<<7|1<<20)
     elif to==s.e:m.append(q|to<<7|1<<20|1<<21)
   elif a in(2,6):
    ds=[33,31,18,14,-14,-18,-31,-33] if a==2 else[-17,-16,-15,-1,1,15,16,17]
    for d in ds:
     to=q+d
     if to&136:continue
     v=b[to]
     if not v and not cp:m.append(q|to<<7)
     elif v*t<0:m.append(q|to<<7|1<<20)
   else:
    ds=[-16,-1,1,16] if a==4 else([-17,-15,15,17] if a==3 else[-17,-16,-15,-1,1,15,16,17])
    for d in ds:
     to=q+d
     while not(to&136):
      v=b[to]
      if not v and not cp:m.append(q|to<<7)
      else:
       if v*t<0:m.append(q|to<<7|1<<20)
       break
      to+=d
  if not cp:
   if t>0:
    if s.c&1 and not b[5] and not b[6] and b[7]==4 and not s.A(4,0) and not s.A(5,0) and not s.A(6,0):m.append(4|6<<7|1<<22)
    if s.c&2 and not b[1] and not b[2] and not b[3] and b[0]==4 and not s.A(4,0) and not s.A(3,0) and not s.A(2,0):m.append(4|2<<7|1<<22)
   else:
    if s.c&4 and not b[117] and not b[118] and b[119]==-4 and not s.A(116,1) and not s.A(117,1) and not s.A(118,1):m.append(116|118<<7|1<<22)
    if s.c&8 and not b[113] and not b[114] and not b[115] and b[112]==-4 and not s.A(116,1) and not s.A(115,1) and not s.A(114,1):m.append(116|114<<7|1<<22)
  return m
 def M(s,m):
  b=s.b;fr=m&127;to=(m>>7)&127;pr=(m>>14)&7
  s.s.append((m,b[to],s.c,s.e,s.h))
  cap=b[to];pc=b[fr]
  if s.e>=0:s.h^=Z[1553+(s.e&7)]
  s.e=-1
  if cap:s.h^=zi(cap,to)
  if m&1<<21:
   o=to-16*s.t;s.h^=zi(b[o],o);b[o]=0
  if m&1<<22:
   if to==6:b[5]=b[7];b[7]=0;s.h^=zi(4,7)^zi(4,5)
   elif to==2:b[3]=b[0];b[0]=0;s.h^=zi(4,0)^zi(4,3)
   elif to==118:b[117]=b[119];b[119]=0;s.h^=zi(-4,119)^zi(-4,117)
   else:b[115]=b[112];b[112]=0;s.h^=zi(-4,112)^zi(-4,115)
  s.h^=zi(pc,fr)
  if pr:
   n=pr*s.t;b[to]=n;s.h^=zi(n,to)
  else:b[to]=pc;s.h^=zi(pc,to)
  b[fr]=0
  if m&2<<17:s.e=fr+16*s.t;s.h^=Z[1553+(s.e&7)]
  s.h^=Z[1537+s.c]
  s.c&={4:12,7:14,0:13,116:3,119:11,112:7}.get(fr,15)
  s.c&={4:12,7:14,0:13,116:3,119:11,112:7}.get(to,15)
  s.h^=Z[1537+s.c]
  if abs(pc)==6:s.k[0 if s.t>0 else 1]=to
  s.h^=Z[1536];s.t=-s.t
 def U(s):
  m,cap,oc,oe,oh=s.s.pop();b=s.b;fr=m&127;to=(m>>7)&127;pr=(m>>14)&7;pc=b[to]
  s.t=-s.t;s.c=oc;s.e=oe;s.h=oh
  b[fr]=pc if not pr else(1 if s.t>0 else -1)
  if m&1<<22:
   if to==6:b[7]=b[5];b[5]=0
   elif to==2:b[0]=b[3];b[3]=0
   elif to==118:b[119]=b[117];b[117]=0
   else:b[112]=b[115];b[115]=0
  elif m&1<<21:b[to-16*s.t]=-s.t
  b[to]=cap
  if abs(b[fr])==6:s.k[0 if s.t>0 else 1]=fr
 def W(s):
  v=0;w=b=0
  for q in range(128):
   if q&136:continue
   p=s.b[q]
   if not p:continue
   a=abs(p)
   if a==3:
    if p>0:w+=1
    else:b+=1
   v+=(V[a]+T[a-1][q if p>0 else q^112])*(1 if p>0 else -1)
  v+=(30 if w>=2 else 0)-(30 if b>=2 else 0)
  return v*s.t
 def NM(s):
  s.s.append((0,0,s.c,s.e,s.h))
  if s.e>=0:s.h^=Z[1553+(s.e&7)]
  s.h^=Z[1536];s.e=-1;s.t=-s.t
 def NU(s):
  _,_,oc,oe,oh=s.s.pop();s.t=-s.t;s.c=oc;s.e=oe;s.h=oh
def O(bd,ms,tt,pl):
 def k(m):
  if m==tt:return 1<<25
  if m&1<<20:
   v=bd.b[(m>>7)&127]
   return V[abs(v)]*16-V[abs(bd.b[m&127])] if v else 0
  if m in KL[pl]:return 1<<20
  return 0
 return sorted(ms,key=k,reverse=True)
def Q(bd,al,be,pl):
 global nd,ab
 nd+=1
 if nd>=N:ab=True;return 0
 if bd.h in HS:return 0
 st=bd.W()
 if st>=be:return be
 if st>al:al=st
 ic=bd.C()
 ms=bd.G(not ic);lg=[]
 for m in ms:
  bd.M(m)
  if not bd.A(bd.k[0 if bd.t<0 else 1],bd.t>0):lg.append(m)
  bd.U()
 if ic and not lg:return -M+pl
 for m in O(bd,lg,0,pl):
  bd.M(m);v=-Q(bd,-be,-al,pl+1);bd.U()
  if v>=be:return be
  if v>al:al=v
 return al
def S(bd,d,al,be,pl):
 global nd,ab
 nd+=1
 if nd>=N:ab=True;return 0
 if bd.h in HS:return 0
 if d<=0:return Q(bd,al,be,pl)
 en=TT.get(bd.h)
 if en and en[0]>=d:
  _,fl,v,mv=en
  if fl==0:return v
  if fl==1 and v>=be:return be
  if fl==2 and v<=al:return al
 ic=bd.C()
 if d>=3 and not ic and be<M-1000:
  bd.NM();v=-S(bd,d-3,-be,-be+1,pl+1);bd.NU()
  if ab:return 0
  if v>=be:return be
 ms=bd.G();lg=[]
 for m in ms:
  bd.M(m)
  if not bd.A(bd.k[0 if bd.t<0 else 1],bd.t>0):lg.append(m)
  bd.U()
 if not lg:return -M+pl if ic else 0
 tt=en[3] if en else 0
 a=al;bs=-2*M;bm=lg[0]
 for i,m in enumerate(O(bd,lg,tt,pl)):
  bd.M(m)
  if i>=3 and d>=3 and not(m&1<<20) and not ic:
   v=-S(bd,d-2,-be,-a,pl+1)
   if not ab and v>a:v=-S(bd,d-1,-be,-a,pl+1)
  else:v=-S(bd,d-1,-be,-a,pl+1)
  bd.U()
  if ab:return 0
  if v>bs:bs=v;bm=m
  if v>a:a=v
  if a>=be:
   if not(m&1<<20):KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 TT[bd.h]=(d,0 if bs<=al else(1 if bs>=be else 2),bs,bm)
 return bs
def BM(bd):
 global nd,TT,KL,ab
 TT={};KL=[[0,0] for _ in range(128)]
 ms=bd.G();lg=[]
 for m in ms:
  bd.M(m)
  if not bd.A(bd.k[0 if bd.t<0 else 1],bd.t>0):lg.append(m)
  bd.U()
 if not lg:return None
 if len(lg)==1:return lg[0]
 best=lg[0];nd=0
 for d in range(1,64):
  ab=False;cb=best;al=-2*M
  for m in O(bd,lg,0,0):
   bd.M(m);v=-S(bd,d-1,-2*M,-al,1);bd.U()
   if ab:break
   if v>al:al=v;cb=m
  if ab:break
  best=cb
 return best
def UC(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 return "abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)+("nbrq"[pr-2] if pr else "")
while True:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  bd=B();bd.F(g["fen"])
  HS=set()
  for mv in g["moves"]:
   HS.add(bd.h);m=None
   for x in bd.G():
    if UC(x)==mv:m=x;break
   if m is None:break
   bd.M(m)
  m=BM(bd)
  g=P("/move",{"game":g["game"],"move":UC(m)})
 print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
