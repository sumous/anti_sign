import base64
from Crypto.Cipher import AES
s = 'bVbFKJYzi+zfWLfqRn5emyfnsxP0mLSD+OHe4n/+FUbqiCyymyNIJ5eQ2jRXps7+VdjeYiyplOrtCcG+b3a5aKr82UBDJ5usQcTGaePBbfUZuecPTvT17SjTljHns8BOVJtJhcj86Ei4Y4v8PvWo0LRsNtla6gnH0xte9jw3rGkfTj45XY2EBAL+gPzGt/Bp1U7ofYnBDLu0eDXk9k273OH/vRy3Gxx6jKt75oAyCLnS5YbuTdIaAv/wNU6iexinJxyOcyiR5qUiDfh6zZwQedsjL4jChxVE9cjI5D2Uz8HRpoQHDJyuksQVVbwxwp6LAgUbMpCUjMlh3N8cQfkvvS8f7X6ED0rI1BFrjtJHrzbWcy6lnGHFdd9P4I7C3Pvr/tzU+b6wzGsVtyRQUV/02t1kxGfDMYH5P9wpL83okMKg/gH185bh6Hm4jj9U6WrtMKcJVlWMv9Mf8IgLfh6IXJEWeHEB4CrGufCDjBevTYFlvfV/lZiSlcpAyNgA/CS39F4T2Li//8ivuxMDyYmwFC7bRGcr26sD9St/bYJnufg1C9Z6jRhPu2XouROnuYgWXQgGz6ptdz+tCbqMfhPamk8wyVxr0MiB/+4FhijvIZ4d+bfJbpPzvLfPlQlTVCyTnEZPVdA/qnhwEMgTLZKbhToIzQ1ejA8+zTmZYfjfnGqkN0GxcyqMa52JZSSiF09wtiM7aD8ePwq1aTUpiIEmOI4iieugOg7QOp88K/KVhmcT5Ia4UClzdDr066NpZ5oB'
# 加解密
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
password =  'ce77c4ff557fb4b1' # 'nyv2r7jbe048snnyr8t5h6m1re9hnu4k'[:16]
decrypt_data = decrypt(t, password)
print(decrypt_data)

# 生成签名
def gen_signature(params):
    import hashlib
    s = []
    for k in params.keys():
        s.append('%s=%s' % (k, params[k]))
    s.sort()
    signature = hashlib.md5(
        ('&'.join(s) + 'veoxpcaCPEmj9jeHc7ya4yoAb8UuzXrD').encode('latin-1')
    ).hexdigest()
    return signature
params = {
    "uid" : "",
    "deviceVersion" : "13.3",
    "version" : "5.0.0",
    "isVip" : "0",
    "channelID" : "itunes",
    "deviceType" : "iPhone8,4",
    "appType" : "0",
    "userLevel" : "0",
    "language" : "ch",
    "uniqueID" : "EB1FC870-E07E-400B-AF00-DD8EF348CCB6",
    "isYn" : "0",
    "deviceID" : "76fb78933fb78d2041ef44a63d8bb68c29151b629e478155eaa7e9df74cf4f25",
    "device" : "0"
}
signature = gen_signature(params)
assert signature == 'e6458bdbfc542574453ad81628e2db52'
