# 航旅纵横（umetrip）app签名算法
航旅纵横app比较麻烦的点在于：安卓的apk加了壳，懒得去壳了。ios端的app做了反调试，只要debugserver hook上去后，立刻退出。大概找了一下，没看到ptrace的地方。

## 旧版
用frida把关键的位置打出来，得到密钥。然后静态分析CCCript调用入口，得到改解密算法。


## v6.5.3版本
这个版本的加密算法，较之前的加密算法升级了。采用AES+RC4进行加密，同时代码上做了一系列乱七八糟的混淆，不过都是花拳绣腿，仔细看就知道哪些是核心代码了。

最最关键的地方是，不知道是有人把RC4源码公布了，还是抄袭别人的（连length拼错的方式都一样）。地址是：https://github.com/Virtue86/RC4ForOC/blob/bae23ef0666b529a173d598ae9004a2946203fa7/RC4Encrypt/RC4Encrypt/RC4/EPRC4Cryptor.m

关键的几个函数：
- +[ume000 cc2_action:lKey]   rc4核心加密代码，lKey是rc4的密钥
- +[ume000 encryptData:aKey:lKey:isBase]   加密的入口，其中，aKey是AES的密钥，lKey是rc4的密钥
- AES的加密入口，没有找到，纯粹靠猜的
