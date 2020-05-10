import math
k1 = 1.2
b = 0.75

#def get_frequence(mot, url_id):
#    f = 0
#    for i in list_url[url_id]:
#        f +=1

# la frequence ici sera calculer par appel a la fonction get frequence implementer dans index_inverse



# la fonction qui calcule le score BM25
def score_BM25(dl, avdl, frequence):
    return (frequence*(k1+1) ) / (frequence + (k1 * ((1-b) + b * (float(dl)/float(avdl)) )))

