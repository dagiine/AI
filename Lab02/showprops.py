'''
Useful utility for examining objects in python.
It lists all the properties of an object and their respective values.
'''

def showprops(obj):
    for x in dir(obj):
        # print (x, getattr(obj, x))
        print ("%s\t%s" % (x, getattr(obj, x)))
        
def sp(obj):
    showprops(obj)

    

        
