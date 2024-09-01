from engine.Wrapper import Wrapper,camelCase 

def foo():
    return "foo"

class Testing:
    def __init__(self):
        pass

    def m(self):
        return "mmmm"

t = Testing()
stuff = [10,"Hello",t,False,12.3,[1,2,3],(1,2,3),{1:"one",2:"two",3:"three"},42]


Q = list()

for x in range(len(stuff)):
    Q.append(Wrapper(stuff[x]))
Q.append(Wrapper(Testing(),"Class-Testing"))
    
Q.append(Wrapper(t.m))
Q.append(Wrapper(foo))
Q.append(Wrapper(None))
    
for node in Q:
    print(node)

print("=================================")    
print("=================================")    

pruneQ = list()
pruneQ.append(Q[0])

for q in Q:
    if q.node == None or q.nodeType == "__NoneNode__":
        pruneQ.append(q)

for q in Q:
    if q in pruneQ:
        del q
    else:
        print(q)
        if  q.nodeType in ["function","method"]:
            print("+-------------------------------------+")
            print(f"|running {q}")
            print(q.node())
            print("+-------------------------------------+")
        
print(camelCase("turn me into camel case"))
        
        
        
        
