import math    
def tf(motDict, url_id):
   tfDict = {}
   nombreMots = len(list_url[url_id])
   for mot, count in motDict.items():
        tfDict[mot] = count/float(nombreMots)
   return tfDict

def idf(list_url):
    idfDict = {}
    n = len(list_url)

    idfDict = dict.fromkeys(list_url[0].keys(),0)
    for url in list_url:
        for mot,val in url.ithems():
            if val>0:
                idfDict[word] +=1

    for mot, val in idfDict.items():
        idfDict[word] = math.log10(n / float(val))

    return idfDict

def TfIdf(tf, idfs):
    tfidf = {}
    for mot, val in tf.items():
        tfidf[mot] = val*idfs[mot]
    return tfidf
