# 什么是redis
Redis 是完全开源免费的，遵守 BSD 协议，是一个高性能的 key-value 数据库。
Redis 与其他 key - value 缓存产品有以下三个特点：
    * Redis 支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再 次加载进行使用。 
    * Redis 不仅仅支持简单的 key-value 类型的数据，同时还提供 list，set，zset， hash 等数据结构的存储。 
    * Redis 支持数据的备份，即 master-slave 模式的数据备份。

性能极高 – Redis 能读的速度是 110000 次/s,写的速度是 81000 次/s 。

Redis持久化有两种方式，分别是RDB（又称快照）与AOF。对于两种方式各有优缺点，具体如下：

RDB（数据快照）：异步全量一次同步内存中所有序列化的二进制数据，同步慢，数据较小。单独使用RDB持久化，存在数据丢失风险（半持久化）

AOF（日志追加）：增量同步操作指令，同步较快，数据量随时间增加而增多，需定期进行AOF文件重写，以便减小日志文件。（全持久化）

Redis的所有数据都是保存在内存中，然后不定期的通过异步方式保存到磁盘上(这称为“半持久化模式”)；也可以把每一次数据变化都写入到一个append only file(aof)里面(这称为“全持久化模式”)。

在日常操作中，一般都是从AOF日志中来恢复数据，因为RDB会丢失大量数据。但是AOF恢复数据又会花费较长时间。
于是从Redis4.0开始，Redis开始支持混合持久化。即将RDB与AOF结合使用，RDB负责定时全量持久化数据，AOF负责记录最后一次RDB后的增量日志。使得Redis的数据恢复在恢复效率与数据完整性之间取得一个完美的平衡点。

# Redis的数据类型？

答：Redis 支持五种数据类型：string（字符串），hash（哈希），list（列表）， set（集合）及 zsetsorted set：有序集合)。
我们实际项目中比较常用的是 string，hash 如果你是 Redis 中高级用户，还需要 加上下面几种数据结构 HyperLogLog、Geo、Pub/Sub。
如果你说还玩过 Redis Module，像 BloomFilter，RedisSearch，Redis-ML，面 试官得眼睛就开始发亮了。

# 使用Redis有哪些好处？
1、速度快，因为数据存在内存中，类似于 HashMap，HashMap 的优势就是查 找和操作的时间复杂度都是 O1)
2、支持丰富数据类型，支持 string，list，set，Zset，hash 等
3、支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行， 要么全部不执行
4、丰富的特性：可用于缓存，消息，按 key 设置过期时间，过期后将会自动删除

# Redis相比Memcached有哪些优势？
1、Memcached 所有的值均是简单的字符串，redis 作为其替代者，支持更为丰 富的数据类 
2、Redis 的速度比 Memcached 快 
3、Redis 可以持久化其数据

# Memcache与Redis的区别都有哪些？

1、存储方式 Memecache 把数据全部存在内存之中，断电后会挂掉，数据不能 超过内存大小。 Redis 有部份存在硬盘上，这样能保证数据的持久性。
2、数据支持类型 Memcache 对数据类型支持相对简单。 Redis 有复杂的数据类 型。
3、使用底层模型不同 它们之间底层实现方式 以及与客户端之间通信的应用协议 不一样。 Redis 直接自己构建了 VM 机制 ，因为一般的系统调用系统函数的话， 会浪费一定的时间去移动和请求
4、Memecache可以缓存图片和视频

# 为什么mc在纯KV时更快呢？

mc是预分配内存机制
redis的VM机制更慢
redis的CPU计算复杂
多线程可以利用多核

# 为什么有的时候单线程的redis比多线程的Memecache快
1、mc的多线程模型引入了缓存一致性和锁，加锁带来了性能损耗

一个字符串类型的值能存储最大容量是512M

# redis过期键的删除策略

