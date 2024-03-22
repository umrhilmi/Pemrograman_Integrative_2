class Person:
    def __init__(self, weight, height):
        self.weight = weight  # in kilograms
        self.height = height  # in meters

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

# Example usage
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
person = Person(weight, height)
print("BMI:", person.BMI_Value())
