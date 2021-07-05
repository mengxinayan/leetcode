# Reference link: https://leetcode-cn.com/problems/print-in-order/solution/1114-an-xu-da-yin-python3de-5chong-jie-fa-by-tuotu/

# Solution 1: Threading-Condition

import threading

class Foo:

    def __init__(self):
        self.c = threading.Condition()
        self.t = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.ans(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.ans(1, printSecond)


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.ans(2, printThird)


    def ans(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            # 参数是函数对象，返回值是bool类型
            # The parameter is a function object, and the return value is of type bool
            self.c.wait_for(lambda: val == self.t)
            func()
            self.t += 1
            self.c.notify_all()



# Solution 2: Threading-Lock

import threading

class Foo:

    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()



# Solution 3: Semaphore

import threading

class Foo:

    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()



# Solution 4: Threading-Event

import threading

class Foo:

    def __init__(self):
        self.e1 = threading.Event()
        self.e2 = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.e1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.e1.wait()
        printSecond()
        self.e2.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e2.wait()
        printThird()



# Solution 5: Barrier

import threading

class Foo:

    def __init__(self):
        self.b1 = threading.Barrier(2)
        self.b2 = threading.Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()



# Solution 6: Queue without fixed length queue

import queue

class Foo:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()



# Solution 7: Queue without fixed length queue

import queue

class Foo:

    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()

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
