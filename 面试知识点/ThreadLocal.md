# ThreadLocal 知识点 JDK1.8 https://zhuanlan.zhihu.com/p/130226698
# 1、什么是ThreadLocal
ThreadLocal 是 Java 里一种特殊变量，它是一个线程级别变量，每个线程都有一个 ThreadLocal 就是每个线程都拥有了自己独立的一个变量，
竞态条件被彻底消除了，在并发模式下是绝对安全的变量。

可以通过 ThreadLocal<T> value = new ThreadLocal<T>(); 来使用。

会自动在每一个线程上创建一个 T 的副本，副本之间彼此独立，互不影响，可以用 ThreadLocal 存储一些参数，以便在线程中多个方法中使用，用以代替方法传参的做法。

    /**
     * ThreadLocal变量，每个线程都有一个副本，互不干扰
     */
    public static final ThreadLocal<String> THREAD_LOCAL = new ThreadLocal<>();
    
# 2、ThreadLocal 内存泄漏
ThreadLocal 在没有外部强引用时，发生 GC 时会被回收，那么 ThreadLocalMap 中保存的 key 值就变成了 null，
而 Entry 又被 threadLocalMap 对象引用，threadLocalMap 对象又被 Thread 对象所引用，那么当 Thread 一直不终结的话，
value 对象就会一直存在于内存中，也就导致了内存泄漏，直至 Thread 被销毁后，才会被回收。

那么如何避免内存泄漏呢？

在使用完 ThreadLocal 变量后，需要我们手动 remove 掉，防止 ThreadLocalMap 中 Entry 一直保持对 value 的强引用，导致 value 不能被回收，

# 3、ThreadLocal 的 set 方法

set 方法的作用是把我们想要存储的 value 给保存进去。set 方法的流程主要是：

* 先获取到当前线程的引用
* 利用这个引用来获取到 ThreadLocalMap
* 如果 map 为空，则去创建一个 ThreadLocalMap
* 如果 map 不为空，就利用 ThreadLocalMap 的 set 方法将 value 添加到 map 中

# 4、ThreadLocal 的 get 方法

get 方法的主要流程为：

* 先获取到当前线程的引用
* 获取当前线程内部的 ThreadLocalMap
* 如果 map 存在，则获取当前 ThreadLocal 对应的 value 值
* 如果 map 不存在或者找不到 value 值，则调用 setInitialValue() 进行初始化

# 5、ThreadLocal 的 rehash 方法

* setThreshold(INITIAL_CAPACITY);//源码,初始容量是16，threshold = len * 2 / 3; 16*2/3=10
* expungeStaleEntries() 删除表中所有过时的条目,即key为null的。
* if (size >= threshold - threshold / 4) 就扩容 10-10/4=8，在清理过期Entery后如果长度大于等于8，则进行扩容，

# 6、ThreadLocal 的 resize 方法
* int newLen = oldLen * 2;如果长度是8，则会扩容到16，到原来的2倍
* setThreshold(newLen) 新的threshold是新长度的2/3
* 2/3 * 3/4 = 1/2 即长度大于等于原长度的1/2时，会扩容到原来的2倍
* 在清理过期Entery后如果长度大于等于原长度的2/3时会进行rehash，再次清理过期Entery后如果长度大于等于原长度的1/2时会进行扩容。

# 7、ThreadLocal 应用场景
ThreadLocal 的特性也导致了应用场景比较广泛，主要的应用场景如下：

* 线程间数据隔离，各线程的 ThreadLocal 互不影响
* 方便同一个线程使用某一对象，避免不必要的参数传递
* 全链路追踪中的 traceId 或者流程引擎中上下文的传递一般采用 ThreadLocal
* Spring 事务管理器采用了 ThreadLocal-https://www.zhihu.com/question/341005993
    Spring采用Threadlocal的方式，来保证单个线程中的数据库操作使用的是同一个数据库连接，同时，采用这种方式可以使业务层使用事务时不需要感知并管理connection对象，通过传播级别，巧妙地管理多个事务配置之间的切换，挂起和恢复。
* Spring MVC 的 RequestContextHolder 的实现使用了 ThreadLocal


Thread是以时间换空间的方式，而ThreadLocal是以空间换时间的方式，

如果我想共享线程的ThreadLocal数据怎么办？
* 使用InheritableThreadLocal可以实现多个线程访问ThreadLocal的值，我们在主线程中创建一个InheritableThreadLocal的实例，然后在子线程中得到这个InheritableThreadLocal实例设置的值。
```text
final ThreadLocal threadLocal = new InheritableThreadLocal();       
threadLocal.set("帅得一匹");    
Thread t = new Thread() {        
    @Override        
    public void run() {            
      super.run();            
      Log.i( "张三帅么 =" + threadLocal.get());        
    }    
  };          
  t.start();
```

那为什么ThreadLocalMap的key要设计成弱引用？

* key不设置成弱引用的话就会造成和entry中value一样内存泄漏的场景。补充一点：ThreadLocal的不足，我觉得可以通过看看netty的fastThreadLocal来弥补，大家有兴趣可以康康。


如何解决哈希冲突？
 ThreadLocalMap 类的底层数据结构是一个 Entry 类型的数组
 基于斐波那契散列法获取当前 ThreadLocal 对象的散列值之后进入了一个循环，在循环中是处理具体处理哈希冲突的方法：
     如果散列值已存在且 key 为同一个对象，直接更新 value
    如果散列值已存在但 key 不是同一个对象，尝试在下一个空的位置进行存储
    
所以，来总结一下 ThreadLocal 处理哈希冲突的方式就是：
**如果在 set 时遇到哈希冲突，ThreadLocal 会通过线性探测法尝试在数组下一个索引位置进行存储，
同时在 set 过程中 ThreadLocal 会释放 key 为 NULL，
value 不为 NULL 的脏 Entry对象的 value 属性来防止内存泄漏 **。