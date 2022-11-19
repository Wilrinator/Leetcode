def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
        ans=[]
        people.sort(key= lambda x: (-x[0],x[1]))
        print(people)
        for item in people:
            print(item)
            ans.insert(item[1],item)
            print(ans)
        return ans





def reconstructQueue2(people: list[list[int]]) -> list[list[int]]:
    n, i = len(people), 0
    if n == 1:
        return people
    people.sort()
    Ans, Count = [0] * n, list(range(n))
    for i in range(n):        
        for j in range(0, n):
            if people[i][0] != people[i-j][0]:                   
                break
            else:
                continue
        Ans[Count[people[i][1]-j+1]] = people[i]
        del Count[people[i][1]-j+1]
        print(Ans, Count, i ,j)
    return Ans


print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))