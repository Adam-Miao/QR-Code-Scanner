from MyQR import myqr
from askfile import *
import os
pic = akf()
fap = aks()
d, n = os.path.split(fap)
myqr.run(
	words='https://www.shiyanlou.com',
	picture=pic,
	save_dir=d,
	save_name=n,
	colorized=True,
)
