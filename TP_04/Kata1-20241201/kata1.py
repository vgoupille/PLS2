"""
Kata 1

"It's a dangerous business, Frodo, going out your door.
You step onto the road, and if you don't keep your feet,
there's no knowing where you might be swept off to."
Bilbo Baggins of Bag End.
"""


## 1 - Some useless names to begin your journey...
##     Nevertheless, you may learn some on the way.

""" 1.1 - Uncomment the next line and replace ___ to assign value 21 to name1. 
    Ask yourself: what is the class of name1?
"""
# name1 = ___

""" 1.2 - Uncomment the next line and replace ___ to assign value 10.5 to name2. 
    Ask yourself: what is the class of name2?
"""
# name2 = ___

""" 1.3 - Uncomment the next line and replace ___ to assign value True to name3. 
    Ask yourself: what is the class of name3?
"""
# name3 = ___

""" 1.4 - Uncomment the next line and replace ___ to assign value "42" to name4. 
    Ask yourself: what is the class of name4?
"""
# name4 = ___


## 2 - The bridge of useful math operators.
##     Where you may meet some new friends : -, **, +, /, %, *, //

""" 2.1 - Uncomment the next line and replace ___ by an operator to assign value 42 to name5. 
    Ask yourself: what is the class of name5? Does this operator always return this type of data? And why? 
"""
# name5 = name1 ___ 2

"""2.2 - Uncomment the next line and replace ___ by an operator to assign value 12.5 to name6. 
    Ask yourself: what is the class of name6? Does this operator always return this type of data? And why? 
"""
# name6 = name2 ___ 2

"""2.3 - Uncomment the next line and replace ___ by an operator to assign value 19 to name7. 
    Ask yourself: what is the class of name7? Does this operator always return this type of data? And why? 
"""
# name7 = name1 ___ 2

"""2.4 - Uncomment the next line and replace ___ by an operator to assign value 10 to name8. 
    Ask yourself: what is the class of name8? Does this operator always return this type of data? And why? 
"""
# name8 = name1 ___ 2

"""2.5 - Uncomment the next line and replace ___ by an operator to assign value 31.5 to name9. 
    Ask yourself: what is the class of name9? Does this operator always return this type of data? And why? 
"""
# name9 = name2 ___ 3

"""2.6 - Uncomment the next line and replace ___ by an operator to assign value 441 to name10. 
    Ask yourself: what is the class of name10? Does this operator always return this type of data? And why? 
"""
# name10 = name1 ___ 2

"""2.7 - Uncomment the next line and replace ___ by an operator to assign value 1 to name11. 
    Ask yourself: what is the class of name11? Does this operator always return this type of data? And why? 
"""
# name11 = name1 ___ 2

"""2.8 - Uncomment the next line and replace ___ by an operator to assign value 10.5 to name12. 
    Ask yourself: what is the class of name12? Does this operator always return this type of data? And why? 
"""
# name12 = name1 ___ 2


## 3 - The Troll under the bridge asks you a riddle :
##         I know the truth about 'and' and 'or'
##         I understand the meaning of 'not' operator
##         "All I say is False" tells my mouth
##         Can you decide if this is True or not?

"""3.1 - Uncomment the next line and replace ___ by an operator to assign value True to name13. 
    Ask yourself: are name5 and 35.1 of the same class? Is it a problem for this kind of operator? And why? 
"""
# name13 = name5 ___ 35.1

"""3.2 - Uncomment the next line and replace ___ by an operator to assign value False to name14. 
    Ask yourself: are different operators possible here? Which ones?
"""
# name14 = name12 ___ 12

"""3.3 - Uncomment the next line and replace ___ by an operator to assign value True to name15.
    Ask yourself: When you have to choose, do you always want to test if something is True or not?
"""
# name15 = ___ name14

"""3.4 - Uncomment the next line and replace ___ by an operator to assign value False to name16. 
    Ask yourself: Would you like cheese or dessert? Both? 
"""
# name16 = name13 __ (name7 == 18)

"""3.5 - Uncomment the next line and replace ___ by an operator to assign value True to name17. 
    Ask yourself: Same question again? You have to choose... Make up your mind.
"""
# name17 = name14 __ name10 > 67

"""3.6 - Uncomment the next line and replace ___ by an operator to assign value False to name18. 
    Ask yourself: Same question again? You have to choose... Make up your mind.
"""
# name18 = (name16 or name13) ___ (name14 and True)


## 4 - Past the bridge, the path winds through the swamp of transformations.
##     Where strings become numbers, and numbers are shapeshifters.
##     Wierder transformations may happen here.

"""4.1 - Uncomment the next line and replace ___ by a function name to assign value 42 to name19. 
    Ask yourself: Is 42 a string or a number?
"""
# name19 = ___(name4)

"""4.2 - Uncomment the next line and replace ___ by a function name to assign value "19" to name20. 
    Ask yourself: Is "19" a string or a number?
"""
# name20 = ___(name7)

"""4.3 - Uncomment the next line and replace ___ by a function name to assign value 2 to name21. 
    Ask yourself: What base is used here? Can you guess it?
"""
# name21 = int("10", ___)

"""4.4 - Uncomment the next line and replace ___ by a function name to assign value 144 to name22. 
    Ask yourself: Did you notice that the reverse of rotor is rotor?
"""
# name22 = int(str(name10)[___])


## 5 - You get out of the swamp without too much damage.
##     Your steps lead you up the hills into a deep forest.
##     Prepare to meet the Elves who think in funny ways...
##     Well, that's functional programming.

"""5.1 - Remove the pass statement in the next function and complete it. One line should be enough.
    Ask yourself: How do you know if a number is even? Which mathematical operator to use here?
"""
def is_even(x):
    """Return True if x is even, False otherwise"""
    pass

"""5.2 - Remove the pass statement in the next function and complete it.
    Ask yourself: Is there a way to write it in one line?
"""
def lesser(x, y):
    """Returns 1 if x is strictly less than y"""
    pass

"""5.3 - Remove the pass statement in the next function and complete it.
    Ask yourself: Are conditionals in the right order? It may be important.
"""
def decide(x, y, z):
    """Returns :
        -1 if x < y
        0 if y <= x <= z
        1 if x > z
    Raise an error if y > z
    """
    pass

"""5.4 - Remove the pass statement in the next function and complete it.
    Ask yourself: Where can you find the formula to convert Farenheit degrees in Celsius degrees?
"""
def to_celsius(t_far):
    """Convert Farenheit degrees in Celsius degrees"""
    pass

"""5.5 - Remove the pass statement in the next function and complete it.
    Ask yourself: Where can you find the formula to convert Celsius degrees in Farenheit degrees?
"""
def to_farenheit(t_cel):
    """Convert Celsius degrees in Farenheit degrees"""
    pass
