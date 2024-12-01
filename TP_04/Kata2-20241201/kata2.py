"""
Kata 2

“Once you've decided that something's absolutely true,
you've closed your mind on it, and a closed mind doesn't go anywhere.
Question everything. That's what education's all about.”
Belgarath the Sorcerer.
"""


## 1 - Some useless names for a new journey.
##     Where you'll see the superpowers of str.

""" 1.1 - Uncomment the next line and replace ___ to assign value "happiness" to name1. 
    Ask yourself: what is the class of name1? Easy question, isn't it?
"""
# name1 = ___

""" 1.2 - Uncomment the next line and replace ___ to assign value True to name2. 
    Ask yourself: you don't know how to do it?... Read the doc!
"""
# name2 = name1.___("happi")

""" 1.3 - Uncomment the next line and replace ___ to assign value True to name3. 
    Ask yourself: quite the same as previous, isn't it?... Read the doc again!
"""
# name3 = name1.___("ness")

""" 1.4 - Uncomment the next line and replace ___ to assign value "ness" to name4. 
    Ask yourself: If you don't know how to slice it, same answer: Read the doc!
"""
# name4 = name1[___]

""" 1.5 - Uncomment the next line and replace ___ to assign value "happi" to name5. 
    Ask yourself: you don't know how to do it?... Read the doc!
"""
# name5 = name1[___]

""" 1.6 - Uncomment the next line and replace ___ to assign value "happy" to name6. 
    Ask yourself: name5 was not correct, how can you change the last character? Can you really change it?
"""
# name6 = name5[___] + "y"

""" 1.7 - Uncomment the next line and replace ___ to assign value 9 to name7. 
    Ask yourself: how is number 9 related to name1? Quite a riddle
"""
# name7 = ___(name1)

""" 1.8 - Uncomment the next line and replace ___ to assign value "pin" to name8. 
    Ask yourself: Remember, what is the slicer format again?
"""
# name8 = name1[___]

""" 1.9 - Uncomment the next line and replace ___ to assign value 1 to name9. 
    Ask yourself: A new fonction to find your way, who can you call?... Not Ghostbusters, Documentation, Yeah!
"""
# name9 = name1.___("a")

""" 1.10 - Uncomment the next line and replace ___ to assign value "Supercalifragilisticexpialidocious" to extraname. 
    Ask yourself: What is the length of this word? 
"""
# extraname = "Super" + ___ + "fragi"+ ___ + "expiali"+ ___

""" 1.11 - Uncomment the next line and replace ___ to assign value "suoicodilaipxecitsiligarfilacrepuS" to revextra. 
    Ask yourself: What is syntactic sugar? Some sweet syntax, isn't it?
"""
# revextra = extraname[___]


## 2 - Repeat after me:
##     "All work and no play makes Jack a dull boy
##      All work and no play makes Jack a dull boy
##      All work and no play makes Jack a dull boy"
##     The Shining

""" 2.1 - Uncomment the next lines and replace all ___ to assign value 10 to name10. 
    Ask yourself: Where's the limit? 
"""
# name10 = 0
# while name10 < ___:
#     name10 += 2

""" 2.2 - Uncomment the next lines and replace all ___ to assign value 56 to name11. 
    Ask yourself: Where do we start? Where's the limit? 
"""
# name11 = ___
# i = 0
# while i <= ___:
#     name11 += 2 * i
#     i += 1

""" 2.3 - Uncomment the next lines and replace all ___ to make j goes from 0 to 50, 
          and name12 is the sum of the 51 first terms of the sequence 1,5j + 3
    Ask yourself: Do you want to use a for loop instead? You are right, but try to do it with a while loop!
"""
# name12 = ___
# ___ = 0
# while ___ < ___ :
#     name12 += ___
#     j += ___

""" 2.4 - Remove the pass statement in the next function and complete it.
          You cannot use the sum function or a for loop.
    Ask yourself: Is it really the same as the previous one? Think wisely...
"""
def name13(n):
    """
    params:
        - n: integer
    return:
        - the sum of the n first terms of the sequence 1,5j + 3
    """
    pass

