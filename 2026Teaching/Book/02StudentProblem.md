##  Are Brachistochrone Segments Reusable?

Three points $P_1, P_2,$ and $P_3$ lie on the same cycloid-shaped curve in a vertical plane. Assume gravity acts vertically downward and friction is negligible.

The **brachistochrone problem** asks for the curve that minimizes the travel time between the two points.

### Question

Suppose the brachistochrone path from $P_1$ to $P_3$ passes through $P_2$.

Does it follow that:

1. the portion of that path from $P_1$ to $P_2$ is the brachistochrone from $P_1$ to $P_2$?
2. the portion of that path from $P_2$ to $P_3$ is the brachistochrone from $P_2$ to $P_3$?

Explain carefully.

------

## 最速降线的曲线段可以重复使用吗？

三个点 $P_1, P_2,$ 和 $P_3$ 位于同一条摆线形曲线上，该曲线处在一个竖直平面内。假设重力竖直向下作用，并且摩擦可以忽略不计。

**最速降线问题**研究的是：在两个给定点之间，使小珠运动时间最短的曲线是什么。

### 问题

假设从 $P_1$ 到 $P_3$ 的最速降线路径经过 $P_2$。

那么是否可以推出：

1. 这条路径中从 $P_1$ 到 $P_2$ 的部分，就是从 $P_1$ 到 $P_2$ 的最速降线？
2. 这条路径中从 $P_2$ 到 $P_3$ 的部分，就是从 $P_2$ 到 $P_3$ 的最速降线？

请仔细说明理由。

## 答案

设从 $P_1$ 到 $P_3$ 的最速降线路径经过 $P_2$。

结论是：

1. **从 $P_1$ 到 $P_2$ 的那一段，是从 $P_1$ 到 $P_2$ 的最速降线。**
2. **从 $P_2$ 到 $P_3$ 的那一段，一般不是从 $P_2$ 到 $P_3$ 的最速降线。**

关键区别在于：**小珠在起点是否从静止开始**。

------

## 1. $P_1 \to P_2$ 这一段是否仍然是最速降线？

答案：**是的。**

假设从 $P_1$ 到 $P_3$ 的整条路径是最速降线，并且它经过 $P_2$。

如果从 $P_1$ 到 $P_2$ 存在另一条更快的路径，那么我们就可以：

1. 先沿着这条更快的路径从 $P_1$ 到 $P_2$；
2. 再沿着原来的路径从 $P_2$ 到 $P_3$。

这样就会得到一条从 $P_1$ 到 $P_3$ 的更快路径。

这与原来 $P_1 \to P_3$ 是最速降线相矛盾。

所以，从 $P_1$ 到 $P_2$ 的那一段也必须是最优的。

因此：

$P_1 \to P_2$

这一段是从 $P_1$ 到 $P_2$ 的最速降线。

------

## 2. $P_2 \to P_3$ 这一段是否仍然是最速降线？

答案：**一般不是。**

原因是：标准的最速降线问题要求小珠从起点**由静止开始运动**。

但是，如果小珠是先从 $P_1$ 出发，再到达 $P_2$，那么它到达 $P_2$ 时通常已经具有一定速度。

根据机械能守恒，如果 $P_2$ 比 $P_1$ 低，那么小珠在 $P_2$ 处的速度为

$v(P_2)=\sqrt{2g(y_1-y_2)},$

其中 $y$ 表示竖直向上的高度坐标。

所以，在原来的 $P_1 \to P_3$ 运动中，小珠从 $P_2$ 出发继续滑向 $P_3$ 时，并不是从静止开始，而是已经有了非零初速度。

因此，$P_2 \to P_3$ 这一段对应的是：

> 从 $P_2$ 出发，但带有从 $P_1$ 下落获得的初速度。

而标准的 $P_2 \to P_3$ 最速降线问题是：

> 从 $P_2$ 由静止开始。

这两个问题不同，所以最优路径一般也不同。

