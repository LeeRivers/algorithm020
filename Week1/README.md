# 【学习笔记】Week-01

## 一，学习心得

还么有适应节奏，已经过去了三周，这才来补第一周的作业。

不得不说，超哥的由浅入深的讲解进一步加深了我对这些基本数据结构之间关联的认识，收获颇多。

常读常新，温故知新，诚不我欺



## 二，Queue 接口笔记

## 2.1 Queue 源码分析

1. 继承自Collection接口，本身也只是个接口。
2. 常见方法
   - boolean add(E e);
   - boolean offer(E e);
   - E remove();
   - E poll();
   - E element();
   - E peek();
3. 实现类
   - ArrayBlockingQueue
   - ConcurrentLinkedQueue
   - PriorityBlockingQueue
   - DelayQueue<E,extends,Delayed>
   - LinkedBlockingQueue
   - SynchronousQueue