class node:#node for adjacency list
    def __init__(self,dist=0,wght=0):
        self.dist=dist
        self.wght=wght
class qnode:#queue node
    def __init__(self,vertex=0,distv=float('inf')):
        self.vertex=vertex
        self.dist=dist
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for i in range(0,len(times)):
            newnode=node(times[i][1],times[i][2])
            adj[times[i][0]].append(newnode)
        qn=qnode(k,0)
        q=[]
        q.append(qn)
        distance=[float('inf')]*(n+1)
        distance[k]=0
        time=0
        while q:
            curr=q[0]
            q.pop()
            for i in adj[curr.vertex]:
                print(type(i))
                temp_qn=qnode(i.dist,i.wght+curr.dist)
                if (distance[temp_qn.vertex]>temp_qn.dist):
                    q.append(temp_qn)
                    distance[temp_qn.vertex]=it.wght+curr.dist
                
        for i in range(1,n+1):
            if distance[i]==float('inf'):
                return -1
            time=max(time,distance[i])
        return time