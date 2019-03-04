class FileReader():

    def __init__(self):

        with open("metin(1).txt", "r", encoding = "utf-8") as metin:

            icerik = metin.read()
            kelimeler = icerik.split()
            self.sadece_kelimeler = list()

            for f in kelimeler:

                if "’" in f:
                    f = f.replace("’", "'")

                f = f.strip(".")
                f = f.strip("\n")
                f = f.strip(",")
                
                self.sadece_kelimeler.append(f)

    
    def tumKelimeler(self):

        kelimelerKumesi = set()
        for f in self.sadece_kelimeler:
            kelimelerKumesi.add(f)

        print("TUM KELIMELER.......")

        for f in kelimelerKumesi:
            print(f)
            print("********************")

    
    def kelimeSay(self):
        kelimelerSozlugu = dict()

        for f in self.sadece_kelimeler:

            if (f in kelimelerSozlugu):
                kelimelerSozlugu[f] += 1
            
            else:
                kelimelerSozlugu[f] = 1

        for kelime, adet in kelimelerSozlugu.items():
            print("Kelime:", kelime, "adet:", adet)



belge = FileReader()
belge.kelimeSay()
