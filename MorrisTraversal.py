def morrisTraversal(root):
    node = root
    while node:
        if node.left != None:
            pre = node.left
            while pre.right != None and pre.right != node:
                pre = pre.right

            if pre.right == None:
                pre.right = node
                node = node.left
            else:
                pre.right = None
                print(node.data, end=" ")
                node = node.right
        else:
            print(node.data, end=" ")
            node = node.right
