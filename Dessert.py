def menu():
    print("-Dessert Quiz")
    print("-Dessert Recipes")
    
def print_recipe(dessert):
    """
    Description: Prints a recipe for either Strawberry Macarons or a Vanilla Panna Cotta
    
    Parameters: dessert - the type of dessert to print out a recipe for
    """
    
    # Prints out recipe for Strawberry Macarons
    if dessert == "strawberry macarons":
        
        print("STRAWBERRY MACARONS RECIPE:\n")
        print("Ingredients:")
        for items in ingredients:
            print(items)
        
        print("Kitchen Tools:")
        for item in kitchenTools:
            print(item)
        
        print("\nLine 2 large baking sheets with parchment paper or silicone baking mats.")
        print("Put powdered sugar, almond flour, and salt in a food processor and pulse several times")
        print("until all of the ingredients are fine and well combined. You can’t over mix this mixture") 
        print("because there is no flour! Place in a large bowl and set aside. Place the whisk attachment") 
        print("on your mixer, and beat the eggs on medium speed until opaque and foamy. You’ll want to see")
        print("your eggs double in volume.  Add a pinch of cream of tartar (if you're using it),")
        print("increase the speed to medium high, continue to beat until the egg whites are white in color") 
        print("and hold the line of the whisk. You should be able to see soft peaks in your whites.\n")
        
        print("With the mixer running, slowly add the granulated sugar, until stiff peaks form, and the") 
        print("whites are shiny, about 2 minutes.\n")
        
        print("Remove 1 cup of the mixture and stir in the jam, then carefully fold back into the egg-sugar mixture.")
        print("Using a silicone spatula, gently fold the dry mixture with the egg whites in 1 cup increments until")
        print("the dry ingredients are just combined. Spoon half of batter into pastry bag fitted with 1/2-inch plain")
        print("round tip. (Or a large ziplock bag which you can cut the corner off of.) Pipe batter onto each prepared") 
        print("sheet in 12 walnut-size mounds, spaced 3″ apart because cookies will spread slightly.\n")

        print("Tap the cookie sheets flat against the counter – you want to get any possible air bubbles out of the cookie") 
        print("batter before baking. This is an important step! Don’t run through getting as many of the bubbles out as") 
        print("you can. Let the cookies dry for 20 minutes before preheating the oven to 350F. Bake the cookies, 1 sheet") 
        print("at a time, until firm to the touch in the center, about 14 minutes. You may want to rotate your cookie") 
        print("sheets midway through baking to ensure even cooking (imperative with macarons). Immediately slide the") 
        print("parchment paper off of the baking sheet to cool to prevent burning. Leaving the cookies on the hot") 
        print("baking sheet will continue to cook them past taking them out of the oven.\n")

        print("Strawberry Filling Recipe:\n")
        
        print("Using a mixer, cream butter until smooth. Add the powdered sugar and beat until light and fluffy.")
        print("Add the vanilla and strawberry puree. Beat until combined. Place in a piping bag with a small round")
        print("tip.\n")
        
        print("Assemble your cookies by matching cookies with similar sizes (diameters). Pipe a small amount of") 
        print("strawberry buttercream into the center of one cookie, and sandwich with it’s other half.")
 
    # Recipe for Vanilla Panna Cotta
    elif dessert == "vanilla panna cotta":
        print("Vanilla Panna Cotta with Mixed-Berry Compote Recipe:\n")
         
        print("Ingredients:\n")
              
        for items in ingredients2:
            print(items)
        
        print("Pour 1/4 cup cold water into small custard cup. Sprinkle gelatin over. Let stand until gelatin softens,")
        print("about 15 minutes. Bring 1 inch of water in small skillet to boil. Place cup with gelatin in water. Stir until")
        print("gelatin dissolves, about 2 minutes. Remove from heat.\n")
         
        print("Combine cream and 2/3 cup sugar in heavy medium saucepan. Stir over medium heat just until sugar dissolves.")
        print("Remove from heat. Mix in vanilla and gelatin. Divide pudding mixture among 8 wineglasses. Cover and chill until")
        print("set, at least 6 hours and up to 1 day.\n")
         
        print("Mixed Berry Compote Recipe:")
        print("Combine berries and remaining 1/3 cup sugar in medium bowl. Crush berries slightly with back of spoon. Let") 
        print("compote stand until berry juices and sugar form syrup, stirring often, at least 1 hour and up to 2 hours.")
        print("Spoon compote over puddings.")
              
