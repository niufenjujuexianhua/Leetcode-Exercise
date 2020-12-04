# Given two sequences pushed and popped with distinct values, return true if and
#  only if this could have been the result of a sequence of push and pop operation
# s on an initially empty stack. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#  
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed is a permutation of popped. 
#  pushed and popped have distinct values. 
#  
#  Related Topics Stack 
#  👍 1173 👎 32


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
        """
        st = []
        i = 0
        for n in pushed:
            st.append(n)
            while st and st[-1] == popped[i]:
                i += 1
                st.pop()

        return i == len(popped)
# print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
# leetcode submit region end(Prohibit modification and deletion)