""" 2.5 - Uncomment the next lines and replace all ___ to make i goes from 1 to 7 by step 1.
    Ask yourself: What is the value of name14 at the end of the loop?
                  Does name i still exists after the loop?
"""
# name14 = 0
# for i in range(___, ___, ___):
#     name14 += 2 * i

""" 2.6 - Uncomment the next lines and replace all ___ to make i goes from 2 to 14 by step 2.
    Ask yourself: What is the value of name15 at the end of the loop? Why is it the same as name14?
"""
# name15 = 0
# for i in range(___, ___, ___):
#     name15 += i

""" 2.7 - Uncomment the next lines and replace all ___ to make i goes from 1 to 20 by step 1.
    Ask yourself: Think about the growth of name16? Is it linear? Is it exponential?
"""
# name16 = 1
# for i in range(___, ___):
#     name16 += name16

""" 2.8 - Uncomment the next lines and replace all ___ to make i goes from 0 to 33 by step 1.
    Ask yourself: Think about the growth of name17? Is it linear? Is it exponential?
"""
# name17 = 1
# for i in range(___):
#     name17 += 3 * i



## 3 - You know how to repeat and to iterate?
##     The difference is still not clear perhaps...
##     Let's create strings and iterate over them to make it clear!

""" 3.1 - Uncomment the next lines and replace all ___ to assign value "0123456789" to name18.
    Ask yourself: Do you remember how to transform int to str?
"""
# name18 = ___
# num = ___
# while num < ___ :
#     name18 += ___(num)
#     num += ___

""" 3.2 - Uncomment the next lines and replace all ___ to assign value "0123456789" to name19.
    Ask yourself: Quite the same as the previous one, isn't it? But why can we use a for loop?
"""
# name19 = ___
# for num in range(___) :
#     name19 += ___(num)

""" 3.3 - Uncomment the next lines and replace all ___ to assign value "0123456789" to name20.
    Ask yourself: Still the same result? What do you think about the syntax? Read the doc about join!
"""
# name20 = "".join(__ for i in range(__))

""" 3.4 - Uncomment the next lines and replace all ___ to assign value False to name21.
    Ask yourself: What is the value of digit at the end of the loop?
"""
# name21 = True
# for digit in "8935728194592343O541":
#     if ___ not in name20:
#         name21 = ___
#         break

""" 3.5 - Uncomment the next lines and replace all ___ to assign value "122333444455555" to name22.
    Ask yourself: Is there a way to simply repeat the same character several times instead of using for loop?
"""
# name22 = ""
# for i in range(___, ___):
#     for j in range(i):
#         name22 += str(___)


""" 3.6 - Uncomment the next lines and replace all ___ to assign value "12345" to name23.
    Ask yourself: Think deeply about what is asked here. Why the last line is needed?
"""
# name23 = ""
# for i in range(___(name22)-1):
#     if name22[___] != name22[___]:
#         name23 += name22[i]
# name23 += name22[___]

""" 3.7 - Uncomment the next lines and replace all ___ to assign value 7 to name24.
    Ask yourself: This works only to count "i", How can you functionalize to take any character as input?
"""
# name24 = 0
# for ___ in extraname:
#     if char == "i":
#         name24 += ___

""" 3.8 - Uncomment the next lines and replace all ___ to assign value 7 to name25.
    Ask yourself: Is there a function already counting characters in a string?
"""
# name25 = extraname.___("i")



## 4 - Now you need to apply what you learned to a real problem!
##     DNA is just text and we can do a lot of things with it!
##     Let's create some useful functions on DNA sequences.

"""4.1 - Remove the pass statement in the next function and complete it.
    Ask yourself: Does it remind you of a previous exercise?
"""
def is_dna(seq):
    """Check if a sequence contains only valid DNA bases ATCG"""
    pass

"""4.2 - Remove the pass statement in the next function and complete it.
    Ask yourself: Can you concieve different ways to do this? 
    Try with while loop, then with for loop, then with join maybe.
    And another try with a str function if you find it.
"""
def dna2rna(seq):
    """Translate dna to rna, replace T by U"""
    pass

"""4.3 - Remove the pass statement in the next function and complete it.
    Ask yourself: Can you concieve different ways to do this?
"""
def rev_comp(seq):
    """Generate the reverse complement of a sequence"""
    pass
