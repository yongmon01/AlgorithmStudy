# 이방법은 완전 이진트리 일때만 가능.
# 완전 이진트리일때 left child index = index * 2, right child index = index * 2 + 1 이 보장되기 때문.

tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]

def traverse_inorder(tree, index):
    """in-order 순회 함수"""
    # 코드를 쓰세요
    if index < len(tree):
        traverse_inorder(tree, index * 2)
        print(tree[index])
        traverse_inorder(tree, index * 2+1)

traverse_inorder(tree, 1)