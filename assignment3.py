from utils import*
from logic2 import*

#hates(X,Y), hates(Y,X) :- enemies(X, Y)
X = Symbol("X")
Y = Symbol("Y")
enemies = Symbol("enemies(X, Y)")
hates1 = Symbol("hates(X,Y)")
hates2 = Symbol("hates(Y,X)")
knowledge1=And(Implication(enemies,And(hates1,hates2)))
print(knowledge1.formula())


#p(X):-(q(X):-r(X)).
p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge2=And(Implication(p,And(q,r)))
print(knowledge2.formula())