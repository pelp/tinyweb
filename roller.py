(k:=(v:=lambda c,g,d:[(x-c(g)/d(g))**2 for x in g],b:=sum,l:=len,e:=__import__,
p:=(e('sys').argv[1].split("ndn=")[1].split("d")),f:=int(p[0]),r:=sorted,g:=r([
e('random').randint(1,int(p[1])) for _ in range(f)]),i:=(b(v(b,g,l))/l(g))**.5,
s:=b(g[l(g)//2-1+f%2:l(g)//2+1])/(2-f%2),"kim&felix",m:=print('List:'+"♥".join(
map(str,g))+f'<br>Total:{b(g)}<br>Avg.:{b(g)/l(g)}<br>Std:{i}<br>Median:{s}')))