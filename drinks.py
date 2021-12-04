# Jessica Qi
# Assignment 10.1: Your Own Class
# The purpose of this code is to implement a class based on a real world object. In this case, a boba shop.

# This class will represent drink orders
class Drinks:
    # Creating a class varaible used to identify the place of all the drink orders
    shop = "Sammy's Shack"
    def __init__(self, name, size, sweetness, other):
        # Formatting and setting the name, size, sweetness, and other add-on/modifications based on constructor arguments
        name = name.title()
        self.name = name
        size = size.title()
        self.__size = size
        self.__sweetness = sweetness
        other = other.title()
        self.__other = other
        # Setting variables to "5 (max level)" or "0" if the constructor argument for sweetness is larger than 5 or less than 0
        if self.__sweetness >= 5:
            self.__sweetness = "5 (max level)"
        elif self.__sweetness <= 0:
            self.__sweetness = 0

    def add_sweetness(self, num):
        # Adding more sweetness by adding the inputted number to the original sweetness
        self.__num = num
        newsweetness = self.__sweetness + self.__num
        self.__newsweetness = newsweetness
        # Setting sweetness to "5 (max level)" if the new sweetness exceeds 5
        if newsweetness >= 5:
            self.__sweetness = "5 (max level)"
        # Proceeds to change the sweetness if it is under 5
        else:
            self.__sweetness = self.__newsweetness
    
    def remove_sweetness(self, num):
        # Removing sweetness by subtracting the inputted number from the orignal sweetness
        self.__num = num
        # Error handling --> ensures the function takes the value 5 and not the string "5 (max level)"
        if self.__sweetness == "5 (max level)":
            newsweetness = 5 - self.__num
        # Proceeds if the original sweetness was not 5
        else:
            newsweetness = self.__sweetness - self.__num
        self.__newsweetness = newsweetness
        # Setting sweetness to either 0 or "5 (max level)" given the new sweetness is either less than 0 or larger than 5
        if self.__newsweetness <= 0:
            self.__sweetness = 0
        elif self.__newsweetness >= 5:
            self.__sweetness = "5 (max level)"
        # Proceeds if the new sweetness is neither below 0 or above 5
        else:
            self.__sweetness = self.__newsweetness

    def change_size(self, size):
        # Formats and changes the size
        size = size.title()
        self.__size = size

    def change_other(self, other):
        # Formats and changes the add-on/modification
        other = other.title()
        self.__other = other

    def get_size(self):
        # Obtains the size
        return f"Current Size: {self.__size}"

    def get_sweetness(self):
        # Obtains the sweetness and provides insight to how many ounces is in a pump of syrup
        return f"Current Sweetness Level: {self.__sweetness} pumps\nOne pump equates to 0.5 ounces."

    def get_other(self):
        # Octains the add-on/modification and provides possible add-ons and modifications
        return f"Current Add-on/Modifications:{self.__other}\nList of possible add-ons: honey boba, grass jelly, aloe vera, custard pudding\nList of possible modifications: alternative substitutes for milk (almond, oat, soy), ice level"

    # Calculating the percentage of syrup in a medium or large sized drink
    def sugar_level(self):
        # Error handling --> ensures the function takes the value 5 and not the string "5 (max level)"
        if self.__sweetness == "5 (max level)":
            level = 5 * 0.5
        # Proceeds if the set sweetness is not 5
        else:
            level = self.__sweetness * 0.5
        self.__level = level
        # Calculating the percent of syrup in a medium sized drink
        if self.__size == "Medium":
            # Error handling --> ensures the function takes the value 5 and not the string "5 (max level)"
            if self.__sweetness == "5 (max level)":
                # Function takes in the ounces of syrup in 5 sweetness and divides by the ounces of a medium sized cup (16 oz.) and computes the percentage
                percent = (2.5 / 16) * 100
                percent = float(percent)
                self.__percent = percent
                return f"With 5 pumps of syrup, you have {self.__level} ounces of syrup. That is {self.__percent:.2f}% of your medium sized drink!"
            else:
                # Function takes in the ounces of syrup and divides by the ounces of a medium sized cup (16 oz.) and computes the percentage
                mediumpercent = (self.__level / 16) * 100
                mediumpercent = float(mediumpercent)
                self.__mediumpercent = mediumpercent
                return f"With {self.__sweetness} pumps of syrup, you have {self.__level} ounces of syrup. That is {self.__mediumpercent:.2f}% of your medium sized drink!"
        # Calculating the percent of syrup in a large sized drink
        elif self.__size == "Large":
            # Error handling --> ensures the function takes value 5 and not the string "5 (max level)"
            if self.__sweetness == "5 (max level)":
                # Function takes in the ounces of syrup in 5 sweetness and divides by the ounces of a large sized cup (20 oz.) and computes the percentage
                percent = (2.5 / 20) * 100
                percent = float(percent)
                self.__percent = percent
                return f"With 5 pumps of syrup, you have {self.__level} ounces of syrup. That is {self.__percent:.2f}% of your large sized drink!"
            # Function takes in the ounces of syrup and divides by the ounces of a large sized cup (20 oz.) and computes the percentage
            else:
                largepercent = (self.__level / 20) * 100
                largepercent = float(largepercent)
                self.__large = largepercent
                return f"With {self.__sweetness} pumps of syrup, you have {self.__level} ounces of syrup. That is {self.__large:.2f}% of your large sized drink!"
        # Return message saying that calculation cannot be done unless it is either medium or large
        else:
            return f"The inputted size ({self.__size}) is not found in our database. Please change the size to either medium (16 oz.) or large (20 oz.) to calculate the sugar level of your drink."

    # Magic methods
    def __str__(self):
        return (f"Your Order at {self.shop}:\nDrink Name: {self.name}\nSize: {self.__size}\nSweetness Level: {self.__sweetness} pumps\nAdd-ons/Modifications: {self.__other}")


def main():
    # Setting smoothie to have negative sweetness to demonstrate how the program handles negative arguments for sweetness
    smoothie = Drinks("mango smoothie", "small", -3, "none")
    print(smoothie)
    print(smoothie.get_sweetness())

    # Adding sweetness to tea and retrieving the sweetness and add-on/modifications
    tea = Drinks("oolong tea", "medium", 2, "sea salt foam")
    print(tea)
    tea.add_sweetness(3)
    print(tea)
    print(tea.get_sweetness())
    print(tea.get_other())

    # Computing the sugar level in the drink given different sweetness and sizes
    coffee = Drinks("vanila latte", "medium", 5, "honey boba")
    print(coffee)
    print(coffee.sugar_level())
    coffee.remove_sweetness(2)
    print(coffee.sugar_level())
    coffee.change_size("large")
    print(coffee.sugar_level())

    # Changing sizes to small to demonstrate how program handles finding the sugar level of a drink given an unknown size
    milkt = Drinks("jasmine milk tea", "large", 3, "aloe vera")
    print(milkt)
    milkt.change_size("small")
    print(milkt.get_size())
    print(milkt.sugar_level())

if __name__ == "__main__":
    main()