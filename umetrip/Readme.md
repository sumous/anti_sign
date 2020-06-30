# 航旅纵横（umetrip）app签名算法
航旅纵横app比较麻烦的点在于：安卓的apk加了壳，懒得去壳了。ios端的app做了反调试，只要debugserver hook上去后，立刻退出。大概找了一下，没看到ptrace的地方。

最后用frida把关键的位置打出来，得到密钥。然后静态分析CCCript调用入口，得到改解密算法。
