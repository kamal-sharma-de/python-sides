import random

class Solution:
   def __init__(self, n: int, blacklist: List[int]):
       self.n = n - len(blacklist)
       self.whitelist = set(range(n)) - set(blacklist)
       self.lookup = {}
       for black in blacklist:
           if black < self.n:
               self.lookup[black] = next(iter(self.whitelist))
               self.whitelist.remove(self.lookup[black])

   def pick(self) -> int:
       x = random.randint(0, self.n - 1)
       return self.lookup.get(x, x)
