import socket as u, threading as t
RN = "\r\n"
RNB = b"\r\n"
s=lambda x,y=None:x.split(y)
def ch(c):
 data = ""
 while RN*2 not in data:
  data += c.recv(2048).decode("utf-8")
 url = s(s(s(s(data,RN*2)[0],RN)[0])[1],"?")[0][1:]
 url = (url, "index.html")[url in ("", "index")]
 try:
  with open(url, "rb") as f:
   data = f.read()
   c.send((f"HTTP/1.1 200 OK{RN}Content-Length: {len(data)}{RN*2}").encode("utf-8") + data)
 except Exception:
  c.send(b"HTTP/1.1 418 I'm a teapot" + RNB*2)
 c.close()
u = u.socket()
u.bind(("0.0.0.0", 3000))
u.listen(5)
while True:
 c, _ = u.accept()
 t.Thread(target=ch, args=(c,)).start()
 #certifiedwomenfriendlyprograming #Loverofwomen #Bringbackväsensmetafysiken #Bringbackwindowsvista #MulleMeck=Slut???