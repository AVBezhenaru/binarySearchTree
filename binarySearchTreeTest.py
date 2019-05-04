from binarySearchTree import *

node_0 = BSTNode(0, 0, None)
node_1 = BSTNode(1, 1, None)
node_3 = BSTNode(3, 3, None)
node_5 = BSTNode(5, 5, None)
node_7 = BSTNode(7, 7, None)

node_9 = BSTNode(9, 9, None)
node_11 = BSTNode(11, 11, None)
node_13 = BSTNode(13, 13, None)
node_15 = BSTNode(15, 15, None)



node_8 = BSTNode(8, 8, None)
node_4 = BSTNode(4, 4, node_8)
node_12 = BSTNode(12, 12, node_8)

node_2 = BSTNode(2, 2, node_4)
node_6 = BSTNode(6, 6, node_4)


node_10 = BSTNode(10, 10, node_12)
node_14 = BSTNode(14, 14, node_12)



tree = BST(node_8)

node_8.LeftChild = node_4
node_8.RightChild = node_12
node_4.LeftChild = node_2
node_4.RightChild = node_6
node_12.LeftChild = node_10
node_12.RightChild = node_14


print(tree.AddKeyValue(1, 1))
print(tree.AddKeyValue(11, 11))
print(tree.AddKeyValue(13, 13))
# print(tree.AddKeyValue(6, 6))

# print(tree.AddKeyValue(5, 5))
print(tree.AddKeyValue(7, 7))
print(tree.AddKeyValue(15, 15))
print(tree.AddKeyValue(3, 3))
# print(tree.AddKeyValue(5, 5))
# print(tree.AddKeyValue(9, 9))
# # print()
# print(tree.FindNodeByKey(9).Node.Parent.NodeKey)

# print("min tree", tree.FinMinMax(10, False))

# print(node_4.RightChild.NodeValue)

# print(tree.Count())

# print(tree.Root.RightChild.RightChild.LeftChild.NodeKey)

# nd = tree.FindNodeByKey(3)
tree.DeleteNodeByKey(15)
tree.DeleteNodeByKey(12)
tree.DeleteNodeByKey(4)
tree.DeleteNodeByKey(2)
tree.DeleteNodeByKey(7)
tree.DeleteNodeByKey(14)
# tree.DeleteNodeByKey(8)

# print(nd.Node.NodeValue)

print(tree.Count())
print(tree.Count())
print(tree.Count())