
#   Incremental build model
#   Hari Niroula
#  ​CSCI 102 – Section B 
#   Week 12 - Part B 

####Function 1 [PRINTOUTPUT]
def printOutput(string):
    print('OUTPUT' , string)
#printOutput('Hello World')


####Function 2 [LOADFILE]
def Loadfile(somefile):
    my_list=[]
    f= open(somefile)
    lines=f.readlines()
    for ln in lines:
        my_list.append(ln[0:len(ln)-1])
    return my_list
#printOutput(Loadfile('test.txt') )       # I have file test as text saved in same loaction.
####Function 3 [UPDATESTRING]

def UpdateString( string1, string2, n):
    my_list= list(string1)
    my_list[n]=string2
    return ''.join(my_list)
#printOutput(UpdateString("Hello World", "a", 3))

####Function 4    

def FindWordCount(some_list, string):    
    number=0
    for word in some_list:
        number += word.count(string)
    return number
#a=Loadfile('test.txt')
#printOutput((FindWordCount(a, 'I'))) # I have file saved as 'test'. 'I' occurs once.

####Function 5  

def ScoreFinder(list_players, list_scores, str_name):
    upper= str_name.upper()        
    for i in range(len(list_players)):
         
        if list_players[i].upper()==upper:
            score=list_scores[i]
            print('OUTPUT', list_players[i], 'got a score of', score)
            return   
        
    print('OUTPUT player not found ')
              
     
     
      
        
#players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"] 
#scores = [5, 8, 10, 6, 10, 4]                    
#ScoreFinder(players,scores,'Jill')
