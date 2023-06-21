# %%

from tree import preorder_construct, TreeNode, preorder_traverse

x = [6, 4, 3, None, None, 5, None, None, 8, 7, None, None, 9, None, None]

root = preorder_construct(x)


def search(root, target):
    if not root:
        return None

    if root.val == target:
        return root

    if root.val > target:
        return search(root.left, target)
    else:
        return search(root.right, target)


node = search(root, 3)
print(node.val)
# %%


def add(root, target):
    node = TreeNode(target)

    if root.val > target:
        if not root.left:
            root.left = node
        else:
            add(root.left, target)

    if root.val < target:
        if not root.right:
            root.right = node
        else:
            add(root.right, target)


add(root, 11)
print(preorder_traverse(root))
