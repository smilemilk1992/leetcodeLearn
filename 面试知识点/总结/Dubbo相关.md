#Dubbo整体架构是什么样的
Provider	暴露服务的服务提供方
Consumer	调用远程服务的服务消费方
Registry	服务注册与发现的注册中心
Monitor	统计服务的调用次数和调用时间的监控中心
Container	服务运行容器

整个发布订阅过程：
启动容器，加载，运行服务提供者。
服务提供者在启动时，在注册中心发布注册自己提供的服务。
服务消费者在启动时，在注册中心订阅自己所需的服务。

注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更数据给消费者。
服务消费者，从提供者地址列表中，基于软负载均衡算法，选一台提供者进行调用，如果调用失败，再选另一台调用。
服务消费者和提供者，在内存中累计调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。



#Dubbo负载均衡策略-
    spring-dubbo 版本
    服务端：<dubbo:service interface="接口名" loadbalance="roundrobin" weight="5"/> 默认random
    客户端：<dubbo:reference interface="" loadbalance="roundrobin" />
    也可通过可视化界面来配置
    通过springboot-dubbo版本
    客户端：
    @Reference(version = "1.0.0",mock = "com.example.consumer.service.DemoMockImpl",interfaceClass=IDemoService.class,check = true,loadbalance = "roundrobin")
    服务端：
    @Service(version = "1.0.0",cluster = "failover",timeout = 3000,retries=2,interfaceClass = IDemoService.class,loadbalance = "roundrobin",weight = 10)
1、Random-随机，按权重设置随机概率
2、RoundRobin-轮询，按照公约后的权重设置轮询比率
3、LeastActive-最少活跃调用数，相同活跃数的随机，活跃数指调用前后计数差
4、ConsistentHash-一直hash，相同参数请求总是发到同一提供者

#集群容错策略
<dubbo:service cluster="failsafe" />
<dubbo:reference cluster="failsafe" />
1、Failover cluster（失败重试）可通过retries 设置重试次数
2、Failsafe cluster(失败安全)当服务出现异常时候忽略，程序继续运行（通常用于记录日志功能）。在实现上，当出现调用失败时，会忽略此错误，并记录一条日志，同时返回一个空结果，在上游看来调用是成功的。
3、Failfast cluster(快速失败)请求只发送一次（通常用于非幂等请求场景，比如说转账，避免重复转账）。
4、Failback cluster(失败恢复)请求失败后，记录请求，后续定时重发（用户消息发送场景）
5、Forking cluster(并行请求)并行调用服务提供者，只要有一个节点返回正确则返回（只适用于查询数据场景）。
6、broadcast cluster（广播请求）广播所有服务提供者，诸葛只要一个节点返回错误就返回错误（用于数据同步，缓存更新场景）。