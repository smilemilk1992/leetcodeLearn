1、hashset 底层就是hashmap ，

HashSet集合特点

 

● HashSet底层是HashMap

 

● 向Hashset中添加元素, 实际上是把这个元素作为键添加到底层的HashMap中

 

● HashSet实际上就是底层HashMap的键的集合

● 保证 唯一性
    需要重写自定义类的hashCode()和equals( )两个方法来达到元素的唯一性保证。
方法重写之后，执行的顺序：
    如果元素的hashCode值相同，才会使用equals()方法进行判断。
    如果元素的hashCode值不同，不会调用equals()方法。
自定义对象，一定要重写hashCode和equals两个方法


结论：

[1]. HashSet判断、删除和添加元素等操作依据的是被操作元素所在的类的hashCode()和equals( )这两个方法。

[2]. ArrayList做同等的操作，依据的仅仅是equals( )方法
    