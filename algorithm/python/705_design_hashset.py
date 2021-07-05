class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 1007
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    def __hash(self, key: int) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self.__hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self.__hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket_index = self.__hash(key)
        return self.bucket_array[bucket_index].is_exist(key)


class Node:

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, new_value: int) -> None:
        if self.is_exist(new_value) == False:
            new_node = Node(new_value, self.head.next)
            self.head.next = new_node

    def delete(self, value: int) -> None:
        prev = self.head
        curr = self.head.next
        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                break
            else:
                prev = curr
                curr = curr.next

    def is_exist(self, value: int) -> bool:
        curr = self.head.next
        while curr != None:
            if curr.value == value:
                return True
            else:
                curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
