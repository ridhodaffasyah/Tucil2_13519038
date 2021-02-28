global hasilTopo, simpan_matkul
hasilTopo = []
simpan_matkul = []

def pilihHapusSimpulDerajatNol(list_matkul):

    derajat_simpul = []
    x = 0
    while (x < len(list_matkul)):
        if (len(list_matkul[x]) == 1):
            derajat_simpul  = 0
            #derajat simpul nol dapat dihitung dari (len(x))
        x+=1

    simpul_derajat_nol = []

    i = 0
    while(i < len(list_matkul)):
        if (len(list_matkul[i]) == derajat_simpul+1):
            #simpan simpul berderajat nol
            simpul_derajat_nol.append(list_matkul[i][0])
            #tempat simpan matkul sementara
            simpan_matkul.append(list_matkul[i][0])
        i+=1
                
    #Hapus simpul yang berderajat nol (matakuliah tanpa prereq) dari list matakuliah
    j = 0
    while (j < len(simpul_derajat_nol)):
        list_matkul.remove([simpul_derajat_nol[j]])
        j+=1

    #Catat mata kuliah yang derajat nol ke array 
    hasilTopo.append(simpul_derajat_nol)

def pendekatanTopologicalSort(list_matkul):
    #Representasi graf pada array 2D
    #[[simpul 1, derajat_masuk 1],
    # [simpul 2, derajat_masuk 1, derajat_masuk 2], dst]

    #kode_kuliah= simpul
    #kode kuliah prasyarat = derajat_masuk

    #Pendekatan Topological Sorting
    # 1. Dari graf (DAG) yang terbentuk, hitung semua derajat-masuk (in-degree) setiap simpul,
    #    yaitu banyaknya busur yang masuk pada simpul tersebut
    # 2. Pilih sembarang simpul yang memiliki derajat-masuk 0.
    pilihHapusSimpulDerajatNol(list_matkul)
    
    # 3. Ambil simpul tersebut, dan hilangkan simpul tersebut beserta semua busur yang keluar dari simpul tersebut pada graf.
    #dan kurangi derajat simpul yang berhubungan dengan simpul tersebut dengan 1.
    #Hapus simpul yang bersisian dengan simpul berderajat nol yang dipilih
    j = 0
    while (j < len(simpan_matkul)):
        y = 0
        while (y < len(list_matkul)):
            if (list_matkul[y].count(simpan_matkul[j]) == 1):
                list_matkul[y].remove(list_matkul[y][list_matkul[y].index(simpan_matkul[j])])
            y += 1
        j += 1
                
    #basis jika sudah tidak ada matakul yang harus diambil
    if (len(list_matkul) == 0):
        return
    else :
        #rekursif
        #Ulangi langkah (2) dan (3) hingga semua simpul pada DAG terpilih.
        pendekatanTopologicalSort(list_matkul)
