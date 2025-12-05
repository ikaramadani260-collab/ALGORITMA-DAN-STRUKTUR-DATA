#Nama   : Ika Ramadani
#NIM    : D0425325
#Kelas  : B Sistem Informasi

# Array 1D: Daftar Nilai Siswa
nilai_siswa = [90, 75, 88, 92, 70]

# Mengakses elemen pada indeks ke-2
# (yaitu nilai 88, karena indeks dimulai dari 0)
print(f"Nilai Siswa Kedua: {nilai_siswa[2]}")

# Array 2D: Data Nilai 3 Siswa untuk 2 Mata Pelajaran (Baris x Kolom)
# [  [MTK, IPA], [MTK, IPA], [MTK, IPA]  ]
data_nilai_matriks = [
    [80, 95],  # Siswa 1
    [75, 88],  # Siswa 2
    [92, 79]   # Siswa 3
]

# Mengakses nilai IPA (Kolom 1) milik Siswa 2 (Baris 1)
nilai_ipa_siswa_2 = data_nilai_matriks[1][1] 
print(f"Nilai IPA Siswa 2: {nilai_ipa_siswa_2}")

# Array 3D: Data Nilai Siswa di 2 Kelas, dengan 2 Mata Pelajaran
data_3d = [
    # Halaman 0: Data Kelas A
    [
        [90, 85], # Siswa 1 (MTK, IPA)
        [70, 75]  # Siswa 2 (MTK, IPA)
    ],
    # Halaman 1: Data Kelas B
    [
        [95, 88], # Siswa 3 (MTK, IPA)
        [80, 92]  # Siswa 4 (MTK, IPA)
    ]
]

# Mengakses Nilai MTK (Kolom 0) milik Siswa 3 (Baris 0) di Kelas B (Halaman 1)
nilai_mtk_kelas_b = data_3d[1][0][0]
print(f"Nilai MTK Siswa 3 (Kelas B): {nilai_mtk_kelas_b}")