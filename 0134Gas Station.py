def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n, ans, Ans = len(gas), 0, 0
    if sum(gas) < sum(cost):
        return -1
    if n == 1:
        return 0
    for i in range(n):
        ans += gas[i] - cost[i]
        if ans < 0:
            ans = 0
            Ans = i + 1
    return Ans



def canCompleteCircuit2(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    if sum(gas) < sum(cost):
        return -1
    if n == 1:
        return 0
    gas.extend(gas)
    cost.extend(cost)
    for i in range(n):
        if gas[i] > cost[i]:
            if i == n - 1:
                return i
            ans = 0
            for j in range(n):
                ans += gas[i + j] - cost[i + j]
                if ans < 0:
                    break
                if j == n - 1:
                    return i
    return -1



print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(canCompleteCircuit([5,8,2,8],[6,5,6,6]))