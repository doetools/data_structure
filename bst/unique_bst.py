class Solution(object):
    def __init__(self):
        self.ht = {}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # use dynamic programming

        # create a list of 20 members, as n <=19
        dp = [0] * (20)
        dp[0] = 1  # if no node, that is one form
        dp[1] = 1  # if one node, one form
        dp[2] = 2  # if two nodes, two possible forms

        # if n >= 3
        for i in range(3, n+1):
            # since the n value is at the head, so decrement by 1
            total = j = i - 1
            # the initial value for dp[n]
            num = 0
            # enumerate through all possible forms
            # for example, if n = 5
            # the possible forms are
            """
                left right
            1.  4    0
            2.  3    1
            3.  2    2

            """
            while (j >= 1):
                diff = total - j

                if j < diff:
                    break

                if (diff == j):
                    num += dp[diff]**2

                else:
                    num += (dp[j] * dp[diff])*2

                j -= 1

            # update dp[n]
            dp[i] = num

        return dp[n]

s = Solution()
print(s.numTrees(5))