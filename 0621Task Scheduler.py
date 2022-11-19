def leastInterval(tasks: list[str], n: int) -> int:
    tsk = dict()
    for i in tasks:
        if i not in tsk:
            tsk[i] = 1
        else:
            tsk[i] += 1
    
    Task = sorted(list(tsk.values()))
    count = 0        
    while Task:
            print(Task, count)
            if len(Task) > n:
                for i in range(len(Task)):
                    Task[i] -=1
                    count +=1
                    if i == n:
                        break
            else:
                temp = n-len(Task)+1
                for i in range(len(Task)):
                    Task[i] -=1
                    count +=1
                Task = [i for i in Task if i != 0]
                if Task == []: 
                    return count
                else:
                    count += temp
                
            Task = [i for i in Task if i != 0]
    return count
    
    
print(leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))