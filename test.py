#coding:utf-8

# ça retourne quoi une value de dict non trouvé ?

dico = {"prout":23,"caca":45}


def update_dict(dico,key,proba):
    if key in dico:
        dico[key] += proba
    else:
        dico[key] = proba

def delete_item(dico,key):
    del dico[key]

update_dict(dico,"prout",22)
delete_item(dico,"caca")
print dico