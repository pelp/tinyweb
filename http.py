(R:=b"\r\n",s:=lambda a,b=None:a.split(b),i:=[__import__(a)for a in s("socket "
"os _thread subprocess")],u:=i[0].socket(),u.bind(("",80)),u.listen(10),h:=lambda c:(d:=(l
:=(lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048),a))[R*2 in d][1](a,b))))
(l,b"")[0],u:=s(s(s(s(d,R*2)[0],R)[0])[1],b"?")[0][1:],d:=(lambda x: ((f:=open(
("i.htm",u)[i[1].path.isfile(x)],"r",encoding="utf-8")).read(),f.close())[0], lambda x:
i[3].run(["python",x],stdout=i[3].PIPE).stdout.decode())[s(u,b".")[-1]==b"py"](
u),c.send(("HTTP/2 200\r\nContent-Type:text/html\r\nContent-Length:"+str(len(d))+"\r\n\r\n"+d).encode()),
c.close()),(k:=(lambda a:(i[2].start_new_thread(h,(u.accept()[0],)),a(a))))(k))