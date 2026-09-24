#### Q1: we are given n tasks with **durations and deadlines** and our task is to choose an order to perform the tasks. For each task, we **earn d-x points** where d is the task’s deadline and x is the moment when we finish the task. What is the largest possible total score we can obtain?
*NOTE:* in this problem, task cab be done after deadline as well
- for ex:
duration = [4, 3, 2, 4]
deadline = [2, 5, 7, 5]

**SOLUTION:**
The one algo which always gives an optimal solution is that: choose in ascending order of duration.
*explaination:*
of the two factors that affect the score, d and -x, 
- d: since we can finish all tasks no matter what since it can be done after deadline. hence this is a constant.
- x: in order to minimize x, we take minimum duration tasks first.

**ANS:** total score = sum(duration) - sum(prefix sum array of sorted duration array)