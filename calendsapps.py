print ("===============")
print ("    CALENDS    ")
print ("===============")

akunArray = []

while True :
    print ("Masukkan Akun")
    username = input("Username : \n")
    password = input("Password : \n")
    akunArray.append([username,password])
    
    print ("Pilih :")
    print ("1. Laporan Keuangan")
    print ("2. Kegiatan Kesehariaan")
    print ("3. Goals")
    
    pilih = input("Nomor : ")
    
    if pilih == "1" :
        barangArray = []
        print ("====================")
        print ("  LAPORAN KEUANGAN  ")
        print ("====================")
        namaItem = input("Nama Barang : \n")
        banyakItem = input("Banyak Barang : \n")
        barangArray.append([namaItem, banyakItem])
    elif pilih == "2" :
        kegiatanArray = []
        print ("========================")
        print ("  KEGIATAN KESEHARIAAN  ")
        print ("========================")
        print ("Silahkan masukkan nama kegiatan dan tanggal kegiatan")
        namaKegiatan = input("Nama Kegiatan : ")
        print ("Tanggal Kegiatan : ")
        import calendar
        import datetime
        kalender_tahun = datetime.datetime.now().year

        kalender = calendar.calendar(kalender_tahun)

        print (kalender)

        kegiatanArray.append([namaKegiatan, tglKegiatan])

