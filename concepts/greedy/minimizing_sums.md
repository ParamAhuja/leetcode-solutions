### Given: a set of numbers a1, a2, ... an, it could represent ath like distance, money, etc.
### Goal: minimize: |a1 − x|^c +|a2 − x|^c +··· +|an − x|^c. where, x is a any number.

#### case 1: (c = 1) The L₁ Norm (also known as the Manhattan Distance, Taxicab Norm, or Absolute Value Norm) is a mathematical metric that calculates the sum of the absolute values of a vector's components.

|a1 − x| +|a2 − x| +··· +|an − x|

**SOLUTION:** select the median of numbers to minimize deviation

*For ex:-*
nums =  [1,2,9,2,6]
take x=2 (median): 1+0+0+4+7 => 12
if x=4 (avg): 3+2+2+2+5 => 14

### case 2: c=2, The L₂ norm (also known as the Euclidean norm or Euclidean distance) measures the straight-line length of a vector from the origin. It is the most common way to calculate the magnitude of a vector in machine learning, data science, and physics.

(a1 − x)**2 + (a2 − x)**2 + ··· +(an − x)**2

**SOLUTION:** take the average of the numbers

*For ex:-*
nums =  [1,2,9,2,6]
take x=2 (median): 1+0+0+16+49 => 66
if x=4 (avg): 9+4+4+4+25 => 46

## explainiation:
for L1 norm, the sum represents effort, (such as distance, etc.) suppose the numbers in the example are ppl, they need to decide a meeting point, it HAS to be median to be closest to each, since otherwise:
- if the point is 1m to left, the total distance travelled increase by 1m as everyone on right travels 1 more meter, everyone on right one less (center guy moves 1 m too)
- vice versa for 1m to the right 
This means that the count of values given matter and not the magnitude to how much each guy individually travels
Hence, its like tug of war, to minimize DISTANCE (l1), it has to be median.

for L2 norm, the sum represents effort squared, (such as money) suppose the numbers in the example are 5 ppl connected by a bungee cord, at which point do another person stand so as to experience least net force
- deviate from mean, and the extremes on one side exert a lot of force
This means that the magnitude matters not the count.

## mathematical proof:
- derivate l1 norm i.e, sigma(|ai - x|) i= 1 to n
=> sigma(signum(a-x)) = 0
For the sum to be zero, the number of +1 should equal to number of -1
Hence, only the count matters not the magnitude

- derivate l2 norm i.e, sigma(ai) - n.x = 0
=> sigma(ai)/n = x
Hence, it should be median to minimize sum.


## CONCLUSION: 
- median: point closest to each of the given values in a 1D space X, blind to magnitude of numbers, but only cares about the count
- median minimizes L1 norm
- mean: point closest to each of the given values in a 2D space X, sensitive to extremes
- mean minimizes L2 norm

Hence, the MAE and MSE offers two different use cases:
- MAE treats every unit of error equally
- MSE is highly outlier sensitive
lasso and ridge regression works on this principle as well.