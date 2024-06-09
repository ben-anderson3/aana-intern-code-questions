# Question 3
### Algorithmic Questions (Pseudocode):
**Question:** Write a function that takes a sorted array of integers and a target sum. The function should find two numbers in the array that add up to the target sum and return their indices. Assume there is exactly one solution.
```
def target_sum(l, target):
    for i in range(0, len(l)):
        j = target - l[i]
        if j in l: 
            return [i, l.index(j)]
        
    
```