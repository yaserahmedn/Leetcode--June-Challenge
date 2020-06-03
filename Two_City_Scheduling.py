'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference=[]
        i=0
        for cost in costs:
            difference.append((abs(cost[0]-cost[1]), i))
            i=i+1
        
        #print(difference)
        
        a=0
        b=0
        
        difference.sort(key = lambda x: x[0], reverse=True)
        #print(difference)
        minPrice=0
        n=len(costs)//2
        
        for tup in difference:
            current = costs[tup[1]]
            if current[0]<current[1] and a<n:
                a=a+1
                minPrice+=current[0]
            elif current[1]<current[0] and b<n:
                b=b+1
                minPrice+=current[1]
            elif a==n:
                minPrice+=current[1]
                b=b+1
            elif b==n:
                minPrice+=current[0]
                a=a+1
                
        return minPrice
