#TC: O(n) 
#SC: O(h)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 


        self.flag = True 
        self.recur(root) 
        return self.flag 

    def recur(self, root): 

        if root == None: #base condition
            return  0 

        leftht = self.recur(root.left) #recursive call to iterate on the left subtree
        rightht = self.recur(root.right)  #recursive call to iterate on the right subtree

        if abs(leftht-rightht) > 1:  #if the difference between left height and right height is greater than 1, that means, the tree has more nodes on right than the left or vice versa, which means the tree is unbalanced
            self.flag = False #if yes, set the flag to False

        return max(leftht,rightht)+1 #everytime consider the greater height as height is calculated through breadth, and increase it by one, as it goes level by level increased
