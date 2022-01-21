(i:=[__import__(x)for x in["socket","os","threading"]],s:=lambda x,y=" ":x.split(y),
u:=i[0].socket(),u.bind(("",80)),u.listen(5),h:=lambda c,R="\r\n":(d:=(l:=(
lambda a,d:(((d,lambda a,b:(b,)),(b:=d+c.recv(2048).decode(),a))[R*2 in d][1](a
,b))))(l,"")[0],u:=s(s(s(s(d,R*2)[0],R)[0])[1],"?")[0][1:],d:=(f:=open(("index"
".html",u)[i[1].path.isfile(u)],"rb")).read(),f.close(),c.send((f"HTTP/1.1 200"
f"{R}Content-Length:{len(d)}{R*2}").encode()+d),c.close()),(k:=(lambda a:(i[2
].Thread(target=h,args=(u.accept()[0],)).start(),a(a))))(k))