1、定时删除:在设置键的过期时间的同时，创建一个定时器 timer). 让定时器在键 的过期时间来临时，立即执行对键的删除操作。
优点：节约内存，到时就删除，快速释放不必要的内存占用
缺点：抢占CPU，当CPU负载很高的时候，会影响redis指令的响应时间和指令吞吐量

2、惰性删除:放任键过期不管，但是每次从键空间中获取键时，都检查取得的键是 否过期，如果过期的话，就删除该键;如果没有过期，就返回该键。
优点：节约CPU性能
缺点：大量失效数据积压之后，内存占用大，存储空间压力大

3、定期删除（折中方案）:每隔一段时间程序就对数据库进行一次检查，删除里面的过期键。至 于要删除多少过期键，以及要检查多少个数据库，则由算法决定。
周期性轮询redis库中的时效性数据，采用随机抽取的策略，利用过期数据占比的方式控制删除频度
每隔一段时间来执行一次删除过期键操作，并通过限制删除操作执行的时长和频率来减少删除操作对CPU时间的影响
Redis使用的是定期删除和惰性删除结合起来的策略。其中惰性删除很好理解，redis操作每个key的时候都会先进行过期时间判断，如果过期就删除。定期删除是跟随Redis的周期性操作，在规定的时间内，分多次遍历各个数据库，每次从过期字典中随机抽取指定数量过期键并将其删除。
# redis的淘汰策略（当 Redis 的内存达到规定的最大值时，允许配置 6 种策略中的一种进行淘汰键值，并且将一些键值对进行回收。）
volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最 少使用的数据淘汰，以最近一次访问时间作为参考
volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过 期的数据淘汰
volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意 选择数据淘汰
allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰
allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰
no-enviction（驱逐）：禁止驱逐数据

redis 4.0
volatile-lfu：会使用 LFU 算法筛选设置了过期时间的键值对删除，淘汰最近一段时间被访问次数最少的数据，以次数作为参考
allkeys-lfu：使用 LFU 算法在所有数据中进行筛选删除。，淘汰最近一段时间被访问次数最少的数据，以次数作为参考

注意这里的 6 种机制，volatile 和 allkeys 规定了是对已设置过期时间的数据集淘 汰数据还是从全部数据集淘汰数据，后面的 lru、ttl 以及 random 是三种不同的 淘汰策略，再加上一种 no-enviction 永不回收的策略。

使用策略规则：
1、如果数据呈现幂律分布，也就是一部分数据访问频率高，一部分数据访问频率 低，则使用 allkeys-lru
2、如果数据呈现平等分布，也就是所有的数据访问频率都相同，则使用 allkeys-random

第一组：针对设置了过期时间的数据，从这里面应用如下的逐出算法。(最近一段时间指的是新的数据要被添加时之前的一段时间)

volatile-lru：（least recently used）最近一段时间内最久未被使用的数据，针对的是时间，最长时间未被使用。
volatile-lrf：（least frequently used）最近一段时间内使用次数/频率最少的数据，针对的是使用频率小少(在ehcache中对应的是hitCount的值)。
volatile-ttl：（time to live）快要过期的数据，即过期时间所剩不多的。
volatile-random：从设置了过期时间的数据中随机挑选删除。
2、第二组：针对整个redis中的所有数据

allkeys-lru：和上面的lru策略一样，只不过是针对所有数据。
allkeys-lfu：和上面的lfu策略一样，只不过是针对所有数据。
allkeys-random：随机挑选删除。
3、第三组：不设置逐出策略，超过最大内存限制后直接报oom

no-enviction：不逐出数据，redis4.0默认策略。
# 、为什么edis需要把所有数据放到内存中？
答：Redis 为了达到最快的读写速度将数据都读到内存中，并通过异步的方式将数 据写入磁盘。所以 redis 具有快速和数据持久化的特征。如果不将数据放在内存中， 磁盘 I/O 速度为严重影响 redis 的性能。在内存越来越便宜的今天，redis 将会越 来越受欢迎。如果设置了最大使用的内存，则数据已有记录数达到内存限值后不 能继续插入新值。

