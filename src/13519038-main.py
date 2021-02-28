import string
import os.path
topoSort = __import__('13519038-toposort')

def bacaInput(inputFile):
    
    #Input File
    f = open(os.path.dirname(__file__) + '/../test/' + inputFile)
    #Deklarasi list matkul dan prereq
    daftar_matkul_dan_prereq = []
    
    for x in f:
        #Menjadikan list matkul dan prereq ke list 2D
        daftar_matkul_dan_prereq.append(x.strip().split('>'))
    
    x = daftar_matkul_dan_prereq
    #Menghilangkan punctuation
    x = [''.join(c for c in s if c not in string.punctuation) for s in x]
    
    daftar_matkul_dan_prereq2 = []
    for i in x :
        #Menghilangkan "\n"
        daftar_matkul_dan_prereq2.append(i.strip())

    daftar_matkul_dan_prereq3 = []
    for x in daftar_matkul_dan_prereq2:
        #Menghilangkan "." dan memisahkan elemen dengan ","
        y = x.replace(".", "").replace(" ", "").split(",")
        daftar_matkul_dan_prereq3.append(y)

    #return array matkul final
    return daftar_matkul_dan_prereq3

def printRencanaKuliah():
    
    for i in range(len(topoSort.hasilTopo)):
        print("Semester", i+1, ":", end="")
        for j in range(len(topoSort.hasilTopo[i])):
            print(topoSort.hasilTopo[i][j], end=" ")
        print("\r")

def mainProgram():
    print("Masukkan nama file : ", end="")
    x = input()
    matkul = bacaInput(x)
    topoSort.pendekatanTopologicalSort(matkul)
    printRencanaKuliah()

mainProgram()
