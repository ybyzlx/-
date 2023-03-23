import numpy as np


# 方法1：递归法

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


#
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


#
#
# def find_path(maze, pos, end):
#     dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
#     mark(maze, pos)
#     if pos == end:
#         return True
#     for i in range(4):
#         nextp = [dirs[i][0] + pos[0],dirs[i][1] + pos[1]]
#         if passable(maze, nextp):
#             print(nextp)
#             if find_path(maze, nextp, end):
#                 return True


# 方法2：回溯和栈

def find_path(maze, pos, end):
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
    if pos == end:
        return
    st = []
    mark(maze, pos)
    st.append((pos, 0))
    while st is not None:
        print(st)
        pos, nxt = st.pop(-1)

        for i in range(nxt, 4):
            nextp = [pos[0] + dir[i][0], pos[1] + dir[i][1]]
            if nextp == end:
                return True
            if passable(maze, nextp):
                st.append((pos, i+1))
                mark(maze, nextp)
                st.append((nextp, 0))
                break
    return False


maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]

start = [1, 1]
end = [1, 4]
#
print(find_path(maze, start, end))
