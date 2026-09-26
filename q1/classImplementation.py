class Function:
    def __init__(self, a, b, c, d):
        self.name = a
        self.degree = b
        self.leading_coefficient = c
        self.constant = d
        self.__xshifted = 0
        self.__yshifted = 0
        self.__xdilated = 1
        self.__ydilated = 1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def get_expression(self):
        return self.__expression

    def xshift(self, shift):
        self.__xshifted += shift
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def yshift(self, shift):
        self.__yshifted += shift
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def xreflect(self):
        self.__xdilated *= -1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def yreflect(self):
        self.__ydilated *= -1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def xdilate(self, factor):
        self.__xdilated *= factor
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def ydilate(self, factor):
        self.__ydilated *= factor
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

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