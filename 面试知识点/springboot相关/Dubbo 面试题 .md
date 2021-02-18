https://www.cnblogs.com/hetutu-5238/p/11958615.html
# 为什么要用Dubbo
随着服务化的进一步发展，服务越来越多，服务之间的调用和依赖关系也越来越 复杂，诞生了面向服务的架构体系(SOA)，
也因此衍生出了一系列相应的技术，如对服务提供、服务调用、连接处理、通信 协议、序列化方式、服务发现、服务路由、日志输出等行为进行封装的服务框架。
就这样为分布式系统的服务治理框架就出现了，Dubbo 也就这样产生了。

# 、Dubbo 的整体架构设计有哪些分层?
* 接口服务层（Service）：该层与业务逻辑相关，根据 provider 和 consumer 的 业务设计对应的接口和实现
* 配置层（Config）：对外配置接口，以 ServiceConfig 和 ReferenceConfig 为 中心
* 服务代理层（Proxy）：服务接口透明代理，生成服务的客户端 Stub 和 服务端 的 Skeleton，以 ServiceProxy 为中心，扩展接口为 ProxyFactory
* 服务注册层（Registry）：封装服务地址的注册和发现，以服务 URL 为中心， 扩展接口为 RegistryFactory、Registry、RegistryService
* 路由层（Cluster）：封装多个提供者的路由和负载均衡，并桥接注册中心，以 Invoker 为中心，扩展接口为 Cluster、Directory、Router 和 LoadBlancce
* 监控层（Monitor）：RPC 调用次数和调用时间监控，以 Statistics 为中心，扩 展接口为 MonitorFactory、Monitor 和 MonitorService
* 远程调用层（Protocal）：封装 RPC 调用，以 Invocation 和 Result 为中心， 扩展接口为 Protocal、Invoker 和 Exporter
* 信息交换层（Exchange）：封装请求响应模式，同步转异步。以 Request 和 Response 为中心，扩展接口为 Exchanger、ExchangeChannel、 ExchangeClient 和 ExchangeServer
* 网络传输层（Transport）：抽象 mina 和 netty 为统一接口，以 Message 为 中心，扩展接口为 Channel、Transporter、Client、Server 和 Codec
* 数据序列化层（Serialize）：可复用的一些工具，扩展接口为 Serialization、 ObjectInput、ObjectOutput 和 ThreadPool

# 服务提供者能实现失效踢出是什么原理？
服务失效踢出基于 zookeeper 的临时节点原理。

# 如何解决服务调用链过长的问题？
可以结合 zipkin 实现分布式服务追踪。

# 、Dubbo 配置文件是如何加载到Spring中的
Spring 容器在启动的时候，会读取到 Spring 默认的一些 schema 以及 Dubbo 自 定义的 schema，
每个 schema 都会对应一个自己的 NamespaceHandler， NamespaceHandler 里面通过 BeanDefinitionParser 来解析配置信息并转化为 需要加载的 bean 对象！

# Dubbo telnet 命令能做什么？
dubbo 服务发布之后，我们可以利用 telnet 命令进行调试、管理。 Dubbo2.0.5 以上版本服务提供端口支持 telnet 命令

# 、Dubbo 如何优雅停机？
Dubbo 是通过 JDK 的 ShutdownHook 来完成优雅停机的,但能实现优雅停机的前提是，在启动时，需要指定参数-Ddubbo.shutdown.hook=true：，
所以如果使用 kill -9 PID 等强制关闭指令，是不会执行优雅停机的，只有通过 kill PID 时，才 会执行。

服务的优雅停机：
    在Dubbo中，优雅停机是默认开启的，停机等待时间为10000毫秒。可以通过配置dubbo.service.shutdown.wait来修改等待时间。
容器的优雅停机：
    当使用org.apache.dubbo.container.Main这种容器方式来使用 Dubbo 时，也可以通过配置dubbo.shutdown.hook为true来开启优雅停机。

#、Dubbo整体流程
zk在dubbo中是服务注册与发现的注册中心,dubbo的调用过程是consumer和provider在启动的时候就和注册中心建立一个socket长连接。
provider将自己的服务注册到注册中心上,注册中心将可用的提供者列表notify给consumer,consumer会将列表存储到本地缓存,
consumer选举出一个要调用的提供者,去远程调用