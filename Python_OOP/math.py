
class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *nums):
        for a in range (0, len(nums)):
            if type(nums[a]) == list or type(nums[a]) == tuple:
                for b in nums[a]:
                    self.total += b
            else:
                self.total += nums[a]
        return self
    
    def subtract(self, *nums):
        for a in range (0, len(nums)):
            if type(nums[a]) == list or type(nums[a]) == tuple:
                for b in nums[a]:
                    self.total -= b
            else:
                self.total -= nums[a]
        return self
    
    def result(self):
        print str(self.total) + " is total"

md = MathDojo()

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()