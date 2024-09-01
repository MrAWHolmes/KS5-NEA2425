"""
 Wrapper for nodes to be inserted into HashQ    
"""
import inspect

def camelCase(name:str)->str:
    """
    Turns a name into  a valid camel case equivalent
    1. Title Case & remove all spaces (PascalCase)
    2. If first character is a digit _prepended
    3. lowecase first charcter

    Parameters:
    name (str): an identifier name
    
    Returns:
    return_type: str
    """
    # use the user defined type!
    #1. Title Case it
    name = name.title() #Pascal Case
                    
    #2. clean string - no spaces allowed
    name = name.replace(" ","") #remove all spaces
    
         
    #3. camelCase it
    
    if len(name)>0:
        if name[0] in "0123456789":
            name = "_"+name
            
        name = name[0].lower() + name[1:]
        
    return name
    
class Wrapper:
    nodeType = None
    node = None
    
    def __init__(self,node:object,ntype:str="auto"):
        warnOnly = True
        autotypes = [None,"","auto","?"]
        primitives = (int, float, str, bool, list, tuple, dict)
        self.node = node
        #print(self.node)
        
        if self.node == None:
            self.nodeType = "__NoneNode__"
            print(f"Warning! node == None")
            print((f"      this.nodeType set to {self.nodeType}"))
            return
        else:
            ntype = camelCase(ntype)
        
        if (ntype not in autotypes) and len(ntype)>0:    
            self.nodeType = ntype
            if not warnOnly:
                print(f"Notice! User nodeType used")
                print((f"      .nodeType set to {self.nodeType}"))
            return
        
        #We need to detect it as "auto" set / not helpful value
        if (ntype in autotypes) and isinstance(node,primitives):
            self.nodeType = "auto"
            if isinstance(node,int):
                self.nodeType = "int"
            
            if isinstance(node,float):
                self.nodeType = "float"    
            
            if isinstance(node,str):
                self.nodeType = "str"    
            
            if isinstance(node,bool):
                self.nodeType = "bool"
            
            if isinstance(node,list):
                self.nodeType = "list"
            
            
            if isinstance(node,tuple):
                self.nodeType = "tuple"
                        
            if isinstance(node,dict):
                self.nodeType = "dict"
            
        #if we get here not a built in type so self.nodeType is still not set...
        if (self.nodeType in [None,"","auto"]):
            #nodeType = None is a fail flag condition
            self.nodeType = None # assume fail
            #only run if ntype parameter is not helpful/still: "auto" or "" or None    
            if inspect.isfunction(self.node):
                self.nodeType = "function"
                
            if inspect.ismethod(self.node):
                self.nodeType = "method"
                
            
            
        if self.nodeType == None:
            print("node is not builtin or callable....")
            typeClass = str(self.node.__class__)
            print(typeClass)
            
            print(f"Warning! auto typing of {node} failed")
            self.nodeType = None
        else:
            if not warnOnly:
                print(f"Note   ! auto typing of {node} succeded")
                print((f"      this.nodeType set to {self.nodeType}"))    
                
        
    def getNode(self):
        return self.node
    
    def getNodeType(self):
        return self.nodeType
    
    def __str__(self):
       return f"nodeType: {self.nodeType} with node={self.node}"
           

    
def main():
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
        if q in pruneQ:
            del Q
        else:
            print(q)
            if  q.nodeType in ["function","method"]:
                print("+-------------------------------------+")
                print(f"|running {q}")
                print(q.node())
                print("+-------------------------------------+")
            
   
        
        
        
        
        
        
if __name__ == "__main__":
    main()
        
        