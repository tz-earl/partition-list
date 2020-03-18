# partition-list
Problem from Leetcode. https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes
 less than x come before nodes greater than or equal to x. You should
 preserve the original relative order of the nodes in each of the two partitions.

I came up with two very different solutions to this exercise.

Although the first solution had correct functionality, it was buggy and a bit
 difficult to understand and to be convinced of its correctness.
 
The second solution was easy to explain and to write correctly and required
 almost no debugging.
 
Both were equally performant in having O(n) runtime and negligent memory
 requirements, but the difference in clarity is striking.
 