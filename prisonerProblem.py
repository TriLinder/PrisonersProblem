from audioop import mul
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
        boxesSearched = 0
        target = i

        while not foundMyBox and boxesSearched <= prisoners / 2 :
            boxesSearched += 1
            
            if boxes[target] == i : #Box found!
                foundMyBox = True
                #print(f"Prisoner {i} found their box.")
            else :
                target = boxes[target] #Find new target, continue in loop
        
        if not foundMyBox :
            sucess = False
            break
    
    return sucess

def multipleTests(amount, prisoners) :
    successes = 0

    for i in range(amount) :
        if test(prisoners) :
            successes += 1
    
    print(f"{successes} out of {amount} attempts were successful.")
    print(f"Chance: {(successes / amount)*100}%")

    return successes

if __name__ == "__main__" :
    prisoners = int(input("Amount of prisoners: "))
    attempts = int(input("Amount of attempts: "))
    
    multipleTests(attempts, prisoners)