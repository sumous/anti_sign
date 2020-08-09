# 美团客户端skcy参数的生成算法

需要注意美团每个版本的key值是不一样的，需要对应版本号。
```python
sha1_key = b'83c96b209eb9731bab61dd03dc34e1afY4yBJhR5whBO3j8lGOkXJQ=='  # 9.4.2
sha1_key = b'Tb6yTwgSEvbLgLtguw21Q80dR8atTLZ9gbOyX3m9FB0FMGWI60SALA=='  # 10.0.202
sha1_key = b'LE4CaqXEtX4i+pUPZB4tpJGedHznu9+gCII6Yh1ZnwNSf1UgNiFamw=='  # 11.0.201
```
