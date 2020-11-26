# 1、HashMap简介 JDK1.8 https://zhuanlan.zhihu.com/p/125628540
* HashMap是基于哈希表实现的，每一个元素是一个key-value对，其内部通过单链表解决冲突问题，容量不足（超过了阀值）时，同样会自动增长。

* HashMap是非线程安全的，只是用于单线程环境下，多线程环境下可以采用concurrent并发包下的concurrentHashMap。

* HashMap 实现了Serializable接口，因此它支持序列化，实现了Cloneable接口，能被克隆。

* HashMap存数据的过程是：

* HashMap内部维护了一个存储数据的Entry数组，HashMap采用链表解决冲突，每一个Entry本质上是一个单向链表。当准备添加一个key-value对时，首先通过hash(key)方法计算hash值，然后通过indexFor(hash,length)求该key-value对的存储位置，计算方法是先用hash&0x7FFFFFFF后，再对length取模，这就保证每一个key-value对都能存入HashMap中，当计算出的位置相同时，由于存入位置是一个链表，则把这个key-value对插入链表头。

* HashMap中key和value都允许为null。key为null的键值对永远都放在以table[0]为头结点的链表中。

* HashMap继承自AbstractMap类。并且实现了Map接口

* HashMap底层是一个Entry数组，当发生hash冲突的时候，hashmap是采用链表的方式来解决的，在对应的数组位置存放链表的头结点。对链表而言，新加入的节点会从头结点加入。

        // 新增Entry。将“key-value”插入指定位置，bucketIndex是位置索引。      
            void addEntry(int hash, K key, V value, int bucketIndex) {      
                // 保存“bucketIndex”位置的值到“e”中      
                Entry<K,V> e = table[bucketIndex];      
                // 设置“bucketIndex”位置的元素为“新Entry”，      
                // 设置“e”为“新Entry的下一个节点”      
                table[bucketIndex] = new Entry<K,V>(hash, key, value, e);      
                // 若HashMap的实际大小 不小于 “阈值”，则调整HashMap的大小      
                if (size++ >= threshold)      
                    resize(2 * table.length);      
            }  
*在hashmap做put操作的时候会调用到以上的方法。现在假如A线程和B线程同时对同一个数组位置调用addEntry，两个线程会同时得到现在的头结点，然后A写入新的头结点之后，B也写入新的头结点，那B的写入操作就会覆盖A的写入操作造成A的写入操作丢失

* HashMap把Hashtable的contains方法去掉了，改成containsValue和containsKey，因为contains方法容易让人引起误解。
* hash函数是先拿到通过key 的hashcode，是32位的int值，然后让hashcode的高16位和低16位进行异或操作。

        static final int hash(Object key) {
                int h;
                return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
            }
* 底层数组+链表或红黑树实现，可以存储null键和null值，线程不安全
* 初始size为16，扩容：newsize = oldsize*2，size一定为2的n次幂
* 扩容针对整个Map，每次扩容时，原来数组中的元素依次重新计算存放位置，并重新插入
* 插入元素后才判断该不该扩容，有可能无效扩容（插入后如果扩容，如果没有再次插入，就会产生无效扩容）
* 当Map中元素总数超过Entry数组的75%，触发扩容操作，为了减少链表长度，元素分配更均匀
* 计算index方法：index = hash & (tab.length – 1)
* 链表转红黑树阈值是8以空间换时间，这样以来查询的效率就变为O(logN)  红黑树转链表阈值是6
* 内部节点插入无序，有序的Map是LinkedHashMap 和 TreeMap
* LinkedHashMap内部维护了一个单链表，有头尾节点，同时LinkedHashMap节点Entry内部除了继承HashMap的Node属性，还有before 和 after用于标识前置节点和后置节点。可以实现按插入的顺序或访问顺序排序。
* HashMap的容量必须是2的N次方，如果你指定了一个非2的N次方的整数S，那么HashMap在内部会把它转化为大于S的2的N次方的整数。
* HashMap在并发执行put操作时会引起死循环，是因为多线程会导致HashMap的Entry链表 形成环形数据结构，一旦形成环形数据结构，Entry的next节点永远不为空，就会产生死循环获 取Entry。

HashMap的初始值还要考虑加载因子:
* 哈希冲突：若干Key的哈希值按数组大小取模后，如果落在同一个数组下标上，将组成一条Entry链，对Key的查找需要遍历Entry链上的每个元素执行equals()比较。
* 加载因子：为了降低哈希冲突的概率，默认当HashMap中的键值对达到数组大小的75%时，即会触发扩容。因此，如果预估容量是100，即需要设定100/0.75＝134的数组大小。
* 空间换时间：如果希望加快Key查找的时间，还可以进一步降低加载因子，加大初始大小，以降低哈希冲突的概率。


1.7 与1.8区别

* 数组+链表改成了数组+链表或红黑树；
* 链表的插入方式从头插法改成了尾插法，简单说就是插入时，如果数组位置上已经有元素，1.7将新元素放到数组中，原始节点作为新节点的后继节点，1.8遍历链表，将元素放置到链表的最后；
* 扩容的时候1.7需要对原数组中的元素进行重新hash定位在新数组的位置，1.8采用更简单的判断逻辑，位置不变或索引+旧容量大小；
* 在插入时，1.7先判断是否需要扩容，再插入，1.8先进行插入，插入完成再判断是否需要扩容；
