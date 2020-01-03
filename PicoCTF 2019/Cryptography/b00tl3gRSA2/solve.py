#!/usr/bin/env python2
from RSAwienerHacker import hack_RSA
from Crypto.Util.number import long_to_bytes
c = 91774478993672356443599858412675641160586343328648517377028932958617801966066212617852940952922122813505029126215954757250238638575597547832698755690986985511719808690043002616747983328364740648622518625791599433009907561134468592981800268594977397405662648818458308932243977137156293104566092487038026616045
n = 110992716825511403212607262072272781395587456263461020275691928389282296148273534564412232551406667155894398405399616822703522000712819532122048494282129970857652976404459835569514431239224762365117171931596638660144415194929848567853650024213590190521756336158147654227253058970624308389287049537936098594257
e = 99530509103536622906170807097142058529338834813118401827702503006084063389198275063184803924708461206414054654423151518279190143886532662210364648373689595277404758167178962945496393189750247083834842354933491163418505353197966478289837416799015572846284694098100833577026677177144394708633973834317557140993
d = hack_RSA(e,n)
print(long_to_bytes(pow(c,d,n)))