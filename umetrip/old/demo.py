import base64
from Crypto.Cipher import AES
s = '''Q0bKnmf5UGWlTVdLSvL6mdbBCvkd4AFWMhOdXk5ZT3735uxOFDVjtmI4oP8Aguum
TQ1n81JNp6oqaSemFr4ROsmGGIxnWHIfVgIjXqE2uOUG2Bzqoc9meInqqTTfXLuj
2IvCZlclA7M61xxww9Xf4/s/c+Xwp3+RRUa5/mR/uQVHFo4ZdEkM61wShrmbuUUF
3G8ClSBCJBxj8WxDIqCaPTRjxJluB6xRx/V4jjA2YTNh+pS3KGczvBwd6tinqhfi
TdU7kEaQL67cERU6CQw7j/TRzVV4NLjbZef6dLq9Cphgdti5SwyXXRZxtIS1YL5+
6JswISSUNftigPWhO3v9g48YYvUxau2pj5kZesPj3FSAOD9cdaye9p6KZU4tteNy
63r8s+0Fry32h6ojKHEz+1cISijskk9JDlkrdsr61lo='''
t = base64.b64decode(s)
def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-s[-1]]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_ECB, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data
password = 'whc5xi9nOTydj0i3'
decrypt_data = decrypt(t, password)
print(decrypt_data)
