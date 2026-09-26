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

class Discriminant:
    def __init__(self, a, b, c):
        self.value = (b ** 2) - (4 * a * c)

    def get_nature(self):
        if self.value > 0:
            return "two distinct real roots"
        elif self.value == 0:
            return "one real root"
        else:
            return "two complex roots"

class QuadraticFunction(Function):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
        self.degree = 2
        self.__xshifted = 0
        self.__yshifted = 0
        self.__xdilated = 1
        self.__ydilated = 1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}"
        self.discriminant = Discriminant(self.leading_coefficient, 0, self.constant)

    def get_expression(self):
        return self.__expression

    def get_vertex(self):
        return self.__vertex

    def xshift(self, shift):
        self.__xshifted += shift
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")
        
    def yshift(self, shift):
        self.__yshifted += shift
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")
    
    def xreflect(self):
        self.__xdilated *= -1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")
    
    def yreflect(self):
        self.__ydilated *= -1
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")
        
    def xdilate(self, factor):
        self.__xdilated *= factor
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")
        
    def ydilate(self, factor):
        self.__ydilated *= factor
        self.__expression = f"{self.name}(x) = {self.__xdilated}({self.__ydilated}(({self.leading_coefficient}x+{self.constant})-{self.__xshifted}))^{self.degree}+{self.__yshifted}"
        self.__vertex = (f"{(self.__xshifted-self.constant)/self.leading_coefficient}, {self.__yshifted}")

print("TEST 1 — INHERITANCE:")
print("")
print("CREATING OBJECT UNDER QuadraticFunction...")
object1 = QuadraticFunction("f", 2, 3, 1)
print("")
print("OBJECT CREATED:")
print(object1.get_expression())
print("")
print(f"VERTEX: {object1.get_vertex()}")
print("")
print("TEST 2 — COMPOSITION:")
print("")
print(f"DISCRIMINANT OF OBJECT under QuadraticFunction: {object1.discriminant.value}")