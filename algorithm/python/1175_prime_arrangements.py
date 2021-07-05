class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def number_of_prime(n: int) -> int:
            not_prime_set = {1}
            prime_set = set()
            for i in range(2, n+1):
                if i not in not_prime_set:
                    prime_set.add(i)
                    j = 2
                    while i * j <= n:
                        not_prime_set.add(i*j)
                        j += 1
            return len(prime_set)

        def cal_factorial(n: int) -> int:
            ans = 1
            for i in range(1, n+1):
                ans *= i
            return ans

        num_of_prime = number_of_prime(n)
        return (cal_factorial(num_of_prime) * cal_factorial(n-num_of_prime)) % (10**9 + 7)

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
