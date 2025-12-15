def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):

    left1   = x1
    right1  = x1 + w1
    top1    = y1
    bottom1 = y1 + h1

    left2   = x2
    right2  = x2 + w2
    top2    = y2
    bottom2 = y2 + h2

    if right1 <= left2:
        return False
    if left1 >= right2:
        return False
    if bottom1 <= top2:
        return False
    if top1 >= bottom2:
        return False

    return True

print(check_collision(1,2,3,4,5,36,7,1))