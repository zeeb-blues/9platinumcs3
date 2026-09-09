class Function:
    def __init__(self, a, b, c, d):
        self.__name = a
        self.degree = b
        self.leading_coefficient = c
        self.constant = d
        self.xshifted = 1
        self.yshifted = 1
        self.xdilated = 1
        self.ydilated = 1
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

    def get_expression(self):
        return self.__expression

    def xshift(self, shift):
        self.xshifted += shift
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"
    
    def yshift(self, shift):
        self.yshifted += shift
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

    def xreflect(self):
        self.xdilated *= -1
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

    def yreflect(self):
        self.ydilated *= -1
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

    def xdilate(self, factor):
        self.xdilated *= factor
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

    def ydilate(self, factor):
        self.ydilated *= factor
        self.__expression = f"{self.__name}(x) = {self.xdilated}({self.ydilated}(({self.leading_coefficient}x+{self.constant})-{self.xshifted}))^{self.degree}+{self.yshifted}"

object1 = Function("f", 3, 2, 1)
object2 = Function("g", 1, 3, 2)

print("BEFORE:")
print(object1.get_expression())
print(object2.get_expression())
print("")

print("* PERFORMING ACTION ON OBJECT 1 *")
object1.xshift(5)
print("")

print("AFTER:")
print(object1.get_expression())
print(object2.get_expression())