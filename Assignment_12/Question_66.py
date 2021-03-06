"""
Create a method that is called appendPosSum takes one parameter: 
an ArrayList of Integers and returns an ArrayList of Integers
This method should:
Create a new ArrayList of Integers
Add only the positive Integers to the new ArrayList
Sum the positive Integers in the new ArrayList and add the Sum as the last element
For example, if the incoming ArrayList contains the Integers (4,-6,3,-8,0,4,3), 
the ArrayList that gets returned should be (4,3,4,3,14), with 14 being the sum of (4,3,4,3). 
The original ArrayList should remain unchanged.
"""

def appendPosSum(arr):
    
    newArr = []
    
    for each in arr:
        if each > 0:
            newArr.append(each)
    
    newArr.append(sum(newArr))
    
    return newArr
   
#  MAIN
    
arr = [4, -6, 3, -8, 0, 4, 3]
print("\ninput   : ", arr)
print("output : ", appendPosSum(arr))