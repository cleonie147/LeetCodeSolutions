class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res=[]
        max_c=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_c:
                res.append(True)
            else:
                res.append(False)
        return res
        