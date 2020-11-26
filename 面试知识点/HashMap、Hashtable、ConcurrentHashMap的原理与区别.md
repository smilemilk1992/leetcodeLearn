https://www.cnblogs.com/heyonggang/p/9112731.html
https://www.cnblogs.com/williamjie/p/9099141.html

HashTable与HashMap的主要异同点
* 它们都是通过哈希表来实现的，而且都是通过链表来解决哈希冲突的，但是HashMap在链表达到一定长度之后，会将其转化为红黑树。
* 它们计算节点哈希值的方式不同，若key的hashcode为h，则HashMap通过h ^ (h >>> 16)来计算节点的哈希值，而HashTable则将h作为节点的哈希值。
* 它们计算节点对应数组索引下标的方式也不同，HashMap通过haseCode & (capacity - 1)是用来计算节点对应的数组下标，HashTable通过(hashCode & 0x7FFFFFFF) % capacity来计算节点对应的数组下标。hashCode & 0x7FFFFFFF的目的是为了将负的hash值转化为正值。
* HashTable的默认容量为11，而HashMap默认容量为16，Hashtable不要求底层数组的容量一定要为2的整数次幂，而HashMap则要求一定为2的整数次幂。但是，它们的默认负载因子都是0.75。
* Hashtable扩容时，会将容量变为原来的2倍加1，而HashMap扩容时，会将容量变为原来的2倍。
* Hashtable中key和value都不允许为null，而HashMap中key和value都允许为null（key只能有一个为null，而value则可以有多个为null）。若Hashtable中的key或者value为null，则程序运行时会抛出NullPointerException异常。
* HashTable中的大部分的方法都被synchronized修饰，所以HashTable是线程安全的，可以用于多线程环境中，而HashMap则不行。