https://www.cnblogs.com/LiaHon/p/11180869.html

LinkedHashMap可以说是HashMap和LinkedList的集合体，既使用了HashMap的数据结构，又借用了LinkedList双向链表的结构

通过注释发现该变量为true时access-order，即按访问顺序遍历，如果为false，则表示按插入顺序遍历。默认为false


LinkedHashMap使用的也较为频繁，它基于HashMap，用于HashMap的特点，又增加了双链表的结构，从而保证了顺序性，本文主要从源码的角度分析其如何保证顺序性，