# Jedis的Redis Sharding实现具有如下特点
1、采用一致性哈希算法(consistent hashing)，将key和节点name同时hashing，然后进行映射匹配，采用的算法是MURMUR_HASH。采用一致性哈希而不是采用简单类似哈希求模映射的主要原因是当增加或减少节点时，不会产生由于重新匹配造成的rehashing。一致性哈希只影响相邻节点key分配，影响量小。
2.为了避免一致性哈希只影响相邻节点造成节点分配压力，ShardedJedis会对每个Redis节点根据名字(没有，Jedis会赋予缺省名字)会虚拟化出160个虚拟节点进行散列。根据权重weight，也可虚拟化出160倍数的虚拟节点。用虚拟节点做映射匹配，可以在增加或减少Redis节点时，key在各Redis节点移动再分配更均匀，而不是只有相邻节点受影响。
3.ShardedJedis支持keyTagPattern模式，即抽取key的一部分keyTag做sharding，这样通过合理命名key，可以将一组相关联的key放入同一个Redis节点，这在避免跨节点访问相关数据时很重要。

比如扩容，当想要增加Redis节点时，尽管采用一致性哈希，毕竟还是会有key匹配不到而丢失，这时需要键值迁移。
作为轻量级客户端sharding，处理Redis键值迁移是不现实的，这就要求应用层面允许Redis中数据丢失或从后端数据库重新加载数据。但有些时候，击穿缓存层，直接访问数据库层，会对系统访问造成很大压力。有没有其它手段改善这种情况？
Redis作者给出了一个比较讨巧的办法–presharding，即预先根据系统规模尽量部署好多个Redis实例，这些实例占用系统资源很小，一台物理机可部署多个，让他们都参与sharding，当需要扩容时，选中一个实例作为主节点，新加入的Redis节点作为从节点进行数据复制。数据同步后，修改sharding配置，让指向原实例的Shard指向新机器上扩容后的Redis节点，同时调整新Redis节点为主节点，原实例可不再使用。
 这样，我们的架构模式变成一个Redis节点切片包含一个主Redis和一个备Redis。在主Redis宕机时，备Redis接管过来，上升为主Redis，继续提供服务。主备共同组成一个Redis节点，通过自动故障转移，保证了节点的高可用性。则Sharding架构演变成：
 
 # Redis官方集群方案 Redis Cluster
 Redis Cluster是一种服务器Sharding技术，3.0版本开始正式提供。Redis Cluster中，Sharding采用slot(槽)的概念，一共分成16384个槽，这有点儿类似前面讲的pre sharding思路。对于每个进入Redis的键值对，根据key进行散列，分配到这16384个slot中的某一个中。使用的hash算法也比较简单，就是CRC16后16384取模。Redis集群中的每个node(节点)负责分摊这16384个slot中的一部分，也就是说，每个slot都对应一个node负责处理。当动态添加或减少node节点时，需要将16384个槽做个再分配，槽中的键值也要迁移。当然，这一过程，在目前实现中，还处于半自动状态，需要人工介入。
 
Redis集群，要保证16384个槽对应的node都正常工作，如果某个node发生故障，那它负责的slots也就失效，整个集群将不能工作。为了增加集群的可访问性，官方推荐的方案是将node配置成主从结构，即一个master主节点，挂n个slave从节点。这时，如果主节点失效，Redis Cluster会根据选举算法从slave节点中选择一个上升为主节点，整个集群继续对外提供服务。这非常类似前篇文章提到的Redis Sharding场景下服务器节点通过Sentinel监控架构成主从结构，只是Redis Cluster本身提供了故障转移容错的能力。
 
