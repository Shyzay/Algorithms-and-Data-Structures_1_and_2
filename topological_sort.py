#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emman
#
# Created:     12/09/2018
# Copyright:   (c) Emman 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Depth first search function

def iterative_dfs(graph, start):
    seen = set()
    path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            path.append(v)
            q.extend(graph[v]) # this will add the nodes in a slightly different order
                               # for the same order, use reversed(graph[v])

    return path
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}

print(iterative_dfs(graph, 'a'))



# Modification to do a topological sort

def iterative_topological_sort(graph, start):
    seen = set()
    stack = []
    order = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) # no need to append to path any more
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   # new return value!

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}
print(iterative_topological_sort(graph, 'a'))