import hmac
import json
def create_salt(arguments):
    """生成hmac的盐"""
    map_table = {0: "y", 1: "1", 2: "A", 3: "H", 4: "A", 5: "P", 6: "m",
                 7: "s", 8: "y", 9: "C", 10: "x", 11: "R", 12: "M",
                 13: "Q", 14: "D", 15: "c", 16: "y", 17: "C", 18: "V", 19: "S"}
    arguments = arguments.lower()
    m_arg = arguments + arguments
    salt = ""
    for c in m_arg:
        idx = ord(c) % len(map_table)
        salt += map_table[idx]
    return salt

def hmac_sha512(salt, msg):
    """加密hmac_sha512"""
    return hmac.new(salt.encode(), msg.encode(), 'sha512').hexdigest()

def get_enc_kv(url, data):
    url = url.lower()
    
    salt = create_salt(url)
    key = hmac_sha512(salt, url)[10:30]
    msg = (url+url+json.dumps(data, separators=(',', ':'), ensure_ascii=False)).lower()
    value = hmac_sha512(salt, msg)

    return key, value

def main():
    data = {"keyword":"百度","resultCount":"151","searchType":"suggestion","timeConsuming":709}
    url = "/api/userbehavior/sendsearchuserexperience".lower()

    key, value = get_enc_kv(url, data)
    print(key, value)

if __name__ == '__main__':
    main()
