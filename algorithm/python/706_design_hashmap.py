class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 2003
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    def __hash(self, key: int) -> int:
        return key % self.key_range

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket_index = self.__hash(key)
        self.bucket_array[bucket_index].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_index = self.__hash(key)
        return self.bucket_array[bucket_index].get(key)
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_index = self.__hash(key)
        self.bucket_array[bucket_index].remove(key)


class Bucket:

    def __init__(self):
        self.bucket = []
    
    def update(self, key: int, value: int) -> None:
        founded = False
        for i, k_v in enumerate(self.bucket):
            if key == k_v[0]:
                founded = True
                self.bucket[i] = (key, value)
                break
        if founded == False:
            self.bucket.append( (key, value) )

    def get(self, key: int) -> int:
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, k_v in enumerate(self.bucket):
            if key == k_v[0]:
                del self.bucket[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

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
