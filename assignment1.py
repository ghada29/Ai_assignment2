from logic2 import*
#color(carrots, orange).
#in english:carrots color is orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge1=And(Implication(carrots,orange))
print(knowledge1.formula())

#likes(Person, carrots):-vegetarian(Person).
#in english: person like carrots if person is vegetarian
person = Symbol("person")
vegetarian = Symbol("vegetarian(person)")
like = Symbol("like")
personLikeCarrots = Symbol("like(person,carrots)")
knowledge2=And(Implication(personLikeCarrots,vegetarian))
print(knowledge2.formula())

#pass(Student) :- study_hard(Student).
#in english: student pass if student study hard
passExam = Symbol("pass(student)")
study_hard = Symbol("study_hard(Student)")
knowledge3=And(Implication(passExam,study_hard))
print(knowledge3.formula())

#?- pass(Who).
#in english: who will pass?
Pass = Symbol("?- pass(Who)")
knowledge4=And(Pass)
print(knowledge4.formula())

#?- teaches(professor, Course).
#in english:which course professor teaches?
teaches = Symbol("teaches(professor, Course)")
knowledge5=And(teaches)
print(knowledge5.formula())

#enemies(X, Y) :- hates(X, Y), fights(X, Y).
#in english: if X & Y are enemies then X hates Y and X fights Y.
enemies = Symbol("enemies(X, Y)")
hates = Symbol("hates(X, Y)")
fights = Symbol("fights(X, Y)")
knowledge6=And(Implication(enemies,And(hates,fights)))
print(knowledge6.formula())