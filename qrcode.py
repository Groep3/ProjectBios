import pyqrcode
import random


def createqr():
    aanmeldcode = random.randrange(100000, 1000000)
    qrcode = pyqrcode.create('{}'.format(aanmeldcode), error='L', version=10)
    qrcode.png('qrcode.png', scale=5)
    return(aanmeldcode)
    #qrcode.show()

createqr()
