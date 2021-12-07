from utils import*
from logic2 import*

#Maria reads logic programming book by author peter lucas.
#read(Maria,logic programming book) ==> by(peter lucas)
Maria = Symbol("Maria")
peter_lucas = Symbol("peter lucas")
read = Symbol("read(Maria,logic programming book)")
by = Symbol("by(peter_lucas)")
knowledge1=And(Implication(read,by))
print(knowledge1.formula())

#Anyone likes shopping if she is a girl
#is_girl(x) ==> likes(x,shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
likes = Symbol("likes(x,shopping)")
knowledge2=And(Implication(is_girl,likes))
print(knowledge2.formula())

#Who likes shopping?
#? likes(x,shopping)
who = Symbol("? likes(x,shopping)")
knowledge3=And(who)
print(knowledge3.formula())

#kirke hates any city if it is big and crowdy.
#city(x,big,crowdy) ==> hates(kirke,x)
city = Symbol("city(x,big,crowdy)")
hates = Symbol("hates(kirke,x)")
knowledge4=And(Implication(city,hates))
print(knowledge4.formula())
