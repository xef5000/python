import sys
NC = 12
q1 = input("Il y a {0} cartes. Combien en piges-tu? ".format(NC))
r1 = 0
if q1 >= 4:
	print("Erreur")
	sys.exit("Error ")

r1 = 4 - q1
NC = NC - q1 - r1
print("Ok. tu retires {0} carte. Moi je Retire {1} carte. Il reste {2} cartes.\n".format(q1, r1, NC))

q2 = input("Il y a {0} cartes. Combien en piges-tu? ".format(NC))
r2 = 0
if q2 >= 4:
	print("Erreur")
	sys.exit("Error ")
r2 = 4 - q2
NC = NC - q2 - r2
print("Ok. tu retires {0} carte. Moi je Retire {1} carte. Il reste {2} cartes.\n".format(q2, r2, NC))

q3 = input("Il y a {0} cartes. Combien en piges-tu? ".format(NC))
r3 = 0
if q3 >= 4:
	print("Erreur")
	sys.exit("Error ")
r3 = 4 - q3
NC = NC - q3 - r3
print("Ok. tu retires {0} carte. Moi je Retire {1} carte. Il reste {2} cartes.\n".format(q3, r3, NC))

print("J'ai Gagne ! tu as perdu...")