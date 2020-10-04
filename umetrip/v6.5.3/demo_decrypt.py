import base64
from Crypto.Cipher import ARC4
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt_raw_data(raw_data):
    # 第一步：RC4加密
    ciphertext = base64.b64decode(raw_data)
    key = 'CCHPMFMs2XdBmlfd'
    cipher = ARC4.new(key)
    decrypt_data = cipher.decrypt(ciphertext)

    # 第二步：AES加密
    key = 'r6Sl0vIDSlJdmHny'
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(base64.b64decode(decrypt_data))
    return unpad(plaintext, AES.block_size)


if __name__ == '__main__':
    print(decrypt_raw_data('''696f0nChH0n4zEVCGX2mel1YCfAWt771vk2ySSGGfQn5/KcSwJp8bUbDWxn4hnqwmJH48XWCYwlxBNuhZUUXMxnIqu3UJRzntjLOmHICSURCJ1vk/zeV6mhpVLBbhdwYo2cO5neC/qNLiWs52a/cVrnqL78Z6F0fDM29F8kqg0XxySAsNhpfMFtNAlT2Zg1p5MhOmqLs41wBHLDERp87DpyN0jnicMT1JS28xVD8uy9UbMUxOaFjOt8Wu4P/g4XGtr67U4IZvIpd6t7Sz8u21BehquBPdXdB9iDCbzSj968FNcHBAR8iIHt1Zu2KwNTh0ETr3vWv3r+i0YBCpeMBOdg7j1TuQGLVwifkUiAP5/0ov6P8FXkPP9XIE9MOQiXvuMkruwh3alAVClExnfBdjKV72B6Yl4QBX/eWBFn3bcdD6cSXlq4o/CKqMj8NmgTfYqnNsQtQcv4='''))
