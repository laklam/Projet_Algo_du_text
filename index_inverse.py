import os
class IndexInverse:
    """
     class Index Inverser
    """
    def __init__(self, list_url, nb_url, url_id,):
        self.index = dict()
        self.list_url = list_url
        self.nb_url = nb_url
        self.url_id = url_id

    def __contains__(self,item):
        return item in self.index

    def __getitem__(self,item):
        return self.index[item]

    #ajout d'un mot 

    def add(self, mot, url_id):
        # si le mot existe on ajoute 1
        if mot in self.index:
            if url_id in self.index[mot]:
		# dans le cas ou on a un url qui contient deja ce mot
                self.index[mot][url_id] += 1
            else:
                # un url qui n'avait pas ce mot avant
                self.index[mot][url_id] = 1
        # sinon on cree un nouveau avec pour ce mot
        else:
                d = dict()
                d[url_id] = 1
                self.index[mot] = d

    # frequence d'un mot dans un doucument

    def get_frequence(self, mot, url_id):
        if mot in self.index:
            if url_id in self.index[mot]:
                return self.index[mot][url_id]
            else:
                raise LookupError('%s est pas dans l url %s' %(str(mot),str(url_id)))
        else:
            raise LookupError('%s est pas dans index' %str(mot))

    # chargement des doucument dans l'index a partir d'un repertoire
    def chargedoucument(self, repertoire):
        self.nb_url = 0
        self.list_url = []
        for i in os.listdir(repertoire):
            self.list_url.append(i)
            self.nb_url += 1

    # fonction qui calcule la taille moyen des doucuments
    def Avdl(self, list_utl, nb_url):
        x = 0
        for i in self.nb_url:
            x += len(list_url[i])
        return float(x) / float(nb_url)
    







