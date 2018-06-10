#coding: utf-8

steps = [   
    (0, # time
        [('CO', # actorss 
            [('C',100)] # cons_actors
            )])
    (1, 
        [ ('C',
            [('B',100),('A',100)]
            )]),         
    (2,
        [ ('A',
            [('D',100)]),
            ('B',
            [('D',100)]
        )]) ,
    (3,
        [('D',
            [] # fin de la chaine, cons_actors vides
        )])
]

PROB_V = 1 # Position of the probability value in const_actor tuple
ACTORS = 1 # Position of the actor tuple in step tuple
C_ACTOR = 1 # Position of the cons_actor in actor tuple
NAME_A = 0 # Position of the actor's name in actor tuple and cons_actor name in cons_actor tuple
TIME_N = 0 # Position of the time number

# arg = 'X' signifie, si 'X' est activé que se passe t-il ?
arg = 'C'

def get_time_position():
    for s in steps:
        print s
        for actor in s[ACTORS]:
            if actor[NAME_A] == arg:
                print "ça return"
                return s[TIME_N],actor

# get the time position 
time,actor = get_time_position()

def update_dict(dico,key,proba):
    if key in dico:
        dico[key] += proba
    else:
        dico[key] = proba

# on start depuis l'arg donné
i = time

#while True:
while i < len(steps): # pour faire des petits tests
    cons_actors = dict() # création du dict pour sauver cons_actors activé
    # on parcours etape par etape
    step = steps[i]
    # si arg
    if i == time:
        # pour chacun de ses c_actor
        for c_actor in actor[C_ACTOR]
            # si c_actor deja dans le dict
                # on ajoute la proba associé a ce c_actor a la key
            # sinon
                # on crée la key et ajoute la proba associé a ce c_actor
            update_dict(cons_actors,c_actor[NAME_A],c_actor[PROB_V])  
        # next step
        i+=1
        continue
    # si len(cons_actors) > 0 
    if len(cons_actors) > 0:
        # pour chaque acteur de la step,
        for actor in step[ACTORS]
            # si actor présent dans cons_actor
            if actor[NAME_A] in cons_actors:
                # on enleve l'actor de cons_actor
                # si sa proba est > 50
                if cons_actors[actor[NAME_A]] > 50:
                    # pour chacun de ses c_actor
                    for c_actor in actor[C_ACTOR]:
                        # si c_actor deja dans le dict
                            # on ajoute la proba associé a ce c_actor a la key
                        # sinon
                            # on crée la key et ajoute la proba associé a ce c_actor
                        update_dict(cons_actors,c_actor[NAME_A],c_actor[PROB_V])
                del cons_actors[actor[NAME_A]]                
    # sinon
        # on affiche que les acteurs de la step d'avant n'ont pas réussi a effectué l'action
    else:
        print "les acteurs de la step d'avant n'ont pas réussi a effectué l'opération"
    i+=1