import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  


library_data = [
    {"Nama": "NIHA NUR MAYLA PUTRINIPD", "NIPD": "24031554057", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "REFOCHELLA FLORENTINE GWACEVO PERTIWINIPD", "NIPD": "24031554045", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "SYAFIRA NAJEMA PUTRI ANISA", "NIPD": "24031554013", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HULWAH FATIN FATHINAHNIPD", "NIPD": "24031554007", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    
    {"Nama": "IVAN CAHYA ARYASUTA", "NIPD": "24031554172", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FAUZAN RAFINGUDIN", "NIPD": "24031554111", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "AHMAD DHANI ALFAWWAS", "NIPD": "24031554096", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "WAHYU PRASETYONO", "NIPD": "24031554133", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MARIA AGATHA METRI TETRAJATI", "NIPD": "24031554189", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "SAVITRI RAHMANING LUKITO", "NIPD": "24031554219", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "KEVIN FEBRIAN WIDHIARTA", "NIPD": "24031554025", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "RAFAEL HARTONO", "NIPD": "24031554166", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "UMI IMRO'ATUS SHOLEKHAH", "NIPD": "24031554150", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "FRELIN THERESIA PANIA", "NIPD": "24031554220", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NA'ILLAH SHANIA RIZQILLAH", "NIPD": "24031554225", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DIVA IZZA MANSYATHIKA", "NIPD": "24031554217", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "SALSABILA ALIKA SEFTIZIANKA", "NIPD": "24031554117", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NAJMU TSAQIB ARSALAN", "NIPD": "24031554026", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "DAFFA AHMAD PANGREKSA", "NIPD": "24031554159", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "SILVIA TRI MAHARANI", "NIPD": "24031554028", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "AHNAF FARHAN SYIHABUDDIN", "NIPD": "24031554101", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Mengundurkan diri"},
    {"Nama": "AYDA' NUR SALZABILLAH", "NIPD": "24031554017", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "GRACE PINKKAN LADYNA", "NIPD": "24031554137", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ANGGORO DARU PRASETYO", "NIPD": "24031554070", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "VINCENTIUS PUTRA MAHARDIKA", "NIPD": "24031554110", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "SABRINA MIFTAKHUL JANA", "NIPD": "24031554148", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "STELLA DAGATHA", "NIPD": "24031554080", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "FINA NIHAYATUL HUSNA", "NIPD": "24031554022", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HIDAYATUR RAHMAWATI", "NIPD": "24031554038", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ALIFIYANTI PUTRI NUR AZIZAH", "NIPD": "24031554032", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "GITA NURANI", "NIPD": "24031554122", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD KHOIRUL ILHAM", "NIPD": "24031554193", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "NABILLA HILMI ROSANTI", "NIPD": "24031554053", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "VARIESA SABITA MUMTAZA HABIB", "NIPD": "24031554083", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HALIMATUS SA'DIYAH", "NIPD": "24031554075", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DIAN ROHMATUL ISLAM", "NIPD": "24031554047", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DIYANTI PRATIWI", "NIPD": "24031554016", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ARIMBI DEBY SETYONINGRUM", "NIPD": "24031554186", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "SHOLIKIN", "NIPD": "24031554098", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MUSLIM FAZLUR ROHMAN. NIPD", "NIPD": "24031554154", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FAIZAH KHASIFA SALSABILA", "NIPD": "24031554056", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ROBBY IBRAHIMOVIC", "NIPD": "24031554010", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "GUNTORO SATRIAJI", "NIPD": "24031554103", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "DARISTA WARDHANI", "NIPD": "24031554146", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "AUDY ALYCIA", "NIPD": "24031554179", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ANANDA KEISSA AZ ZAHRA", "NIPD": "24031554051", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUTIARA NUR FADHILATUN NI'MAH", "NIPD": "24031554116", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "CHAESAR GIVESON", "NIPD": "24031554058", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "HALILATUNNISA", "NIPD": "24031554130", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HORASIO NISSI IMMANUEL", "NIPD": "24031554068", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "AISYAH IMANI KHOIRUNNISA", "NIPD": "24031554020", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "AFIFAH", "NIPD": "24031554202", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NAUFALAT'ARIQ RAMADHANI OKTAVA PUTRA YUDA", "NIPD": "24031554178", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ILLONA ANINDYA", "NIPD": "24031554222", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NAUFAL SHALIH", "NIPD": "24031554140", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FRIDANIA NISA CALITA", "NIPD": "24031554208", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ARYA ABDI WICAKSANA", "NIPD": "24031554224", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ELVIRA TIARA SUCI TAMBUNAN", "NIPD": "24031554213", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MEIDA RIFA ALFIANI", "NIPD": "24031554139", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "TAMAELA NURANDYAPASA", "NIPD": "24031554044", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "FRENDY ZAHRIL RAMADHANI", "NIPD": "24031554187", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MYLOVIA MAHESA AYU", "NIPD": "24031554001", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NURI MAULIDYATUL HALIZA", "NIPD": "24031554160", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DHIVA AURELYA RYVALDHINA", "NIPD": "24031554151", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Mengundurkan diri"},
    {"Nama": "NAURA KANAYA PUTRI MASRURI", "NIPD": "24031554138", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "M SHIDQI SHARIM ARRASYID", "NIPD": "24031554201", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MARCELLA NURUSSYIFA", "NIPD": "24031554078", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "SOFIA DWI KINASIH", "NIPD": "24031554079", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ALYA UMMI FARICHA", "NIPD": "24031554123", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "LUCKY SURYA REVANSYAH", "NIPD": "24031554090", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD ZAIDAN AL ANWARY", "NIPD": "24031554124", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMAD FADLY SYAIFULLAH", "NIPD": "24031554173", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ASTRID SEPTYA REGITA PRAMESTY", "NIPD": "24031554171", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ZAHRA BRILLIANTY PUTRI", "NIPD": "24031554014", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "AYU WULAN ANGGRAENI PUTRI", "NIPD": "24031554177", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DIMAS RAFI IZZULHAQ", "NIPD": "24031554084", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "KEVIN FOREMAN HUTAHAEAN", "NIPD": "24031554095", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ILMIN NUR LAILIYAH", "NIPD": "24031554135", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMAD ARIEF AFANDI", "NIPD": "24031554181", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "CELINE NURHIDAYAH SANTOSO", "NIPD": "24031554033", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "IN'AM CAVAN RIJAL MUSYAFA", "NIPD": "24031554184", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "APRILIA SAFNA ANGGRAENI", "NIPD": "24031554003", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "BIMA SENANIPD", "NIPD": "24031554214", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FAJAR SYIHABUDDIN", "NIPD": "24031554142", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FIO ULAA' OCTRIYANTI", "NIPD": "24031554030", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "REBRIANE ATITHA GINTING", "NIPD": "24031554039", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "RIFALDA SALMA", "NIPD": "24031554015", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ARIF RAHARJO", "NIPD": "24031554221", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "LUTHFIANA SYAKIRA EKA RAMADANI", "NIPD": "24031554071", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NASLIYATUL INTANI", "NIPD": "24031554097", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "YAZID HUSAIN ABDURRAHMAN", "NIPD": "24031554076", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "EKA PUTRI MAHARANI", "NIPD": "24031554121", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ULFIA NURMALIZHA RAMADHANI", "NIPD": "24031554064", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HELYAS DWI PRAYOGA", "NIPD": "24031554134", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "NABIL PUTRA YUAN", "NIPD": "24031554126", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "HIDAYAH ATMA NEGARA", "NIPD": "24031554169", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD ARIFIN ILHAM", "NIPD": "24031554005", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "CUT AZZAHRA FIRDAUSI SYAKIENA NAZWAN", "NIPD": "24031554180", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "M. HABIBURROHMAN AL-FATHIR", "NIPD": "24031554145", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FAWAZUL 'AMMAR", "NIPD": "24031554136", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ATHIYYATUS SALISAH", "NIPD": "24031554223", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "HERLIN SALWA FADHILAH", "NIPD": "24031554197", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ARYANTI INDAH LESTARIN", "NIPD": "24031554196", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MARIS AL SABINA AZZUHRA", "NIPD": "24031554188", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ROYHAN JINAN RAMADLAN", "NIPD": "24031554167", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "SHAKYLA ANDHARA CHANDRANINGTYAS", "NIPD": "24031554199", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},  {"Nama": "MUHAMMAD ARIEF FIRMANSYAH", "NIPD": "24031554059", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "RAFIF FADHILLAH PUTRA ZAINUR", "NIPD": "24031554185", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ANDIKA FEBRIANTO", "NIPD": "24031554018", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD RAFFI FAHREZI", "NIPD": "24031554100", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "TARA TABRIZA RACHMAN", "NIPD": "24031554107", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD GERALLDO AGATHA SAPUTRA", "NIPD": "24031554091", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "KARTIKA NUR SAVIRA", "NIPD": "24031554049", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "FAWWAZ AZRI MANSHUR PRASETYA", "NIPD": "24031554074", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "EKA DWI WIDAYANTI", "NIPD": "24031554114", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Mengundurkan diri"},
    {"Nama": "CINTIYA AGUSTIN NARESWARI", "NIPD": "24031554218", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "LAILI NURROHMATUL FADHILA ZULFA", "NIPD": "24031554093", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DARIS IKHWANA KHOIR SUHAYAN", "NIPD": "24031554215", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "NADIA KAILANIPD", "NIPD": "24031554109", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ALFIN JAYADINIPD", "NIPD": "24031554082", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MOHAMMAD TYAS SUBIANTONIPD", "NIPD": "24031554077", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "IVAN ANDIKA SETYAWANNIPD", "NIPD": "24031554085", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "SITI AISYAH FEBRIYANTINIPD", "NIPD": "24031554158", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "AGNES CLAREN APRIANY MAUKNIPD", "NIPD": "24031554212", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ADISTI EKA NABILANIPD", "NIPD": "24031554119", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "RAHMAWATI DIAN PRATIWINIPD", "NIPD": "24031554183", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "FAISHAL MUFLIH IRFANU TSAQIBNIPD", "NIPD": "24031554170", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "RUTHTATIA GRACE ASTRIDIANIPD", "NIPD": "24031554072", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "DEWANGGI ERCHINTA DWI PUTRINIPD", "NIPD": "24031554034", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NAJWA AYU RAMADHANINIPD", "NIPD": "24031554168", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "MUHAMMAD ZIKRI WIDIANDRANIPD", "NIPD": "24031554088", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "ABDULLAH AL-FIRDAUS NUZULANIPD", "NIPD": "24031554008", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "MUFID FEBRIYAN AL FAIZNIPD", "NIPD": "24031554006", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "DESSY SAPUTRINIPD", "NIPD": "24031554190", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "ODILE FEBRIANTI GELANGNIPD", "NIPD": "24031554155", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "LINTANG ISA MARDANINIPD", "NIPD": "24031554104", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"},
    {"Nama": "FAUZIAH ROIKHANA WARDAHNIPD", "NIPD": "24031554162", "Jenis Kelamin": "Perempuan", "Status Keaktifan": "Aktif"},
    {"Nama": "NAZRIL RAVI PRATAMANIPD", "NIPD": "24031554129", "Jenis Kelamin": "Laki - Laki", "Status Keaktifan": "Aktif"}, 


]

def search_data():
    keyword = entry.get()
    
    
    if not keyword.strip():  
        messagebox.showwarning("Peringatan", "Silakan masukkan kata kunci pencarian.")
        return 

    results = []
    for row in library_data:
        if keyword.lower() in str(row).lower():
            results.append(row)

    for row in tree.get_children():
        tree.delete(row)

    if results:
        for index, row in enumerate(results, start=1):
            tree.insert("", "end", values=(index, row['Nama'], row['NIPD'], row['Jenis Kelamin'], row['Status Keaktifan']))
    else:
        tree.insert("", "end", values=("Tidak ada data yang ditemukan", "", "", "", ""))

class daftar_menu:
    def __init__(self, root):
        self.root = root
        self.create_menu()  

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        profile_menu = tk.Menu(menubar, tearoff=0)
        profile_menu.add_command(label="menu", command=self.show_profile)
        profile_menu.add_separator()
        profile_menu.add_command(label="Keluar", command=self.root.quit)

        menubar.add_cascade(label="menu", menu=profile_menu)

    def show_profile(self):
        messagebox.showinfo


root = tk.Tk()
root.title("Data search")
root.geometry('925x500+300+200') 
root.configure(bg="#e0f7fa")  
root.resizable(False, False)

menu_bar = daftar_menu(root)

main_frame = tk.Frame(root, bg="#e0f7fa", padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)


label = tk.Label(main_frame, text="Masukan Nama yang Ingin Anda Cari:", bg="#e0f7fa", font=('Arial', 14, 'bold'), fg="#00796b")
label.pack(pady=10)


entry = tk.Entry(main_frame, width=30, font=('Arial', 12), borderwidth=2, relief='groove')
entry.pack(pady=10)


search_button = tk.Button(main_frame, text="Cari", command=search_data, bg='#57a1f8', fg='white', font=('Arial', 12, 'bold'), borderwidth=0)
search_button.pack(pady=10)


tree_frame = tk.Frame(main_frame)
tree_frame.pack(pady=20)


columns = ("No", "Nama", "NIPD", "Jenis Kelamin", "Status Keaktifan")
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=15)  #
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  


scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


tree.configure(yscrollcommand=scrollbar.set)


tree.heading("No", text="No")
tree.column("No", width=50, anchor="center")  
tree.heading("Nama", text="Nama")
tree.column("Nama", width=300)  
tree.heading("NIPD", text="NIPD")
tree.column("NIPD", width=150, anchor="center")
tree.heading("Jenis Kelamin", text="Jenis Kelamin")
tree.column("Jenis Kelamin", width=150, anchor="center")  
tree.heading("Status Keaktifan", text="Status Keaktifan")
tree.column("Status Keaktifan", width=200, anchor="center")  


root.mainloop()
