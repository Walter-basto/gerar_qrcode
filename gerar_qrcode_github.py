from pyqrcode import QRCode
import pyqrcode
import png


# link desejado do qrcode
#QRString='http://www.instagram.com/pycodebr/'

QRString='https://github.com/'
#monta o qrcode
url=pyqrcode.create(QRString)
#salva o qrcode gerado no localk desejado
url.png(r'qr.png',scale=8)