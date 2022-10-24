

#TC: O(n) 
#SC: O(h)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:



        self.maximum = root.val #initially the max is set to root.val
        self.recur(root) 
        return self.maximum 

    def recur(self,root): 

        if root == None: #base condition
            return 0 

        leftsum = max(self.recur(root.left), 0) #leftsum is going to be the maximum between choose or no choose
        rightsum = max(self.recur(root.right),0) #rightsum is going to be the maximum between choose or no choose

        rootmax = root.val + leftsum + rightsum #rootmax is the sum of right left and rroot

        if rootmax > self.maximum: #check and update accordingly with global maximum
            self.maximum = rootmax 

        return root.val + max(leftsum, rightsum) #now at every recursion, we need to return the max of left sum, right sum with addition to root.val