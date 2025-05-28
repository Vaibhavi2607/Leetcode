class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def a(edges):
            temp={}
            nodes=0
            for u,v in edges:
                if u not in temp: temp[u]=[]
                if v not in temp: temp[v]=[]
                temp[u].append(v)
                temp[v].append(u)
                nodes=max(nodes,u,v)
            return temp,nodes+1
        
        (a1,n),(a2,m)=a(edges1),a(edges2)

        def foo(root,x,a,d,depth,mx,par):
            if depth>mx: return
            d[root].add(x)
            for c in a[x]: 
                if c==par: continue
                foo(root,c,a,d,depth+1,mx,x)

        d1,d2={i:set() for i in range(n)},{i:set() for i in range(m)}
        for i in range(n): foo(i,i,a1,d1,0,k,-1)
        for i in range(m): foo(i,i,a2,d2,0,k-1,-1)

        for k in d1: d1[k]=len(d1[k])
        for k in d2: d2[k]=len(d2[k])

        d2mx=max(d2.values())

        return list(d1[i]+d2mx for i in range(n))