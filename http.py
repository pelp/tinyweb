(s:=lambda a,b=" ":a.split(b),(u:=(i:=[__import__(a)for a in s("socket os _thr"
"ead")])[0].socket()).bind(("",80)),u.listen(),R:="\r\n",r:=R*2,(k:=(lambda a:(
i[2].start_new_thread(lambda c:(d:=c.recv(9999).decode(),y:=s(s(d)[1],"?"),u:=y
[0][1:],d:=(lambda:(f:=open(("idx.htm",u)[i[1].path.isfile(u)])).read(),lambda:
i[1].popen("python "+i[1].getcwd()+" ".join(y)).read())[s(u,".")[-1]=="py"](),c
.send(("HTTP/2 200\r\nServer:tw\r\nContent-Type:text/html;charset=utf-8\r\nCon"
f"tent-Length:{len(d)}"+r+d).encode()),c.close()),(u.accept()[0],)),a(a))))(k))
