## 0x1.背景
抓包过程中面临几大问题，抓包面临过程中，常见两种问题解决办法：1.普通https用中间人攻击的方法解决，2.自签名证书校验（SSL-pinning）采用hook证书校验方法。而还有很多app，像美团，根本连包都抓不到。因此提出了一种奇淫技巧：降级网络抓包。
    
降级网络抓包的想法来源于2017年逆向淘宝客户端的x-sign的时候，hook后发现淘宝客户端的请求在应用层上都是走http协议，并且http请求放浏览器上都能正常请求，当时一直都是百思不得其。后又看到了美团技术博客https://tech.meituan.com/2017/03/17/shark-sdk.html  ，提及当Failover方案，当长连接服务器故障时，可绕过长连接服务器，向业务服务器发起HTTP公网请求。降级抓包的想法由此诞生。

## 0x2.环境准备
- 1.openwrt路由器一个
- 2.已越狱iphone一部，并且通过cydia安装了netstat的network commands包
- 3.一台笔记本，安装charles用于抓包

## 0x3.降级网络
我们以滴滴app为例，降级网络需要把app服务商的所有长连接服务器都禁用了，因此可以用到iptables进行ip封禁。当所以长连接服务器都被禁用了后，app就会选择http/https进行通信，网络包就抓取到了。以下是详细步骤：
* （1）iphone和笔记本电脑连上openwrt的wifi，并且设置iphone的代理为笔记本的ip，装好代理的证书
* （2）通过ssh连接iphone，打开滴滴app，等app开启后等待大概1分钟（避免初始化过程建立的连接影响判断，同时稳定一分钟都没断的很可能就是长连接）。然后在ssh终端输入netstat -an | grep ESTABLISHED | grep -v 8888  ， 得到类似如下截图：
  ![image](https://github.com/sumous/anti_sign/blob/master/resources/ios_netstat.png)


    PS:为避免干扰，最好把其他app全退出，只开滴滴！
    从截图里，可以看到139.199.240.12这个ip是长连接。17.57.145.85应该是苹果的某项服务
* （3）ssh登录openwrt路由器，输入命令：iptables -I FORWARD -d 139.199.240.12 -j DROP  。将往139.199.240.12发的包全DROP。
* （4）关闭滴滴app，然后重新打开app。重复(2)(3)步骤，直到抓到http的包，类似如下：
  ![image](https://github.com/sumous/anti_sign/blob/master/resources/charlse_didi.jpg)


大功告成！

## 0x4.总结
降级网络的方法，测试下来，适用于淘宝客户端、滴滴客户端、美团客户端以及支付宝客户端，是一种基于服务端理解猜想出来的方案，未来可应用场景也很多。实际测试效果如下：
- 淘宝系客户端（淘宝app、天猫app、闲鱼app等等）抓包全部没有问题
- 滴滴客户端抓包没有问题
- 美团客户端抓包也没有问题
- 支付宝客户端部分请求可行
