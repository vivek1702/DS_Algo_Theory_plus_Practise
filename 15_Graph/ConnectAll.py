def __getPathBFS(self, sv, ev, visited):
        mapp = {}
        q = queue.Queue()

        if self.adjMatrix[sv][ev] == 1 and sv == ev:
            ans = []
            ans.append(sv)
            return ans

        q.put(sv)
        visited[sv] = True

        while q.empty() is False:
            front = q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[sv][i] == 1 and visited[i] is False:
                    mapp[i] = front
                    q.put(i)

                    visited[i] = True

                    if i == ev:
                        ans = []
                        ans.append(ev)
                        value = mapp(ev)

                        while value != sv:
                            ans.append(value)
                            value = mapp[value]

                        ans.append(value)
                        return ans
        
        return []


def getPathBFS(self, sv, ev):
    visited=[False for i in range(self.nVertices)]
    return self.__getPathBFS(sv, ev, visited)



def dfs(self, sv, visited):
    visited[sv] = True

    for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                self.dfs(i,visited)
                visited[i] = True


def isConnected(self):
    visited=[False for i in range(self.nVertices)]
    self.dfs(0, visited)

    for boolVal in visited:
        if not boolVal:
            return False

    return True


li = stdin.readline().strip().split() 
V=int(li[0])
E=int(li[1])
if V==0:
    print('true')
else:
    g=Graph(V)
    for i in range(E):
        arr = stdin.readline().strip().split()
        fv = int(arr[0])
        sv = int(arr[1])
        g.addEdge(fv, sv)

    print()
    if g.isConnected():
        print('true')
    else:
        print('false')
