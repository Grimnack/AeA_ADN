

class Mot(object):
    """docstring for Mot"""
    def __init__(self, chaine):
        super(Mot, self).__init__()
        self.chaine = chaine

    def __str__(self) :
        return self.chaine

    def __eq__(self, other) :
        return self.chaine == other.chaine

    def __hash__(self) :
        return hash(self.chaine)
        
    def reverse(self) :
        return Mot(self.chaine[::-1])

    def complem(self) :
        res = ""
        for lettre in self.chaine :
            if lettre == 'A' :
                res+='U'
            elif lettre == 'U' :
                res+='A'
            elif lettre == 'G' :
                res+='C'
            else :
                res+='G'
        return Mot(res)

    def revCompl(self) :
        return self.complem().reverse()

    def algoNaif(self,mot,normal=True,reverse=False,complem=False,revCompl=False) :
        """
        rechercher un mot dans self
        avec l'algoNaif
        """
        lesMots = []
        res = []
        #initialisation de la liste mot.
        if normal :
            lesMots.append(mot)
        if reverse :
            lesMots.append(mot.reverse())
        if complem :
            lesMots.append(mot.complem())
        if revCompl :
            lesMots.append(mot.revCompl())
        #############################
        n = len(self.chaine)
        m = len(mot.chaine)
        # i = 0
        j = 0
        for motTest in lesMots :
            for i in range(n-m+1) :
                trouve = True
                for j in range(m) :
                    if not motTest.chaine[j] == self.chaine[i+j] :
                        trouve = False
                        break
                if trouve :
                    res.append(i)

        return res

    def algoNaif2(self,mot,normal=True,reverse=False,complem=False,revCompl=False) :
        """
        rechercher un mot dans self
        avec l'algoNaif
        """
        res = []
        #initialisation de la liste mot.
        if normal :
            res.append(self.algoNaif(mot))
        else :
            res.append([])

        if reverse :
            res.append(self.algoNaif(mot, normal=False, reverse=True))
        else :
            res.append([])

        if complem :
            res.append(self.algoNaif(mot, normal=False, complem=True))
        else :
            res.append([])

        if revCompl :
            res.append(self.algoNaif(mot, normal=False, revCompl=True))
        else :
            res.append([])

    def occurencesMotsTailleN(self, N) :
        n = len(self.chaine)
        mapMot = {}
        for i in range(n-N+1) :
            mot = Mot(self.chaine[i:i+N])
            if(not mot in mapMot ):
                mapMot[mot] = [-1]
        for mot in mapMot :
            mapMot[mot] = self.algoNaif(mot)
        return mapMot

def printMapMot(mapMot):
    for key, value in mapMot.items() :
        print('key = ' + str(key) + '### value = ' + str(value) )

def printPlot(mapMot,pathname) :
    f = open(pathname,'w')
    for mot,liste in mapMot.items() :
        for i in liste :
            for j in liste :
                f.write(str(i)+'\t'+str(j)+'\n')
    f.close()



def lecture(pathname) :
    f = open(pathname,'r')
    #premiere ligne osef 
    f.readline()
    chaine = ""
    for ligne in f :
        chaine += ligne.rstrip()
    f.close()
    # print(chaine)
    return Mot(chaine)


# Test 1

# mot = Mot("ACAUAG")

# print("chaine : ACAUAG")
# print("reverse : ", mot.reverse())
# print("complem : ", mot.complem())
# print("revCompl : ", mot.revCompl())

# Test algoNaif

# mot = Mot("AA")
# text = Mot("AACGUAACGGAA")
# print("mot : ",mot)
# print("text : ", text)
# print ("occurences : ",text.algoNaif(mot))

# Test lecture

mot = lecture("data-mirna/ARNmessager-1.fasta")


mapMot = mot.occurencesMotsTailleN(6)

printPlot(mapMot,'test.plot')








