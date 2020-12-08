# Write your MySQL query statement below
select distinct id,
    sum(IF(month="Jan",revenue,null)) as Jan_Revenue,
    sum(IF(month="Feb",revenue,null)) as Feb_Revenue,
    sum(IF(month="Mar",revenue,null)) as Mar_Revenue,
    sum(IF(month="Apr",revenue,null)) as Apr_Revenue,
    sum(IF(month="May",revenue,null)) as May_Revenue,
    sum(IF(month="Jun",revenue,null)) as Jun_Revenue,
    sum(IF(month="Jul",revenue,null)) as Jul_Revenue,
    sum(IF(month="Aug",revenue,null)) as Aug_Revenue,
    sum(IF(month="Sep",revenue,null)) as Sep_Revenue,
    sum(IF(month="Oct",revenue,null)) as Oct_Revenue,
    sum(IF(month="Nov",revenue,null)) as Nov_Revenue,
    sum(IF(month="Dec",revenue,null)) as Dec_Revenue
    from Department group by id order by id;

/*
 * This is my personal record of solving Leetcode Problems. 
 * If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
 * Copyright (C) 2020  mengxinayan

 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
