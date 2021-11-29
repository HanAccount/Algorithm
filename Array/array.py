"""
    包装list的简单数组，支持插入、删除、按照下标随机访问操作
"""
class array():
    def __init__(self, capacity: int = 10):
        self._capacity = capacity
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def __repr__(self):
        return str(self._data)


    def find(self, index: int) -> object:
        """
            根据索引返回数组的元素并返回
            input: index数组下标
            return:1) 如果查找成功返回对应元素
                   2) 如果索引越界，则提示False
        """
        if (index < 0) or (index >= len(self)):
            return -1

        return self._data[index]


    def delete(self, index: int) -> bool:
        """
            根据索引删除数组的元素
            input: index数组下标
            return:1) 如果删除成功返回True
                   2) 如果删除失败返回False
        """
        if index < 0 or index >= len(self):
            return False
        self._data.pop(index)
        return True

    def insert(self, index: int, value: int) -> bool:
        """

        :param index:插入的位置
        :param value:插入的值
        :return:是否插入成功
        """
        if index < 0 or index >= self._capacity:
            return False
        self._data.insert(index,value)
        return True


if __name__ == '__main__':
    listA = array(4)
    listA.insert(0, 1)
    listA.insert(0, 2)
    listA.insert(1, 3)
    listA.insert(2, 4)
    listA.insert(1,5)

    print(listA)
    print(listA.find(3))
    listA.delete(0)
    print(listA)

        