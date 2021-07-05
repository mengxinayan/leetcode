# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n'|sort|uniq -c |sort -r|awk '{print $2" "$1}'

# cat ——浏览文件
# tr -s ——替换字符串（空格换为换行）保证了一行一个单词
# sort ——默认ASCII值排序，排序号后还会有重复
# uniq —— 去重，-c再输出重复次数。结果就是 ”4 abc“ abc出现了4次
# sort -r —— 反向排序，也就是从大到小。得到按频率高低的结果
# awk ——格式化输出，规定输出是先字符串再重复次数，所以先$2再$1，中间空格分隔

# This is my personal record of solving Leetcode Problems. 
# If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
# Copyright (C) 2020  mengxinayan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.