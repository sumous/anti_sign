# -*- coding:utf-8 -*-
import hashlib
app_code = '315DQ162G0E8'
cap_key = '5d5a5a1c6f301f485a118b8f'


def get_caocao_sign(data):
    keys = data.keys()
    keys = sorted(keys)
    encrypt_str = ''
    for k in keys:
        encrypt_str += '%s=%s&' % (k, data[k])
    encrypt_str += 'key=' + cap_key
    return hashlib.md5(encrypt_str.encode()).hexdigest().upper()


if __name__ == '__main__':
    data = {
        'appVersion':	'4.3.6',
        'bizNumInfo':	'[{"bizNo":1,"queriedCount":0},{"bizNo":3,"queriedCount":0},{"bizNo":5,"queriedCount":0},{"bizNo":9,"queriedCount":0},{"bizNo":2,"queriedCount":0},{"bizNo":13,"queriedCount":0},{"bizNo":16,"queriedCount":0},{"bizNo":61,"queriedCount":0}]',
        'buildVersion':	'215',
        'clientType':	'1',
        'customerNo':	'14013727',
        'fullVersion':	'4.3.6.215',
        'isJailBreak':	'1',
        'mobileType':	'ios',
        'pageSize':	'20',
        'systemType':	'iPhoneSE',
        'systemVersion':	'12.1',
        'timestamp':	'1566982002264',
        'version':	'4.3.6'
    }
    data['appCode'] = app_code
    data['sign'] = get_caocao_sign(data)
    print(data['sign'])
