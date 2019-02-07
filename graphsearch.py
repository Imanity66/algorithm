# -*- coding: utf-8 -*-

BFS(graph, s):
    frontier = [s]
    marked = set(s)

    while frontier:
        next = []
        for u in frontier:
            for v in neighbors(u):
                if v not in marked:
                    next.append(v)
                    marked.add(v)
        frontier = next


zigzag问题

def solve(root):
    frontier = [root]
    res = []
    reverse = False
    while frontier:
        next = []
        curr = []
        for u in frontier:
            curr.append(u.val)
            if u.left:
                next.append(u.left)
            if u.right:
                next.append(u.right)
        res.append(curr[::-1] if reverse else curr)
        frontier = next
        reverse = not reverse
    return res


岛屿问题
BFS(grid, r, c, marked):
    frontier = [(r,c)]
    marked.add((r,c))
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    while frontier:
        next = []
        for r,c in frontier:
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0 <= nr < len(grid) and 0 <= nc <len(grid[0]) and grid[nr][nc] == '1'\
                and (nr, nc) not in marked:
                    node = (nr, nc)
                    next.append(node)
                    marked.add(node)
        frontier = next

class solution(object):
    def numIslands(self, grid):
        res, marked = 0, set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in marked:
                    res += 1
                    BFS(grid, r, c, marked)
        return res

import string
class solution(object):
    def ladderLength(self, beginWord, endWord, wordlist):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        ans = 1
        frontier = [beginWord]
        marked= set(frontier)


    while frontier:
        next = []
        for word in frontier:
            for p in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:p] + c + word[p+1:]
                    if newWord == endWord:
                        return ans + 1
                    if newWord in wordList and newWord not in marked:
                        next.append(newWord)
                        marked.add(newWord)
        frontier = next
        ans += 1
    return 0

找最近的门
第四题复杂度
找0是 mn
做一次BFS 是 mn
一共mn
class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms:
            return

    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    frontier , INF = [(r,c) for r in range(N) for c in range(C) if rooms[r][c] == 0], 2147483647
    distance = 0
    while frontier:
        next = []
        for r,c in frontier:
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0 <= nr < len(rooms) and 0 <= nc <len(rooms[0]) and rooms[nr][nc] == INF:
                    rooms[nr][nc] == distance + 1
                    next.append((nr, nc))
        frontier = next
        distance += 1
        
        
DFS(graph, visited, s):
    for u in graph.neighbors:
        if u not in visited:
            visited.add(u)
            dfs(graph, visited, u)
DFS_ALL(graph):
visited = set()      
            
for v in graph:
    if v not in visited:
        visited.add(v)
        dfs(graph, visited, v)
        
        
from collections import defaultdict
无向图
def has_cycle(graph, visited, parent, u):
    visited.add(u)
    for v in graph[u]:
        if v! = parent:
            if v in visited or has_cycle(graph, visited, u, v):
                return True
    return False

class solution(object):
    def validTree(self, n, edges):
        visited = set()
        graph = defaultdict(lambda: list())
        for edge in edges:
            graph[edge[0]].append(edge[1])#edge是一个点对 （1，2） （0，1）
            graph[edge[1]].append(edge[0])
        return not has_cycle(graph, visited, -1, 0) and len(visited) == n
    
有向图
visiting 指向 visiting 就GG
    
    
def dfs(diriected_graph, visit_status, u):
    # 0 表示 visitsing
    # 1 表示 finished
    visit_status[u] = 0
    for v in directed_graph[u]:
        if v not in visit_status:
           if dfs(directed_graph, visit_status, v):
               return True
        elif visit_status[v] == 0:
            return True
    visit_status[u] == 1:
        return False

def has_cycle(directed_graph):
    visit_status = {}
    for v in directed_graph:
        if v not in visit_status and dfs(directed_graph, visit_status, v):
            return True
    return False
    
def can_color(graph, colors, u, color):
    colors[u] = color
    for v in graph[u]:
        if colors[v] == color or (not colors[v] and not can_color(graph, colors, v, -color):
            return False
    return True

class solution(object):
    def isBipartite(self, graph):
        colors = [0] * len(graph)
        for v in range(len(graph)):
            if not colors[v] and not can_color(graph, colors, v, 1):
                return False
        return True
        


选课题
from collections import defualtdict

class solution(object):
    def findorder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        courses = []
        visited = [-1]* numCourses
def dfs(u):
    visited[u] = 0
    for v in graph[u]:
        if visited[v] == 0 or (visited[v] == -1 and not dfs(v)):
            return False
    visited[u] = 1
    courses.append(u)
    return True
for u in range(numCourses):
    if visited[u] == -1 and not dfs(u):
        return []
return courses

        
    
    