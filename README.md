# Causality_models

2 solutions

1. For each actor we do a random based on his probability, if succeed we continue the chain otherwise we killed the actor
2. For each actor we add each of the probability and we continue the chain if the value is under 50

manque_argent 70  chef_mort 10   mauvaise_reputation 20 

faillite d'un restaurant

que se passe t'il si il manque de l'argent ?
-> total > 50 alors faillite du restaurant

que se passe t'il si le chef meurt et que le restaurant a une mauvaise reputation
-> 10 + 20 = 30 < 50 alors pas faillite du restaurant

tireur_A 90     tireur_B 90    tireur_C 90
            
            mort de la cible

que se passe t'il si le tireur_A tire ?
-> total > 50 donc le cible va mourir

Ne pas tomber dans le piège de la probabilité, qui
nous bloque au stade 1 du ladder et nous fait penser que nous
vivons dans un monde statique.
La causalité n'est pas pris en compte dans le Bayesian Network