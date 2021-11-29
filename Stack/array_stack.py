
class ArrayStack():
    """
    使用数组实现顺序栈
    """
    def __init__(self, size: int):
        self.items = [None] * size     # 数组
        self.count = 0          # 栈元素个数
        self.size = size        # 栈的大小

    def push(self, item) -> bool:
        """
        入栈操作
        :param item:
        :return:
        """
        if self.count == self.size:
            "栈满"
            return False

        # 将item放在count的位置 并且count++
        self.items[self.count] = item
        self.count += 1
        return True

    def pop(self):
        """
        出栈操作
        :return:
        """
        if self.count == 0:
            "栈空"
            return None
        "返回下标为count-1的元素,并将count-1"
        temp = self.items[self.count - 1]
        self.count -= 1
        return temp

    # 自定义输出实例化对象时的信息
    def __repr__(self):
        return str(self.items[:self.count])


if __name__ == '__main__':
    stack = ArrayStack(6)

    for i in range(5):
        print(stack)
        stack.push(i)
        # print(stack)

    print('--------------------')

    for i in range(5):
        print(stack)
        stack.pop()

    # print(stack)


