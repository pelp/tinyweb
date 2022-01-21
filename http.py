import socket
import threading
RN = "\r\n"
RNB = b"\r\n"

def ch(c):
    data = ""
    while RN*2 not in data:
        data += c.recv(2048).decode("utf-8")
    header_data, _ = data.split(RN*2)
    req = header_data.split(RN)[0].split()
    url = req[1].split("?")[0][1:]
    # hd = {h.split(": ")[0].lower(): h.split(": ")[1] for h in header_data.split(RN)[1:]}
    if url in ("", "index"):
        url = "index.html"
    print(url)
    try:
        with open(url, "rb") as f:
            data = f.read()
            c.send((f"HTTP/1.1 200 OK{RN}Content-Length: {len(data)}{RN*2}").encode("utf-8") + data)
    except Exception:
        c.send(b"HTTP/1.1 418 I'm a teapot" + RNB*2)
    c.close()

s = socket.socket()

s.bind(("0.0.0.0", 3000))
s.listen(5)
while True:
    c, _ = s.accept()
    threading.Thread(target=ch, args=(c,)).start()
