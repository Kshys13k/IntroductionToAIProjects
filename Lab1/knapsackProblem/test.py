from KnapsackProblem import KnapsackProblem

prices=[16,8,9,6,5,7,12,1,7,11,3,1,4,11,13,7]
weights=[8,3,5,2,6,3,2,2,3,3,2,1,1,9,4,5]
maxWeight=21
items=[prices,weights]
kp= KnapsackProblem(items, maxWeight)
kp.algorithm2()