有 A，B，C 三个节点的集群,在没有复制模型的情况下,如果节点 B 失败了， 那么整个集群就会以为缺少 5501-11000 这个范围的槽而不可用。

 # Redis有三种集群模式
 * 主从模式（主从模式的弊端就是不具备高可用性，当master挂掉以后，Redis将不能再对外提供写入操作）
    * 主数据库可以进行读写操作，当读写操作导致数据变化时会自动将数据同步给从数据库
    * 从数据库一般都是只读的，并且接收主数据库同步过来的数据
    * 一个master可以拥有多个slave，但是一个slave只能对应一个master
    * slave挂了不影响其他slave的读和master的读和写，重新启动后会将数据从master同步过来
    * master挂了以后，不影响slave的读，但redis不再提供写服务，master重启后redis将重新对外提供写服务
    * master挂了以后，不会在slave节点中重新选一个master

* Sentinel模式
    * sentinel模式是建立在主从模式的基础上，如果只有一个Redis节点，sentinel就没有任何意义
    * 当master挂了以后，sentinel会在slave中选择一个做为master，并修改它们的配置文件，其他slave的配置文件也会被修改，比如slaveof属性会指向新的master
    * 当master重新启动后，它将不再是master而是做为slave接收新的master的同步数据
    * sentinel因为也是一个进程有挂掉的可能，所以sentinel也会启动多个形成一个sentinel集群
    * 多sentinel配置的时候，sentinel之间也会自动监控
    * 当主从模式配置密码时，sentinel也会同步将配置信息修改到配置文件中，不需要担心
    * 一个sentinel或sentinel集群可以管理多个主从Redis，多个sentinel也可以监控同一个redis
    * sentinel最好不要和Redis部署在同一台机器，不然Redis的服务器挂了以后，sentinel也挂了


* Cluster模式

# 、Jedis与Redisson对比有什么优缺点？
：Jedis 是 Redis 的 Java 实现的客户端，其 API 提供了比较全面的 Redis 命令 的支持；Redisson 实现了分布式和可扩展的 Java 数据结构，和 Jedis 相比，功能 较为简单，不支持字符串操作，不支持排序、事务、管道、分区等 Redis 特性。 Redisson 的宗旨是促进使用者对 Redis 的关注分离，从而让使用者能够将精力更 集中地放在处理业务逻辑上。

# 说说Redis哈希槽的概念
Redis 集群没有使用一致性 hash,而是引入了哈希槽的概念，Redis 集群有 16384 个哈希槽，每个 key 通过 CRC16 校验后对 16384 取模来决定放置哪个槽， 集群的每个节点负责一部分 hash 槽。

# 如果有大量的key需要设置同一时间过期，一般需要注意什么？
如果大量的 key 过期时间设置的过于集中，到过期的那个时间点，redis 可能 会出现短暂的卡顿现象。一般需要在时间上加一个随机值，使得过期时间分散一 些

# 使用过Redis做异步队列么，你是怎么用的？
一般使用 list 结构作为队列，rpush 生产消息，lpop 消费消息。当 lpop 没有 消息的时候，要适当 sleep 一会再重试。

# redis 如何实现延时队列？
：使用 sortedset，拿时间戳作为 score，消息内容作为 key 调用 zadd 来生产消息，消费者用 zrangebyscore 指令 获取 N 秒之前的数据轮询进行处理。到这里，面试官暗地里已经对你竖起了大拇 指。但是他不知道的是此刻你却竖起了中指，在椅子背后。

# 使用过Redis分布式锁么，它是什么回事
先拿 setnx 来争抢锁，抢到之后，再用 expire 给锁加一个过期时间防止锁忘记了 释放。


# redis为什么那么快-https://www.toutiao.com/i6916758138347815438/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1610671141&app=news_article&utm_source=weixin&utm_medium=toutiao_ios&use_new_style=1&req_id=2021011508390001020402804528146060&share_token=7B249A92-4F1B-4945-BDCE-667907933744&group_id=6916758138347815438
1、Redis 是一款纯内存结构，避免了磁盘 I/O 等耗时操作。
2、Redis 命令处理的核心模块为单线程，减少了锁竞争，以及频繁创建线程和销毁线程的代价，减少了线程上下文切换的消耗。
3、采用了 I/O 多路复用机制，大大提升了并发效率。