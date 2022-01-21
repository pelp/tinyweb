import socket as u, os, threading as t
R,s,_=("\r\n",lambda x,y=None:x.split(y),(u:=u.socket(),u.bind(("",3000)),u.listen(5)))
h=lambda c:(d:=(l:=(lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048).decode(),
a))[R*2 in d][1](a,b))))(l,"")[0],url:=s(s(s(s(d,R*2)[0],R)[0])[1],"?")[0][1:],
d:=(f:=open(("index.html",url)[os.path.isfile(url)],"rb")).read(),f.close(),
c.send((f"HTTP/1.1 200 OK{R}Content-Length: {len(d)}{R*2}").encode()+d),
c.close())
(k:=(lambda a:(t.Thread(target=h,args=(u.accept()[0],)).start(),a(a))))(k)