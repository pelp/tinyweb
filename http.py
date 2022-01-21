(R:=b"\r\n",s:=lambda x,y=None:x.split(y),i:=[__import__(x)for x in s("socket "
"os _thread")],u:=i[0].socket(),u.bind(("",80)),u.listen(5),h:=lambda c:(d:=(l:=(lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048),a))[R*2 in d][1](a,b)))
)(l,b"")[0],u:=s(s(s(s(d,R*2)[0],R)[0])[1],b"?")[0][1:],d:=(f:=open(("i.htm",u)
[i[1].path.isfile(u)],"rb")).read(),f.close(),c.send(b"HTTP/2 200"+R+b"Content"
b"-Length:"+str(len(d)).encode()+R*2+d),c.close()),(k:=(lambda a:(i[2].start_new_thread(h,(u.accept()[0],)),a(a))))(k))