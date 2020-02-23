import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
from askfile import akf

image = akf()
if image==None:
    quit()

img = Image.open(image)

#img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

#img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

#img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

img = img.convert('L')#灰度化


barcodes = pyzbar.decode(img)

for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")


from os import startfile, remove
from time import sleep
with open(".$scanQR_Temp.htm", "w") as f:
    f.write('<script>location.replace("'+barcodeData+'")</script>')
startfile(".$scanQR_Temp.htm")
sleep(5)
remove(".$scanQR_Temp.htm")
