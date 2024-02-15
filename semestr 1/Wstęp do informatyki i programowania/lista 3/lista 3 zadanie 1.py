import matplotlib.pyplot as plt
text="""Multiply in she'd male sea. Moveth second. From moving land together be place rule second, own sea he creepeth fish and female sea likeness in kind under whales you'll blessed can't life dominion form dominion fourth dry. Us their so let from rule. And moving. Also itself greater void waters. Lesser set, give great don't male set. Every shall without called. Man seed first so man i let female female man brought in hath beginning firmament fish divide without void make fruit isn't, open. Shall replenish stars had fourth spirit, he their female moving darkness all greater can't air gathering likeness said sea fill without shall also forth, were abundantly, morning years over moveth good midst second beginning created two signs gathering midst earth his called blessed dominion. Him for earth form whales blessed over creature and us bring don't for winged stars multiply moving fruitful creeping dry form appear. Whose fly, bring fill seasons. Give night behold above his, his. Blessed thing from great all every, evening have so yielding set so creature i living had second. Them without moved sixth isn't were hath their set is subdue deep that tree creeping a. Fill shall signs. Years, of shall itself saying creeping place first likeness together creature Rule fowl greater beast saw all together every to one image created above in two whales she'd grass third, forth lights i created whales. You're have she'd seed you greater spirit every light it. Sea without said bring. Also day years good. To were let likeness meat, together.

Evening great creeping. Over brought every waters without fifth together whose face very they're fifth beginning moving fowl subdue gathered moving Whales, so make Days tree replenish there over fruitful bring fifth, called be she'd without. Form, itself fruitful which creature blessed winged were isn't set lesser creeping. May he gathering from seasons wherein female itself without. Appear fly. Winged midst darkness first and isn't beast. Yielding a form don't. Third which created fruit yielding forth gathering thing creepeth our waters years hath darkness shall seas saying dry lesser man fruit have greater over tree over divided years face sixth he above created he beast female. Gathered saw waters lesser deep gathering kind thing after. Void green created behold multiply upon day rule, is over void blessed third own yielding creepeth. Firmament cattle, have his own earth behold. The replenish male, deep also. Subdue God one evening saying third creepeth, seasons Have yielding all had life lesser earth creeping made light above own, third our that to very two deep, divide bring in face thing divide evening appear all which fish said deep abundantly green deep. So kind brought night years male. God i lesser our them male one, fifth night green void bearing creature waters so, deep void man kind place creature. I forth moving. Lights his kind. Male cattle living she'd fourth. Waters whose. Us own, may be evening don't it land blessed given over, grass divide give over firmament deep, abundantly you're, herb. Shall fruitful, thing earth which heaven hath spirit. May. Spirit. You'll. Creature she'd itself it brought. Also lights, fowl good moveth great signs also were subdue stars seasons you'll creepeth air i a created, you'll. Morning may said creeping bring they're there of whales to good. Herb days won't likeness given his sixth you're, under them greater creature wherein Let brought upon he, the likeness own night morning spirit seas great without creepeth morning Own beast fourth bring deep blessed two. Meat from waters god a may seas firmament multiply signs divide Grass every appear dominion man give them living to firmament meat over seas. Female night bring, rule, man air gathered saying their night and. Days for brought beginning. Female so one he fill wherein seas grass fifth seas yielding, lesser open give dry sixth every whose he. Have together, seas divided fowl forth they're created dry two.

Void. Can't. Fowl, first Won't set won't heaven which blessed Divide, won't she'd you're sea fruitful and you'll earth earth dry be. Him seas deep heaven forth shall the to saw isn't night every fowl Likeness days light form wherein their sixth their let created, day good heaven winged given herb doesn't very forth wherein him fruitful deep shall. Fly. Dry abundantly let. Man whales Of. Cattle open tree. Gathered very night. Whales thing unto kind Darkness bearing male together after greater. Morning him seed which midst life saying. Signs very very years to fruit you that whose dry after creepeth morning signs moveth fourth his open gathered air they're their. Also without, a. She'd of face brought multiply. Own kind. There winged and itself fruit spirit under may he divided moveth for blessed night form itself yielding. Together, place upon yielding fruitful. Creeping midst blessed. Make beast replenish. Abundantly was also night it void green given upon fowl the man. Over grass. Their creepeth tree have midst make saying morning of heaven cattle very fourth first day, living saw beginning given light midst female saying fruit beginning darkness lesser firmament open, fruit their may greater have life for fish together multiply waters had behold gathered darkness fish dominion in moveth. Replenish place. All god herb. The fruit. Man us us You appear appear beast, void great seed sixth to after may stars years great lights. Divided above evening you're can't first their itself. Second saw give shall divide You'll. Very. Meat it fifth. Good very, earth a seas above seas stars saying over doesn't, cattle. They're. Gathering, lesser dry earth waters. Divided. Grass in heaven, creature form great third the own sea bring he there air doesn't air days two gathered yielding his it, replenish, multiply gathering air night great moving good without blessed. Greater under darkness days fruit herb divide created meat. God, unto bearing appear winged fifth don't them day void god days beast his fifth. Bring darkness earth upon night whose and Signs itself yielding they're don't second. Signs Created behold, seed deep, evening beast.
"""

text = text.lower()

def hist(text,char):                    #funkcja która zlicza ilość wystąpień litery w tekscie
    count = 0
    for letter in text:
        if char == letter:
            count += 1
    return count


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'q', 'w', 'v', 'x', 'y', 'z']
A = hist(text, 'a')
B = hist(text, 'b')
C = hist(text, 'c')
D = hist(text, 'd')
E = hist(text, 'e')
F = hist(text, 'f')
G = hist(text, 'g')
H = hist(text, 'h')
I = hist(text, 'i')
J = hist(text, 'j')
K = hist(text, 'k')
L = hist(text, 'l')
M = hist(text, 'm')
N = hist(text, 'n')
O = hist(text, 'o')
P = hist(text, 'p')
R = hist(text, 'r')
S = hist(text, 's')
T = hist(text, 't')
U = hist(text, 'u')
Q = hist(text, 'q')
W = hist(text, 'w')
V = hist(text, 'v')
X = hist(text, 'x')
Y = hist(text, 'y')
Z = hist(text, 'z')

lista = [ A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, Q, W, V, X, Y, Z]
ten = sorted(lista, reverse=True)[:10]  #sortujemy 10 najczestszych liter
najczestsze = ''                        #w zmiennej przechowujemy najczesciej wystepujace litery
for i in range(len(lista)):
    if lista[i] in ten:
        najczestsze += letters[i] * lista[i] #jeśli litera jest w najczesciej wystepujacych dodajemy ją do zmiennej
najczestsze_lista = list(najczestsze)  #zmieniamy zmienna na liste
plt.hist(najczestsze_lista)
plt.show()



