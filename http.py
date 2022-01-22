(R:=b"\r\n",s:=lambda a,b=None:a.split(b),i:=[__import__(a)for a in s("socket "
"os _thread subprocess")],u:=i[0].socket(),u.bind(("",80)),u.listen(),h:=lambda
c:(d:=(l:=(lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048),a))[R*2 in d][1]
(a,b))))(l,b"")[0],y:=s(s(s(s(d,R*2)[0],R)[0])[1],b"?"),u:=y[0][1:],"felix&kim"
,d:=(lambda x:((f:=open(("i.htm",u)[i[1].path.isfile(x)],"rb")).read(),f.close(
))[0],lambda x:i[3].run(["python",x,b"".join(y[1:])],stdout=i[3].PIPE).stdout)[
s(u,b".")[-1]==b"py"](u),c.send((b"HTTP/2 200\r\nContent-Type:text/html\r\nCon"
b"tent-Length:"+str(len(d)).encode()+b"\r\n\r\n"+d)),c.close()),(k:=(lambda a:(
i[2].start_new_thread(h,(u.accept()[0],)),a(a))))(k))