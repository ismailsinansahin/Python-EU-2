"""
A pizza delivery man has a scooter and a lot of deliveries to make, 
he will have to refuel a few times. 
Refuel_times gets an ArrayList deliveries of the amount of fuel it will take to get to destinations like:
[1,3,5], first place will take 1 fuel unit to get to the second 3 fuel units etc...
the max_fuel is the max fuel units in the vehicle fuel tank.
you will need to returns how meany refuels it will take to do all deliveries 
(if the units are bigger then the tank he will refuel along the way in a gas station).
for example:
refuel_times([7,7,7],7)
returns:3 (3 fuel stops 7 units each delivery)
refuel_times([9,1],3)
returns:4 (3 fuel stops for first delivery and +1 stop for second)
refuel_times([100,200,10],10)
returns:31
"""

import math

def refuelTimes(arr):

    return  math.ceil(sum(arr[0])/arr[1])
    
#  MAIN
    
arr1 = [[7,7,7],7]
arr2 = [[9,1],3]
arr3= [[100,200,10],10]

print("\ninput   : ", arr1)
print("output :", refuelTimes(arr1))
print("\ninput   : ", arr2)
print("output :", refuelTimes(arr2))
print("\ninput   : ", arr3)
print("output :", refuelTimes(arr3))

