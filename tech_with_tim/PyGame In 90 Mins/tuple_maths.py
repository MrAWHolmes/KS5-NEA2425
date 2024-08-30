#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      archi
#
# Created:     28/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class C:
    count : int = 0
    name  : str = None

    def __init__(self):
        C.count += 1
        self.name = "name"+str(self.count)




def main():
    t = {"bob":12, "mary":13}

    for k in t:
        print(k)

    c1 = C()
    c2 = C()

    print(c1.name)
    print(c2.name)

if __name__ == '__main__':
    main()