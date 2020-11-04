#一个小球从10米的高空落下，每次落地跳回原来的一半，再落下，求第10次时落地的高度
height = 10
def lifting(height):
    """
    this method is to solve the lifting ball ques
    height:initial falling height
    """
    for i in range(2,11):
        height/=2

    return(i,height)