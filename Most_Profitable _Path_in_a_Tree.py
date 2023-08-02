class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist,parents={},{}

        def find_dist_and_parent_from_alice(u,parent,d):
            parents[u]=parent
            dist[u]=d
            for v in graph[u]:
                if v!=parent:
                    find_dist_and_parent_from_alice(v,u,d+1)

        def find_maximum_profit_from_alice(u,parent):
            res=float('-inf')
            for v in graph[u]:
                if v!=parent:
                    res=max(res,find_maximum_profit_from_alice(v,u))

            if not res>float('-inf'):
                res=0

            return amount[u]+res

        def update_amount_from_bob(curr,d):
            while curr!=0:
                if d<dist[curr]:
                    amount[curr]=0
                elif d==dist[curr]:
                    amount[curr]//=2
                
                curr=parents[curr]
                d+=1

        find_dist_and_parent_from_alice(0,0,0)
        update_amount_from_bob(bob,0)
        return find_maximum_profit_from_alice(0,0)
