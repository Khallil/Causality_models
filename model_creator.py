#coding: utf-8
# How many times steps ?
    # 4

# For each time step specify the actors, if more than 2,
# precise if their impact percentage 0%->100%
    # 0 - CO
    # 1 - C
    # 2 - (A,100) (B,100)
    # 3 - D

# Fils n Papa v Maman -> True
# Papa v Maman n Fils -> True

# Format cellule acteur : 
        #       [ n_a  n_con, prob, isActive]
steps = [   (0, [('CO',('C'),100,False)] )  , 
            (1, [('C',('B','A'),100,False)] ) , 
            (2, [('A',('D'),100,False),('B',('D'),100,False)] ) ,
            (3,[('D',100,False)]) ]
PROB_V = 0 # Position of the probability value in actor tuple
ACTOR = 1 # Position of the actor tuple in time tuple
NAME_A = 0 # Position of the actor's name in actor tuple
TIME_N = 0 # Position of the time number
# ARG = et si le court order avait dit true

arg = 'C'
def get_time_position():
    for s in steps:
        print s
        for actor in s[ACTOR]:
            if actor[NAME_A] == arg:
                print "ça return"
                return s[PROB_V]

# get the time position 
time = get_time_position()
print time

# going through the logical path
# on start from get_time
i = time
while True:    
    if i == len(steps)-1:
        print "final cause at i = ",i
        break
    else:
        for actor in steps[i][1]:
            print actor
        # on parcours chaque acteur sur la timeline 
        # et additionne la probabilité total si l'actor est a True sinon on skip
            # on lance le random sur probabilité
            # si retour == true
                # on set 
        # 
    i+=1    
    
#    on assign True à tous les éléments suivants (qui on chacun leur pourcentage de réussite)




# 20    30      50
# 51

# 50 + 50 + 50
# 91

# 50     20      30
# 50        