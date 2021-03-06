/*
Find the path with the maximum sum in a given binary tree. 
Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes 
and doesn’t necessarily pass through the root. The path must contain at least one node.
*/

#include <iostream>
#include <limits>

using namespace std;

class TreeNode {
 public:
  int val;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int x) {
    val = x;
    left = right = nullptr;
  }
};

class MaximumPathSum {
public:
    static int findMaximumPathSum(TreeNode* root){
        int maxSum = numeric_limits<int>::min();
        calculatePathSum(root, maxSum);
        return maxSum;
    }
private:
    static int calculatePathSum(TreeNode* currNode, int &maxSum){
        if (currNode == nullptr){
            return 0;
        }

        int leftTreeSum = calculatePathSum(currNode->left, maxSum);
        int rightTreeSum = calculatePathSum(currNode->right, maxSum);

        leftTreeSum = max(leftTreeSum, 0);
        rightTreeSum = max(rightTreeSum, 0);

        int currSum = leftTreeSum + rightTreeSum + currNode->val;   
        maxSum = max(currSum, maxSum);

        return max(leftTreeSum, rightTreeSum) + currNode->val;
    }
};

int main(int argc, char *argv[]) {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  cout << "Maximum Path Sum: " << MaximumPathSum::findMaximumPathSum(root) << endl;
  
  root->left->left = new TreeNode(1);
  root->left->right = new TreeNode(3);
  root->right->left = new TreeNode(5);
  root->right->right = new TreeNode(6);
  root->right->left->left = new TreeNode(7);
  root->right->left->right = new TreeNode(8);
  root->right->right->left = new TreeNode(9);
  cout << "Maximum Path Sum: " << MaximumPathSum::findMaximumPathSum(root) << endl;
  
  root = new TreeNode(-1);
  root->left = new TreeNode(-3);
  cout << "Maximum Path Sum: " << MaximumPathSum::findMaximumPathSum(root) << endl;
}
