import random

def test(prisoners) :
    #Generate boxes
    boxes = []

    for i in range(prisoners) :
        boxes.append(i)
    
    random.shuffle(boxes)
    
    #Simulate prisoners
    sucess = True

    for i in range(prisoners) :
        foundMyBox = False
        boxesSearched = []
        target = i

        while not foundMyBox and len(boxesSearched) <= prisoners / 2 :
            boxesSearched.append(target)
            
            if boxes[target] == i : #Box found!
                foundMyBox = True
                #print(f"Prisoner {i} found their box.")
            else :
                target = boxes[target] #Find new target, continue in loop
        
        if not foundMyBox :
            sucess = False
            break
    
    return sucess

test(100)