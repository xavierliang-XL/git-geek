#一个小球从10米的高空落下，每次落地跳回原来的一半，再落下，求第10次时准备下降时，一共途径了多少路程
#i表示下降次数
height = 10
def lifting(height):
    """
    this method is to solve the 'lifting ball' question
    height:initial falling height
    """
    sum = 0
    i = 1
    while i<10:
        sum+=height
        height/=2
        sum += height
        i+=1

    return(sum)

