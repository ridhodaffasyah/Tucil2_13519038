global hasilTopo, simpan_matkul
hasilTopo = []
simpan_matkul = []

def pilihHapusSimpulDerajatNol(list_matkul):

    derajat_simpul = []
    for x in list_matkul:
        if (len(x) == 1):
            derajat_simpul  = 0
            #derajat simpul nol dapat dihitung dari (len(x))

    simpul_derajat_nol = []
    
    for x in list_matkul:
        if (len(x) == derajat_simpul+1):
            #simpan simpul berderajat nol
            simpul_derajat_nol.append(x[0])
            #tempat simpan matkul sementara
            simpan_matkul.append(x[0])
                
    #Hapus simpul yang berderajat nol (matakuliah tanpa prereq) dari list matakuliah
    for x in simpul_derajat_nol:
        list_matkul.remove([x])

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
    for j in range(len(simpan_matkul)):
        for y in list_matkul:
            if (y.count(simpan_matkul[j]) == 1):
                    y.remove(y[y.index(simpan_matkul[j])])

    #basis jika sudah tidak ada matakul yang harus diambil
    if (len(list_matkul) == 0):
        return
    else :
        #rekursif
        #Ulangi langkah (2) dan (3) hingga semua simpul pada DAG terpilih.
        pendekatanTopologicalSort(list_matkul)
