class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def foo(k):
            diff=[0 for i in range(len(nums)+1)]
            for i,j,val in queries[:k]:
                diff[i]-=val
                diff[j+1]+=val
            curr=0
            for x,y in zip(nums,diff):
                curr+=y
                if curr+x>0: return False
            return True
        l,r=0,len(queries)
        while l<r:
            mid=(l+r)//2
            if foo(mid): r=mid
            else: l=mid+1
        return l if l<=len(queries) and foo(l) else -1