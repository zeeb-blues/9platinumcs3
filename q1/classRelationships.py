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
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def get_expression(self):
        return self.expression

    def xshift(self, shift):
        self.__xshifted += shift
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def yshift(self, shift):
        self.__yshifted += shift
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def xreflect(self):
        self.__xdilated *= -1
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def yreflect(self):
        self.__ydilated *= -1
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def xdilate(self, factor):
        self.__xdilated *= factor
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

    def ydilate(self, factor):
        self.__ydilated *= factor
        self.expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"

class CartesianPlane:
    def __init__(self, a):
        self.__name = a
        self.functions = []

    def plotFunction(self, function):
        self.functions.append(function)

    def get_name(self):
        return self.__name

if __name__ == "__main__":
    print("CREATING OBJECTS...")

    plane = CartesianPlane("delta")
    object1 = Function("f", 3, 2, 1)
    object2 = Function("g", 1, 3, 2)
    object3 = Function("h", 5, 1, 4)

    print("")
    print("OBJECTS CREATED:")

    print(plane.get_name())
    print(object1.expression)
    print(object2.expression)
    print(object3.expression)

    print("")
    print("PLOTTING FUNCTIONS...")

    plane.plotFunction(object1)
    plane.plotFunction(object2)
    plane.plotFunction(object3)

    print("")
    print("FUNCTIONS PLOTTED ON plane:")

    for function in plane.functions:
        print(function.expression)