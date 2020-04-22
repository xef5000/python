import random

Mots = ["roi", "lionne", "pilote", "cinq", "micro"]
mot = random.choice(Mots)
num = len(mot)
progression = "_ " * num
print("C'est un mot a {} lettres. ".format(num))
tour = 6
win = False
lettretrouves = 0
LettreUtilises = []
while tour != 0 and win == False:
  if lettretrouves == num:
      win = True
  print("\n")
  print(progression)
  a = input("Ecrivez une lettre: ")
  if a in LettreUtilises:
    print("Vous avez deja ecrit cette lettre.")
  elif a not in LettreUtilises:
    LettreUtilises.append(a)
    if a in mot:
      for position,lettre in enumerate(mot):
        if lettre == a:
          print("{0} est dans le mot dans la position {1}".format(a, position+1))
          progression = progression[:position*2] + lettre + " " + progression[(position+1)*2:]
          lettretrouves += 1
          if lettretrouves == num:
            win = True
          tour -= 1
          print("Il vous reste {} tour(s)".format(tour))
    else:
      print("{} n'est pas dans le mot".format(a))
      tour -= 1
      print("il vous reste {} tour(s)".format(tour))   

print("Bravo, tu as trouve le mot!")


