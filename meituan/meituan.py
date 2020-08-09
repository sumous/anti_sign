# -*- coding: utf-8 -*-
import base64
import hmac
import hashlib


def get_skcy(url, param, method='POST'):
    # 这个key和版本号有关系
    sha1_key = b'83c96b209eb9731bab61dd03dc34e1afY4yBJhR5whBO3j8lGOkXJQ=='  # 9.4.2
    sha1_key = b'Tb6yTwgSEvbLgLtguw21Q80dR8atTLZ9gbOyX3m9FB0FMGWI60SALA=='  # 10.0.202
    sha1_key = b'LE4CaqXEtX4i+pUPZB4tpJGedHznu9+gCII6Yh1ZnwNSf1UgNiFamw=='  # 11.0.201
    # param += "&__sksc=http"
    raw_string = "&".join(sorted([
        "%s=%s" % (s.split("=")[0], s.split("=")[1] if len(s.split("=")) > 1 else "")
        for s in param.split("&")]))
    before = " ".join([method, url, raw_string]).encode()
    return base64.b64encode(hmac.new(sha1_key, before, hashlib.sha1).digest()).rstrip()
