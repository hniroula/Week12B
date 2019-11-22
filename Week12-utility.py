
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
