# 1、HashTable简介
* Hashtable同样是基于哈希表实现的，同样每个元素是一个key-value对，其内部也是通过单链表解决冲突问题，容量不足（超过了阀值）时，同样会自动增长。
* Hashtable也是JDK1.0引入的类，是线程安全的，能用于多线程环境中。
* Hashtable同样实现了Serializable接口，它支持序列化，实现了Cloneable接口，能被克隆。
* Hashtable继承自Dictionary类 ，并且实现了Map接口
* 多线程环境下使用HashTable
* Hashtable则保留了contains，containsValue和containsKey三个方法，其中contains和containsValue功能相同。
* Hashtable中，key和value都不允许出现null值。但是如果在Hashtable中有类似put(null,null)的操作，编译同样可以通过，因为key和value都是Object类型，但运行时会抛出NullPointerException异常，这是JDK的规范规定的。
* 哈希值的使用不同，HashTable直接使用对象的hashCode。而HashMap重新计算hash值。
* Hashtable计算hash值，直接用key的hashCode()，而HashMap重新计算了key的hash值，Hashtable在求hash值对应的位置索引时，用取模运算

* 底层数组+链表实现，无论key还是value都不能为null，线程安全，实现线程安全的方式是在修改数据时锁住整个HashTable，效率低，ConcurrentHashMap做了相关优化
* 初始size为11，扩容：newsize = olesize*2+1 ,Hashtable不要求底层数组的容量一定要为2的整数次幂
* 计算index的方法：index = (hash & 0x7FFFFFFF) % tab.length