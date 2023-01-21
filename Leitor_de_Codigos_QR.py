from PIL import Image
from pyzbar.pyzbar import decode

#  Aqui são carregadas as imagens com código QR
leitor1 = decode(Image.open('.\\Fotos\\qr.png'))
leitor2 = decode(Image.open('.\\Fotos\\qr_python.png'))

# O link do resultado é printado no console
print(' ')
print(leitor1[0].data)
print(' ')
print(leitor2[0].data)