def dessert_quiz():
    """
    Description: A short quiz about what dessert the player is
    """
    pointsList = [0, 0, 0, 0, 0]    # Keeps track of the total points for each category
    newList = 0                     # Holds the return value from calling the points function
    
    # The categories that points are being added to
    category = ["Fruit Tart", "Cookie", "Chocolate Cake", "Strawberry Shortcake", "Panna Cotta"]
    
    # Answer choices for all 4 questions
    question1 = ["yes", "no"]       
    question2 = ["chocolate", "cookie dough", "cookies and cream", "mint", "strawberry", "vanilla"]
    question3 = ["crunchy", "soft", "creamy", "jelly-like"]
    question4 = ["painting", "riding a bike", "cooking", "exercising"]
    
    # Question 1
    # Prints out the question and answer choices
    print("Question 1:")
    print("Do you like having fruits on your desserts?\n")
    print("%s    %s" % (question1[0], question1[1]))
    
    playerInput = input().lower()
    
    # Calculates the amount of points added to each category based on the answer choice
    if playerInput == "yes":
        newList = points(["fruit", "strawberry shortcake", "panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "no":
        newList = points(["cookies", "chocolate cake"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
        
    
    # Question 2
    # Prints the question and answer choices
    print("\nQuestion 2:")
    print("What is your favorite flavor of ice cream?\n")
    print("%s    %s    %s\n" % (question2[0], question2[1], question2[2]))
    print("%s         %s    %s" % (question2[3], question2[4], question2[5]))
    
    playerInput = input().lower()
    
    # Asks the user for another input if the input is invalid
    while playerInput not in question2:
        playerInput = input("That is not a valid answer. Please type a valid answer.")
    
    # Calculates the points added to each category based on the answer choices
    if playerInput == "chocolate":
        newList = points(["cookies", "chocolate cake"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "cookie dough":
        newsList = points(["cookies"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput in ["cookies and cream", "cookiesncream"]:
        newList = points(["cookies", "chocolate cake"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "mint":
        newList = points(["fruit tart"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "strawberry":
        newsList = points(["strawberry shortcake"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "vanilla":
        newList = points(["panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    # Question 3
    # Prints out the question and answer choices
    print("\nQuestion 3:")
    print("What is your favorite texture in a dessert?\n")
    print("%s    %s\n" % (question3[0], question3[1]))
    print("%s     %s" % (question3[2], question3[3]))
    
    playerInput = input().lower()
    
    # Asks the user for anotehr input if the input is invalid
    while playerInput not in question3:
        playerInput = input("That is not a valid answer. Please type a valid answer.")
    
    # Calculates the points added to each category based on teh answer choices
    if playerInput == "crunchy":
        newList = points(["fruit tart", "cookies"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "soft":
        newList = points(["fruit tart", "chocolate cake", "strawberry shortcake", "panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput in "creamy":
        newList = points(["chocolate cake", "panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput in ["jelly-like", "jellylike", "jelly like"]:
        newList = points(["panna cotta"]) 
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    # Question 4
    
    # Prints out the question and answer choices
    print("\nQuestion 4:")
    print("What is your favorite hobby?\n")
    print("%s    %s\n" % (question4[0], question4[1]))
    print("%s     %s" % (question4[2], question4[3]))
    
    playerInput = input().lower()
    
    # Asks the user for a valid input if the input is not valid
    while playerInput not in question4:
        playerInput = input("That is not a valid answer. Please type a valid answer.")
    
    
    # Calculates the amount of points added to each category based on the answer choice   
    if playerInput == "painting":
        newList = points(["fruit tart", "panna cotta"]) 
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput in ["riding a bicycle", "ridingabicycle", "riding"]:
        newList = points(["fruit tart", "cookies", "panna cotta"]) 
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "cooking":
        newList = points(["fruit tart", "chocolate cake", "strawberry shortcake", "panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    elif playerInput == "exercising":
        newList = points(["fruit tart", "strawberry shortcake", "panna cotta"])
        pointsList[0] = pointsList[0] + newList[0]
        pointsList[1] = pointsList[1] + newList[1]
        pointsList[2] = pointsList[2] + newList[2]
        pointsList[3] = pointsList[3] + newList[3]
        pointsList[4] = pointsList[4] + newList[4]
    
    # Gets the index of the cateogry with the most points
    finalResult = result(pointsList)
    finalResult = category[finalResult]
    
    # Prints out the final result
    print("\nCongratulations! You are a %s!" % finalResult)
    print("ﾟ･✿ヾ╲(｡◕‿◕｡)╱･ﾟ:✲:～♬♫♬\n")
    print("() ()    () ()")
    print("(^-^)    (^-^)")
    print('(")(")  (")(")')
    

def points(answerList):
    """
    Description: Calculates the amount of points for each category
    
    Parameters: answerList(list of strings) - the list of categories to add points to
    parametrs list must only contain: "fruit tart", "cookies", "chocolate cake", "strawberry shortcake", "panna cotta"
    """
    fruit = 0            # Keeps track of the points for the Fruit Tart category 
    cookie = 0           # Keeps track of the points for the Cookie category
    chocoCake = 0        # Keeps track of the points for the Chocolate Cake category
    strawShortcake = 0   # Keeps track of the points for the Strawberry Shortcake category
    pannaCotta = 0       # Keeps track of the points for the Panna Cotta category
    pointsList = []      # a list of the new amount of points 
    
    # Categories of desserts
    dessert = ["fruit tart", "cookies", "chocolate cake", "strawberry shortcake", "panna cotta"]
  
    # Adds points to the category based on the strings in the answerList parameter
    for dessert in answerList:
        
        # Breaks out of the for loop if the dessert is not one of the 5 desserts in the dessert list
        while dessert not in dessert:
            print("That is not a valid dessert")
            break
            
        if dessert == "fruit tart":
            fruit = fruit + 1
        
        if dessert == "cookies":
            cookie = cookie + 1
        
        if dessert == "chocolate cake":
            chocoCake = chocoCake + 1
        
        if dessert == "strawberry shortcake":
            strawShortcake = strawShortcake + 1
        
        if dessert == "panna cotta":
            pannaCotta = pannaCotta + 1
                            
    # A list of the newly calculated points
    pointsList = [fruit, cookie, chocoCake, strawShortcake, pannaCotta]
                            
    return pointsList

def result(lst):
    """
    Description: Calculates which category has the most points
    
    Parameters: lst (list of int) - list of the number of points for each category
    Ex. ["fruit tart", "cookies", "chocolate cake", "strawberry shortcake", "panna cotta"]
    
    Return Value: Returns the index of the category with the most points 
    """
    
    maximum = 0    # Keeps track of the category with the largest amount of points 
    
    for points in lst:
        
        # Finds the maximum number of points out of all the categories
        if points > maximum:
            maximum = points
    
    index = lst.index(points)
    
    return index