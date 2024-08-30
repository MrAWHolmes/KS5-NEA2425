#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      archi
#
# Created:     29/08/2024
# Copyright:   (c) archi 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Testing:
    def __init__(self,name:str):
        self.name = name
        self.warn_count = False

    def fail(self):

        if not hasattr(self,'foo'):
            if not self.warn_count :
                print(f"{self.name} has not attribute 'foo'")
                self.warn_count = True
        else:
            if self.foo == None:
                if not self.warn_count:
                    print(f"{self.name}.foo == None (has no value)")
                    self.warn_count = True


    def oops(self):
        self.foo = None





def main():
    one = Testing("one")

    for x in range(100):
        one.fail()

    input("Press Enter...")

    two = Testing("two")
    two.oops()

    for x in range(100):
        two.fail()



if __name__ == '__main__':
    main()
