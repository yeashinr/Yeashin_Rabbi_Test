def overlap(PQ,AB):
    index = 0
    output = 'Empty'

    for x in range(len(PQ)):
        if PQ[x] > 0 and PQ[x] >0:
            while index < len(PQ):
                print('Hello')
                if PQ[1] <= AB[index] or PQ[0] >= AB[index]:                #(PQ[0] < AB[0] and AB[1] < PQ[1] or AB[0] < PQ[1] and AB[1] > PQ[0])
                    output = 'Two lines are overlaped'
                else:
                     index +=1
        else:
            while index < len(PQ):
                if PQ[1] <= AB[index] or PQ[0] >= AB[index]:                #(PQ[0] < AB[0] and AB[1] < PQ[1] or AB[0] < PQ[1] and AB[1] > PQ[0])
                    output= 'Two lines are overlaped '
                else:
                    index +=1
    return output

            
    

   

if __name__ == '__main__':
    try:
        PQ1 = int(input("Please enter First cordinates for First line:"))
        PQ2 = int(input("Please enter Second cordinates for First line:"))

        AB1 = int(input("Please enter First cordinates for Second line:"))
        AB2 = int(input("Please enter Second cordinates for Second line:"))
        output = overlap([PQ1, PQ2],[AB1,AB2])
        
    except ValueError:
        print('Only numeric values are allowed')
    except KeyboardInterrupt:
        print('You have to interrupted the program')
    
    
     