def solve(gas, cost, n):
    sumGas = 0
    sumCost = 0
    start = 0
    tank = 0

    for i in range(n):
        print i 
        sumGas += gas[i]
        sumCost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i+1
            tank = 0

    if sumGas < sumCost:
        return -1

    return start

if __name__=="__main__":
    gas = [1,2,3,4,3,4]
    cost = [2,1,3,7, 3,4]
    print solve(gas, cost, 6)
