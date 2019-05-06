class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если не найден узел
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        node = BSTFind()
        node.Node = self.Root

        if key == node.Node.NodeKey:
            node.NodeHasKey = True

        else:
            if key > node.Node.NodeKey:
                if node.Node.RightChild:
                    node = BST(node.Node.RightChild)
                    return node.FindNodeByKey(key)

            else:
                if node.Node.LeftChild:
                    node = BST(node.Node.LeftChild)
                    return node.FindNodeByKey(key)

                else:
                    node.ToLeft = True

        return node


    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey(key)

        if node.NodeHasKey is False:

            if node.ToLeft == True:
                node.Node.LeftChild = BSTNode(key, val, node.Node)

            else:
                node.Node.RightChild = BSTNode(key, val, node.Node)

            return True

        else:
            return False


    def FinMinMax(self, FromNode, Findmax):
        findNode = self.FindNodeByKey(FromNode)
        print("find node", findNode)
        node = findNode.Node

        if Findmax:
            while node.RightChild:
                node = node.RightChild
        else:
            while node.LeftChild:
                node = node.LeftChild

        return node.NodeKey

    def DeleteNodeByKey(self, key):
        deleteNode = self.FindNodeByKey(key)
        left = deleteNode.Node.LeftChild
        right = deleteNode.Node.RightChild

        if left and right:
            replaceKey = self.FinMinMax(right.NodeKey, False)
            replaceNode = self.FindNodeByKey(replaceKey)

            if replaceNode.Node.RightChild:
                replaceNode = replaceNode.Node.RightChild

            else:
                replaceNode = replaceNode.Node

        elif left and right is None:
            replaceNode = left

        elif right and left is None:
            replaceNode = right

        else:
            deleteNode.Node.Parent.LeftChild = None
            deleteNode.Node.Parent.RightChild = None
            return

        deleteNode.Node.NodeValue = replaceNode.NodeValue
        deleteNode.Node.NodeKey = replaceNode.NodeKey
        replaceNode.Parent.RightChild = None
        replaceNode.Parent.LeftChild = None

    def Count(self):

        node = self.Root
        count = 1

        if node.LeftChild:
            lnode = BST(node.LeftChild)
            count += lnode.Count()

        if node.RightChild:
            rnode = BST(node.RightChild)
            count += rnode.Count()

        return count

