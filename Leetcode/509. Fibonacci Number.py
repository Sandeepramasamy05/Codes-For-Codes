class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = {0: 0, 1: 1}

        def fibbo(n):
            if n in a:
                return a[n]
            if n not in a:
                a[n] = fibbo(n-1) + fibbo(n-2)
            return a[n]
        return fibbo(n)
