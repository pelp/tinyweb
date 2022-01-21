import socket as u, os as o, threading as t
s,_=(lambda x,y=None:x.split(y),(u:=u.socket(),u.bind(("",3000)),u.listen(10)))
h=lambda c,R="\r\n":(d:=(l:=(lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048
).decode(),a))[R*2 in d][1](a,b))))(l,"")[0],u:=s(s(s(s(d,R*2)[0],R)[0])[1],"?"
)[0][1:],d:=(f:=open(("index.html",u)[o.path.isfile(u)],"rb")).read(),f.close()
,c.send((f"HTTP/1.1 200{R}Content-Length:{len(d)}{R*2}").encode()+d),c.close())
(k:=(lambda a:(t.Thread(target=h,args=(u.accept()[0],)).start(),a(a))))(k)