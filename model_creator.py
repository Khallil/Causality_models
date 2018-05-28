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

n_steps = 4
steps = [ (0, [('CO',100)] )  , (1, [('C',100)] ) , (2, [('A',100),('B',100)] )  ,(3,[ ('D',100) ]) ]
PROB_V = 0 # Position of the probability value in actor tuple
ACTOR = 1 # Position of the actor tuple in time tuple
NAME_A = 0 # Position of the actor's name in actor tuple
TIME_N = 0 # Position of the time number
# ARG = et si le court order avait dit true

arg = 'D'
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
for 
#    on assign True à tous les éléments suivants (qui on chacun leur pourcentage de réussite)






