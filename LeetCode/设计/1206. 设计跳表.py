# 跳跃表节点的类
import random


class SNode:

    def __init__(self, key=None, value=None):
        # 键
        self.key = key
        # index表示数组中最末的元素
        self.maxIndex = -1
        # link使用一个数组  存放全部下节点的索引  link[i]表示第i层的索引
        self.link = []
        self.value = value


class SkipList:
    def __init__(self, size=8, larger=65535):
        # 深度
        self.size = size
        '''
        跳跃表的深度和你的数据有关  大约为 log n   
        '''
        # 尾节点指针
        self.tial = SNode()
        # 头结点指针   存放头结点
        self.head = SNode()
        # 存放在插入和删除操作中  每一个链上遇到的最后节点
        self.last = []
        self.tial.key = larger  # 表示尾节点

        self.head.key = -65535  # 表示节点

        # 头结点的全部指针指向尾节点
        for i in range(self.size):
            self.head.link.append(self.tial)

        self.MAX_RAND = self.size

    # 随机分配层数  但是不会超过最大层数
    def randomDispenseLevel(self):
        level = 1
        while random.randint(0, 1) == 1:
            level += 1
        return level if level <= self.MAX_RAND else self.MAX_RAND

    # 获取last数组里的值
    def getLast(self, data):
        # print(data)
        num = self.size - 1  # 数组存储时是自底向上    查找是自顶向下   所以num表示层数
        p = self.head
        while num >= 0:
            while p.link[num].key < data:  # 和进行一次查找一样 如果小于，说明这个节点是待动态操作节点的前一个节点
                p = p.link[num]
            num -= 1
            self.last.append(p if p else self.head)  # 如果节点不是空就加入last里

        return self.last[len(self.last) - 1]  # p指向最底层的节点

    def find(self, data):
        FLAGE = False  # 标准位   查询是否成功
        temp = self.head  # temp开始存放头指针
        i = self.size - 1  # i是最大长度-1   因为是从上往下找
        while i >= 0:  # 如果没有越界
            if temp.link[i].key == self.tial.key:  # 如果到达最后的尾指针 说明当前层没有要找的节点
                i -= 1
                continue
            if temp.link[i].key < data:  # 如果小于待查找的数据  说明要将节点切换到下一个节点
                temp = temp.link[i]
                i = len(temp.link) - 1

            elif temp.link[i].key == data:  # 如果相等说明找到了
                FLAGE = True
                return temp.link[i], FLAGE

            else:
                if i > 0:  # 如果没找到  切没有到最后一层  直接下降一层

                    i -= 1
                else:
                    return temp, FLAGE
        return temp, FLAGE

    def insert(self, key, value=None):
        '''
        插入的方法
        :param key: 待插入数据的 键值对
        :return:    true  or false
        '''

        curNode = self.getLast(key)  # 获取last数组的值

        if curNode.key != key:  # flag为false说明没有相同元素
            # 获得层数
            lev = self.randomDispenseLevel()
            # 构造一个新节点
            newNode = SNode(key, value)

            count = self.size - 1  # 控制节点的变化
            num = 0  # 控制节点里面数组的具体号
            '''
                为什么count是从大到小  num是从小到大
                因为查找是从上往下  所以last数组存放是从上往下 
                但是每个节点的link数组存放节点对象是从下往上        
    
            '''
            while num <= lev - 1:
                length = len(self.last[count].link) - 1  # 获取不同的节点link数组长度

                while num <= length:
                    if num > lev - 1:
                        break
                    newNode.link.append(self.last[count].link[num])  # 插入新节点 last里的节点指向new节点
                    self.last[count].link[num] = newNode  # 新节点变成last里元素的下一个节点
                    num += 1
                count -= 1  # 节点切换

            self.last = []  # 必须插入一次后必须将last重新变为空  因为list的append方法会不断添加新的元素
            return True
        return False

    def remove(self, key):
        '''
        删除的思路

        先进行一次find  如果存在就删除

        先获得last数组

        然后进行删除

        :param key: 待删除数据的键
        :return:
        '''
        temp, flag = self.find(key)
        if flag:  # 如果存在这个键

            self.getLast(key)  # 获取last数组的值
            length = len(temp.link) - 1  # 获取待删除数组键的长度
            count = self.size - 1  # 控制last数组里节点的变化
            num = 0  # 6控制待删除节点里面数组的具体号

            while num <= length:
                self.last[count].link[num] = temp.link[num]
                num += 1
                count -= 1
            self.last = []  # 必须插入一次后必须将last重新变为空  因为list的append方法会不断添加新的元素
            return True
        return False

        # 顺序输出跳跃表

    def outpute(self):
        i = self.size - 1
        while i >= 0:
            # i是最大长度-1   因为是从上往下找
            p = self.head
            if p.link == None or p.link[i].key == self.tial.key:  # 如果到达最后的尾指针 说明当前层没有要找的节点
                print('head----->tial')
                i -= 1
                continue
            else:
                print('head', end='--->')
                while True:
                    if p.link == None or p.link[i].key == self.tial.key:
                        break
                    print(p.link[i].key, end='--->')
                    p = p.link[i]
                print('tail')
            i -= 1


if __name__ == '__main__':
    s = SkipList(size=5)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in x:
        s.insert(i, i)
        s.outpute()
    import sys
    sys.exit(0)
    print('最开始的情况')
    s.outpute()
    print('删除4')
    print(s.remove(4))
    s.outpute()
    print('插入4')
    print(s.insert(4))
    s.outpute()
    print('删除3')
    print(s.remove(3))
    s.outpute()
    print('删除5')
    print(s.remove(5))
    s.outpute()
    print('删除1')
    print(s.remove(1))
    s.outpute()
