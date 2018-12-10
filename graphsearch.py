# -*- coding: utf-8 -*-

BFS(graph, s):
    frontier = [s]
    has_seen = set(s)
    
    while frontier:
        next = []
        for u in frontier:
            for v in neighbors(u):
                if v not in has_seen:
                    next.append(v)
                    has_seen.add(v)
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
