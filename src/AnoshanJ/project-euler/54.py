import time

start = time.time()
#values of cards with indices correponding to their values

values = ["0","1", "2", "3" , "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

count = 0

with open("54_poker.txt", mode="r") as poker_file:
    #going line by line
    for line in poker_file:
        
        #splitting line to list
        cards = line.split()

        #adding each players cards with the value of the card now taken in digits
        player1 = [(values.index(char[0]), char[1]) for char in cards[0:5]]
        player2 = [(values.index(char[0]), char[1]) for char in cards[5:10]]

        #checking the suits of the cards
        symbol1 = len({player1[i][1] for i in range(5)})
        symbol2 = len({player2[i][1] for i in range(5)})

        #the values of the cards in ascending order
        card_values1 = sorted([player1[i][0] for i in range(5)])        
        card_values2 = sorted([player2[i][0] for i in range(5)])

        #creating a dictionary with the counts of how many time each card occured
        card_counts1 = {}
        card_counts2 = {}
        
        for i in range(5):
            card_counts1[card_values1[i]]=card_values1.count(card_values1[i])
            card_counts2[card_values2[i]]=card_values2.count(card_values2[i])


        #for special scenario where suits are same for all cards winning ranks is declared                   
        winning_ranks_1 = 0
        winning_ranks_2 = 0

        #checking if player one has all same suits
        if symbol1==1:            

            #checking if it is a royal flush
            if set(x for x in range(10,15))=={(player1[i][0]) for i in range(5)}:
                winning_ranks_1 = 10
            else:
                #checking if its a straight flush
                for i in range(2,9):
                    if set(x for x in range(i,i+5))=={(player1[j][0]) for j in range(5)}:                        
                        winning_ranks_1 = 9
                        break
                else:
                    #if not it is a flush
                    winning_ranks_1 = 6

        #repeating same scenario for player 2 if his suits are same            
        if symbol2==1:
            
            if set(x for x in range(10,15))=={(player2[i][0]) for i in range(5)}:
                
                winning_ranks_2 = 10
                
            else:                
                
                for i in range(2,9):
                                     
                    if set(x for x in range(i,i+5))=={(player2[j][0]) for j in range(5)}:       
                        
                        winning_ranks_2 = 9                        
                        break
                else:
                    winning_ranks_2 = 6
        #if there is a royal flush
        if winning_ranks_1 == 10 or winning_ranks_2 ==10:
            #if player 1 wins add one to the count and go to next line by continue
            if winning_ranks_1>winning_ranks_2:
                count+=1                
                continue
            #if draw or player 2 wins skip
            else:
                continue

        #if there is a straight flush    
        if winning_ranks_1 == 9 or winning_ranks_2 ==9:

            #if player 1 wins add one to the count and go to next line by continue
            if winning_ranks_1>winning_ranks_2:
                count+=1                
                continue
            #if draw further check
            elif winning_ranks_1==winning_ranks_2:
                #since the list is sorted check from reverse the one with higher card wins
                for i in range(4,-1,-1):                    
                    if card_values1[i]>card_values2[i]:
                        count+=1
                        #break out of the for loop
                        break
                    
                    elif card_values1[i]<card_values2[i]:
                        break
                continue
                
            else:                
                continue

        #note that if player b wins by royal flush or straight flush it will automatically skip
            
        #check if there is a 4 of a kind          
        if 4 in card_counts1.values():            

            #in the case player 2 also has 4 of a kind
            if 4 in card_counts2.values():
                
                #get the value which occured 4 times and the value which occured once
                for value, instances in card_counts1.items():

                    if instances==1:
                        maximum1_2 = value
                    if instances==4:
                        maximum1_1 = value
                        
                        
                for value, instances in card_counts2.items():

                    if instances==1:
                        maximum2_2 = value
                    if instances==4:
                        maximum2_1 = value

                #if the 4 of a kind is highest player 1 wins
                if maximum1_1>maximum2_1:
                    count+=1                    
                    continue
                
                if maximum1_1 ==maximum2_1:
                    #in the case of a draw check the value of the card which occured once
                    if maximum1_2 > maximum2_2:
                        count+=1                        
                        continue
                    else:
                        continue
                else:
                    continue
            #if player 2 doesn't have a 4 of a kind then player 1 wins
            else:                
                count+=1                
                continue
        #skip all cases player 2 has a 4 of a kind
        if 4 in card_counts2.values():
            continue        

        #check for player 1's full house
        if 3 in card_counts1.values() and 2 in card_counts1.values():           

            #in the case player 2 also has full house
            if 3 in card_counts2.values() and 2 in card_counts2.values():

                #get the value which occured 3 times and the value which occured twice
                for value, instances in card_counts1.items():
                                       
                    if instances==2:
                        maximum1_2 = value
                        
                    if instances==3:
                        maximum1_1 = value
                        
                        
                for value, instances in card_counts2.items():

                    if instances==2:
                        maximum2_2 = value
                        
                    if instances==3:
                        maximum2_1 = value
                        
                #compare the three of a kind 
                if maximum1_1>maximum2_1:
                    count+=1                    
                    continue
                #if three of a kind is a tie compare the pair
                if maximum1_1 ==maximum2_1:
                    if maximum1_2 > maximum2_2:
                        count+=1                        
                        continue
                    else:
                        continue
                else:
                    continue
            #in the event player 2 doesn't have a full house player 1 wins
            else:
                count+=1                
                continue

        #skip player 2's full houses   
        if 3 in card_counts2.values() and 2 in card_counts2.values():
            continue

        #check for flush        
        if winning_ranks_1 == 6 or winning_ranks_2 ==6:            

            #if player 1 wins the flush
            if winning_ranks_1>winning_ranks_2:
                count+=1                
                continue
            #in the case both have flushes
            elif winning_ranks_1 == winning_ranks_2:
                
                #compare the cards
                for i in range(4,-1,-1):                    
                    if card_values1[i]>card_values2[i]:
                        count+=1                        
                        continue
                    elif card_values1[i]<card_values2[i]:
                        continue
                continue
                    
            else:
                continue

        #checking for straight where all cards are consecutive valuse
        if(len(set(card_values1)))==5:            
            
            for i in range(2,10):

                #straight occurs
                if set(x for x in range(i,i+5))==set(card_values1):

                    #check if player 2 can have a straight 2
                    if(len(set(card_values2)))==5:
                       
                        for j in range(2,10):
                            #straight occurs    
                            if set(x for x in range(j,j+5))==set(card_values2):

                                #in the event both are straights compare the values of the cards
                                for i in range(4,-1,-1):                    
                                    if card_values1[i]>card_values2[i]:
                                        count+=1                                                                                
                                        break
                                    elif card_values1[i]<card_values2[i]:
                                        break
                                continue
                            else:
                                #player 1 wins if player 2 didn't have a straight but consecutive values
                                count+=1                                
                                break
                    #player 1 wins if player 2 couldn't have a straight
                    else:
                        count+=1                                                
                        continue

        #skip the instances player 2 has a straight
        if(len(set(card_values2)))==5:
            val = False
            
            for i in range(2,10):                
                if set(x for x in range(i,i+5))==set(card_values2):
                    val = True
                    break
            if val:                
                continue 

        #check for 3 of a kind(definitely other value should be one)
        if 3 in card_counts1.values() and 1 in card_counts1.values():
            
            #in the case player 2 also has a 3 of a kind
            if 3 in card_counts2.values() and 1 in card_counts2.values():
                
                maximum1_2 =[]
                #getting the value which occured thrice and the values which occured once in ascending order
                for value, instances in card_counts1.items():                                   
                                           
                    if instances==3:
                        maximum1_1 = value

                    else:
                        maximum1_2.append(value)

                maximum1_2.sort()                
                        
                maximum2_2 = []         
                for value, instances in card_counts2.items():                    
                        
                    if instances==3:
                        maximum2_1 = value
                    else:
                        maximum2_2.append(value)

                maximum2_2.sort()                        

                #player 1's three of a kind wins
                if maximum1_1>maximum2_1:
                    count+=1                    
                    continue
                #three of a kind draws
                if maximum1_1 ==maximum2_1:
                    #check the next highest value
                    if maximum1_2[1] > maximum2_2[1]:
                        count+=1                        
                        continue
                    #if that draws
                    elif maximum1_2[1] == maximum2_2[1]:
                        #compare the last value
                        if maximum1_2[0] > maximum2_2[0]:
                            count+=1                            
                            continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            #player 1 wins if player 2 didn't also have a 3 of a kind
            else:
                count+=1                
                continue
        #skipping the instances player 2 has 3 of a kinds
        if 3 in card_counts2.values():
            continue            

        #checking for instances where player 1 has two pairs( in that case there will be a 2 and the there has to be 3 unique elements)
        if 2 in card_counts1.values() and len(set(card_values1))==3:         
            
            #if player 2 has two pairs too
            if 2 in card_counts2.values() and len(set(card_values2))==3:

                #checking the values of the pairs and the single occured value
                maximum1_1 = []
                for value, instances in card_counts1.items():
                                   
                    if instances==1:
                        maximum1_2 = value                    

                    else:
                        maximum1_1.append(value)

                maximum1_1= sorted(list(maximum1_1))
                
                        
                maximum2_1 = []
                for value, instances in card_counts2.items():
                                   
                    if instances==1:
                        maximum2_2 = value                    

                    else:
                        maximum2_1.append(value)

                maximum2_1= sorted(list(set(maximum2_1)))
                        
                #comparing paris
                if maximum1_1[1]>maximum2_1[1]:
                    count+=1                    
                    continue
                #if the pairs draw
                if maximum1_1[1]==maximum2_1[1]:
                    #check next pair
                    if maximum1_1[0] > maximum2_1[0]:
                        count+=1                        
                        continue
                    #if that pair also draws
                    elif maximum1_1[0] == maximum2_1[0]:
                        #check last card
                        if maximum1_2 > maximum2_2:
                            count+=1                            
                            continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            #player 1 wins if player 2 didnt have 2 pairs    
            else:
                count+=1                
                continue

        #skipping the instances where player 2 has two pairs
        if 2 in card_counts2.values() and len(set(card_values2))==3:
            continue

        #checking for instances where player 1 has one pair( in that case there will be a 2 and the there has to be 4 unique elements)
        if 2 in card_counts1.values() and len(set(card_values1))==4:            
            #if player 2 also has a pair                
            if 2 in card_counts2.values() and len(set(card_values2))==4:            
                
                maximum1_2 = []
                #getting the value of the pair and the other values which occured once in ascending order
                for value, instances in card_counts1.items():
                                   
                    if instances==1:
                        maximum1_2.append(value)                    

                    else:
                        maximum1_1 = value                    
                maximum1_2.sort()                       
                
                maximum2_2 = []
                for value, instances in card_counts2.items():
                                   
                    if instances==1:
                        maximum2_2.append(value)                    

                    else:
                        maximum2_1=(value)                    
                maximum2_2.sort()
                        
                #player 1 wins if his pair is highest
                if maximum1_1>maximum2_1:
                    count+=1                    
                    continue
                #in the case of a draw
                if maximum1_1==maximum2_1:
                    # compare next highest value
                    if maximum1_2[2] > maximum2_2[2]:
                        count+=1                        
                        continue
                    #in the case of a draw
                    elif maximum1_2[2] == maximum2_2[2]:
                        #compare next highest value
                        if maximum1_2[1] > maximum2_2[1]:
                            count+=1                            
                            continue
                        #in the case of a draw
                        elif maximum1_2[1] == maximum2_2[1]:
                            #compare last value
                            if maximum1_2[0] > maximum2_2[0]:
                                count+=1                                
                                continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            #player 1 wins in the case player 2 doesnt have a pair
            else:
                count+=1                
                continue

        
        #the last case compare all cards
        if len(set(card_values1))==5:
            #in the case b all has unique cards, other cases like pairs are ignored
            if(len(set(card_values2)))==5:
                for i in range(4,-1,-1):
                    #one with highest card wins
                    if card_values1[i]>card_values2[i]:
                        count+=1                                                                
                        break
                    elif card_values1[i]<card_values2[i]:
                        break
                continue
            else:
                continue
            
print(count)

end = time.time()

print(end-start)
            
        
            
        

        
        
            
                
            
                
                    
                
        
        
