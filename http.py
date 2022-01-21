import socket as u
import os
import threading as t
RN = "\r\n"
RNB = b"\r\n"
s=lambda x,y=None:x.split(y)
def non(a, b):
    pass

h=lambda c: (
    l := (
        lambda a,d: (
            (
                (b := d+c.recv(2048).decode("utf-8"), a, print(d)),
                (d, non)
            )[RN*2 not in b][1](a, b)
        )
    ),
    d:=l(l, "")[0],
    print("Done reading"),
    url:=s(s(s(s(d, RN*2)[0], RN)[0])[1], "?")[0][1:],
    exists:=os.path.isfile(url),
    f:=open(("index.html",url)[exists], "rb"),
    d:=f.read(),
    c.send((f"HTTP/1.1 200 OK{RN}Content-Length: {len(d)}{RN*2}").encode("utf-8") + d),
    f.close(),
    c.close()
)


u = u.socket()
u.bind(("0.0.0.0", 3000))
u.listen(5)
while True:
    t.Thread(target=h, args=(u.accept()[0],)).start()
    # certifiedwomenfriendlyprograming #Loverofwomen #Bringbackväsensmetafysiken #Bringbackwindowsvista #MulleMeck=Slut???
