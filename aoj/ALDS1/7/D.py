n = int(input())
*preorder, = map(int, input().split())
*inorder, = map(int, input().split())


def reconstruction(l, r):
    global preorder
    global inorder

    if l >= r:
        return ""
    a = ""
    c = preorder.pop(0)
    i = inorder.index(c)
    a += reconstruction(l, i)
    a += reconstruction(i+1, r)
    a += f"{c} "
    return a


print(reconstruction(0, n).strip())
