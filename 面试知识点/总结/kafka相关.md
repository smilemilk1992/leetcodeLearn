https://my.oschina.net/u/3070368/blog/4338739
https://www.cnblogs.com/bonelee/p/6893286.html

https://blog.51cto.com/11110720/2535120?source=dra

https://blog.csdn.net/lizhitao/article/details/51718185
https://www.jianshu.com/p/a036405f989c

https://zhuanlan.zhihu.com/p/95831768

#kafka拓扑架构
一个典型的Kafka集群包含若干Producer，若干broker、若干Consumer Group，
以及一个Zookeeper集群。Kafka通过Zookeeper管理集群配置，选举leader，
以及在Consumer Group发生变化时进行rebalance。Producer使用push模式将消息发布到broker，
Consumer使用pull模式从broker订阅并消费消息。

# Topic与Partition
0、Kafka中的topic是以partition的形式存放的，每一个topic都可以设置它的partition数量，Partition的数量决定了组成topic的log的数量。
1、推荐partition的数量一定要大于同时运行的consumer的数量。
2、建议partition的数量大于集群broker的数量，这样消息数据就可以均匀的分布在各个broker中。

# 为什么Topic为什么要设置多个Partition呢，
这是因为kafka是基于文件存储的，通过配置多个partition可以将消息内容分散存储到多个broker上,
这样可以避免文件尺寸达到单机磁盘的上限。同时，将一个topic切分成任意多个partitions，
可以保证消息存储、消息消费的效率，因为越多的partitions可以容纳更多的consumer，
可有效提升Kafka的吞吐率。因此，将Topic切分成多个partitions的好处是可以将大量的
消息分成多批数据同时写到不同节点上，将写请求分担负载到各个集群节点。

# Consumer消费机制
consumer只是从broker pull消息，pull模式的一个好处是Consumer可自主控制消费消息的速率，
同时Consumer还可以自己控制消费消息的方式是批量的从broker拉取数据还是逐条消费数据。

#kafka如何保证高吞吐
1、顺序读写
    kafka中每条消息写到partition中，是顺序写入磁盘的，这种顺序写入磁盘机制是kafka高吞吐率的一个很重要的保证。
    kafka的消息是不断追加到文件中的，这个特性使kafka可以充分利用磁盘的顺序读写性能
2、多分区
    kafka中的topic中的内容可以被分为多分partition存在,每个partition又分为多个段segment,
    所以每次操作都是针对一小部分做操作，很轻便，并且增加并行操作的能力
3、零拷贝
4、批量发送
    kafka允许进行批量发送消息，producter发送消息的时候，可以将消息缓存在本地,等到了固定条件发送到kafka
    1、等消息条数到固定条数
    2、一段时间发送一次
5、数据压缩
    Kafka还支持对消息集合进行压缩，Producer可以通过GZIP或Snappy格式对消息集合进行压缩。
    压缩的好处就是减少传输的数据量，减轻对网络传输的压力。
    Producer压缩之后，在Consumer需进行解压，虽然增加了CPU的工作，但在对大数据处理上，
    瓶颈在网络上而不是CPU，所以这个成本很值得


#kafka如何保证高可用
1、Acks=all，必须跟 ISR 列表里至少有 2 个以上的副本配合使用
2、broker多副本
3、Partition多副本
4、手动提交改为自动提交

#kafka的ISR是个啥
这个机制简单来说，就是会自动给每个 Partition 维护一个 ISR（同步副本集） 列表，
这个列表里一定会有 Leader，然后还会包含跟 Leader 保持同步的 Follower。
也就是说，只要 Leader 的某个 Follower 一直跟他保持数据同步，那么就会存在于 ISR 列表里。
但是如果 Follower 因为自身发生一些问题，导致不能及时的从 Leader 同步数据过去，
那么这个 Follower 就会被认为是“out-of-sync”，被从 ISR 列表里踢出去。

就是 Kafka 自动维护和监控哪些 Follower 及时的跟上了 Leader 的数据同步。

#kafka分区算法（生产者）
1、key存在时 对其采用murmur2 hash算法，再对总分区数取模 得到分区数。
2、key不存在时，轮询，

#consumer group的分区再平衡
每个consumer负责自己对应的分区，但是当group中有consumer退出或者新加入consumer，
再或者topic中新增partition，group中的消费者负责的partition都得重新计算，
Rebalance 期间consumer不能再消费消息，做rebalance的时候是会影响整个consumer group。

#kafka broker调优
https://www.jianshu.com/p/c9bb658dc788?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

#kafka ISR、OSR、AR、HW、LEO、LSO、LW
AR=ISR+OSR
HW :
    ISR（in-sync replica ）分区所有副本中offset最小的副本他最后一条消息后的待写位置。也是该副本的LEO！
    （High Watermark）俗称高水位，它标识了一个特定的消息偏移量（offset），消费者只能拉取到这个offset之前的消息。
    即消费者可见的message的offset是HW-1
LEO ISR分区副本最后一条消息的待写位！即每个副本最大offset+1=LEO
LSO :
    消费端参数——isolation.level,这个参数用来配置消费者事务的隔离级别。字符串类型，“read_uncommitted”和“read_committed”，
    表示消费者所消费到的位置，如果设置为“read_committed"，那么消费这就会忽略事务未提交的消息，既只能消费到LSO(LastStableOffset)的位置，
    默认情况下，”read_uncommitted",既可以消费到HW（High Watermak）的位置。

LSO≤HW≤LEO

#zk 与kafka 
数据一致性 kafka 是保存副本 leader读写，follower 只备份 而 zookeeper是 leader 读写，follower负责读

#Zookeeper对kafka作用
1、leader选举和follower信息同步
2、broker注册
3、topic注册
4、生产者负载均衡：数据一致性 kafka 是保存副本 leader读写，follower 只备份 而 zookeeper是 leader 读写，follower负责读
5、消费者负载均衡
    与生产者类似，Kafka中的消费者同样需要进行负载均衡来实现多个消费者合理地从对应的Broker服务器上接收消息，
    每个消费者分组包含若干消费者，每条消息都只会发送给分组中的一个消费者，不同的消费者分组消费自己特定的Topic下面的消息，互不干扰。
6、消息消费进度Offset 记录
7、消费者注册




