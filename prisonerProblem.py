import random

def test(prisoners) :
    boxes = []

    for i in range(prisoners) :
        boxes.append(i)
    
    random.shuffle(boxes)
    print(boxes)

test(100)