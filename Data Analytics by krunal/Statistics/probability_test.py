import random
def test():
    """
    Head=1
    tail=0
    
    """
    num_of_head=0
    for flip in range(10):
        num_of_head=num_of_head+random.randint(0,1)
    return (num_of_head>=6)

def excercise(n):
    success=0
    for t in range(n):
        success+=int(test())
    print(success)
    print(n)
    print(success/n)
excercise(10)