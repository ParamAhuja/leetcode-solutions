### given a set of coins, we must find a way to make a sum x in minimum number of coins
For ex:
- coins = {1, 2, 5, 10, 20, 50, 100, 200}
- x = 520 => x = 200+200+100+20

**SOLUTION**
choose the max coins as many as possible

*NOTE:* 
We can only apply greedy for optimal solution, if the set of coins follow the conditions, otherwise DP must me used:

First, each coin 1, 5, 10, 50 and 100 appears at most once in an optimal solution, because if the solution would contain two such coins, we could replace them by one coin and obtain a better solution. For example, if the solution would contain coins 5+5, we could replace them by coin 10. In the same way, coins 2 and 20 appear at most twice in an optimal  solution, because we could replace coins 2+2+2 by coins 5+1 and coins 20+20+20 by coins 50 + 10. Moreover, an optimal solution cannot contain coins 2 + 2 + 1 or 20+20+10, because we could replace them by coins 5 and 50. 


**CODE:**
```python
coins = [1, 2, 5, 10, 20, 50, 100, 200]
x = 520

ans = 0 # store number of coins needed, use an array if exact coins are needed.
for i in range(len(coins)-1, -1, -1):
    coin_used = x//coins[i]
    x %= coins[i]
    ans+=coin_used
    if x == 0:
        break
print(ans) 
```