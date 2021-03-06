首次安装
========

同步快盘的```denchi```文件夹，
在文件夹```setup```中，双击```setup.cmd```（会弹出一个黑色的框，几十秒后，会不断滚动一些信息，不用理会，直到提示“按任意键结束”，这时关掉这个黑色的框即可）


更新网站内容
============

更新网站内容有两个步骤

**步骤1: 修改content里的内容**<br/>
**步骤2: 双击update.cmd**

步骤2可能会让你输入username和password，请输入我那天给你们的用户名和密码。

如无意外，网站会更新并自动同步到远端服务器，这时访问http://denchi.cn/ 即可看到效果。

---

content目录里有一些txt文件，所有这些文本文件构成了整个网站的内容，修改这些文件也就相当于修改网站。
一般来说，一个文件代表一个页面（navigation.txt除外）。
下面具体说明一下如何修改各类网站内容。


### 普通页面 ###
普通页面是指类似[公司概览](http://denchi.cn/cn/introduction/company/)这种页面。
一个典型的普通页面格式如下：

```
title: 公司简介
head_image: xxx.jpg

我们公司是....
blablabla
```

文件最开始会定义一些页面的属性，这些属性内容不包含在正文里。这里用```title```定义了该页面的标题，注意，```:```是半角的。
然后用```head_image```定义了该页面的顶部图像，这个图像实际指向```content/image/xxx.jpg```。
接下来空一行，再另起一行开始写页面正文，正文采用markdown语法，当然，如果只是纯文本，完全可以不管这些语法，就当普通打字录入即可。

某些文件可能属于同一栏目，这时我们可以用一个文件夹把他们装在一起，不必担心文件夹有多少或者埋藏得多深，只要在content目录内，所有的txt文件都会被程序识别并转为网页。

总结一下创建一个普通页面需要注意的地方：
* 不要漏了title属性
* 确保页面属性信息中的冒号是半角的
* 页面属性部分和正文部分需要用空行隔开

### 新闻类页面 ###
新闻类页面是指类似[敬请期待](http://denchi.cn/cn/news/hello-denchi/)这种更新较为频繁的页面。
一个典型的新闻页面格式如下：

```
title: 敬请期待
date: 2013/07/31
type: event

敬请期待
```

格式其实和普通页面差不多，只不过多了```date```属性和```type```属性。
其中```date```属性表示该新闻的时间，首页和列表页将依据这个时间对新闻列表进行排序。
而```type```属性表示该新闻属于哪种类型。
目前```type```属性可以填写的类型包括
* event
* law
* practice

总结一下创建一个新闻类页面需要注意的地方：
* 不要漏了title属性
* 确保页面属性信息中的冒号是半角的
* 需要定义date属性和type属性

### 列表页面 ###
列表页面是指类似[最新活动](http://denchi.cn/cn/list-seminar/)这种页面。
一个典型的列表页面格式如下：

```
title: 最新活动
list: event
```

文件没有正文，只有页面属性，首先是title，然后是一个list属性，这里的```list: event```表示该页将列出所有类型为```event```的新闻类页面，也就是把所有“最新活动”列出来。

总结一下创建一个普通页面需要注意的地方：
* 不要漏了title属性
* 确保页面属性信息中的冒号是半角的
* 需要定义list属性
* 不需要写正文部分



### 导航条设置 ###
导航条是指所有页面上方黑色那条东西，里面包含了网站各个页面的导航。
其对应的是cn目录和jp目录的navigation.txt，这个文件定义了网站的导航结构（也就是网页中二级导航条的内容），例如

```
公司简介:: /cn/introduction/company, /cn/introduction/group, /cn/introduction/concepts
业务概况:: /cn/service/training, /cn/service/price
/cn/list-seminar
```
表示网站有两个一级栏目，第一个栏目是“公司简介”，这个栏目有三个子栏目，分别对应了introduction目录下的company, group和concepts页面。
第二个栏目是“业务概括”，这个栏目有两个子栏目，分别对应了service目录下的training和price页面。
第三个栏目是“最新活动”，对应根目录下的list-seminar页面，“最新活动”这个栏目标题也抽取自list-seminar页面的title，这个栏目没有子栏目。

总结一下什么时候应该修改这个文件：
* 新增了一个页面，并且希望把这个页面显示在导航条中，作为一个新的栏目/子栏目
* 调整栏目/子栏目的位置
* 删除某个栏目/子栏目
* 修改了某个与导航关联的页面的文件名

在修改这个文件时，需要注意的地方如下：
* 一级栏目及其子栏目须写在同一行
* 一级栏目和子栏目之间须用```::```分隔，注意不要输入全角的冒号
* 子栏目只需要指定文件位置，不需要指定标题，程序会自动对应页面的title提取标题
* 一级栏目可以没有子栏目，这时一级栏目应该对应一个具体的页面，只需要指明这个页面的位置即可。
  例如有个“关于我们”的栏目，内容是根目录下的about页面（也就是content\cn\about），那么这一行就是```/cn/about```，注意这里没有栏目标题（程序自动提取about页面的title，也就是“关于我们”，作为这个一级栏目的标题），没有冒号，也没有子栏目。
  


关于Markdown的更多知识
======================
本网站正文均采用Markdown格式，下面列出一些常见的用法：

### 小标题 ###
在标题下加上三个以上的```-```
例如：
```
关于服务价格和服务质量
----------------------
```

### 更小的标题 ###
在标题左右加上三个```#```
例如：
```
###员工###
```

### 无序列表 ###
在每一项前面加上```*```+空格
例如：
```
* 精深的专业知识
* 商务日语的语言能力
* 对日本企业的文化有深刻理解
```

### 有序列表 ###
在每一项前面加上数字+```.```+空格
例如：
```
1. 精深的专业知识
2. 商务日语的语言能力
3. 对日本企业的文化有深刻理解
```

### 在正文中插入图片 ###
首先把图片放到content/image目录中，
然后插入```![](图片名称)```
例如：
把图片map.png放到content/image目录中，
然后在正文写上
```
![](map.png)
```

更多markdown的格式可以参考
http://wowubuntu.com/markdown/
