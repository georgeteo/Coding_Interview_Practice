def path(solution, maze, position, goal):
    if position == goal:
        # Print solution
        for row in solution:
            print row
        return True
    else:
        solution[position[0]][position[1]] = 1
        right_move = (position[0], position[1]+1)
        if maze[right_move[0]][right_move[1]]:
            if path(solution, maze, right_move, goal):
                return True
        else:
            # Go down instead
            down_move = (position[0]+1, position[1])
            if maze[down_move[0]][down_move[1]]:
                if path(solution, maze, down_move, goal):
                    return True
        solution[position[0]][position[1]] = 0
        return False

if __name__=="__main__":
    maze = [[1,0,0,0],[1,1,0,1], [0,1,0,0], [1,1,1,1]]
    position = (0,0)
    goal = (3,3)
    solution = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    path(solution, maze, position, goal)
