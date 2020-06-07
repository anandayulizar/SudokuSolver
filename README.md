# Sudoku Solver

Tugas ini dibuat untuk memenuhi tugas seleksi Asisten Lab IRK Teknik Informatika ITB angkatan 2018.

## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.

## Cara Menjalankan Program
Berikut merupakan langkah-langkah untuk menjalankan dalam sistem operasi Windows:
1. Buka directory dari repository ini
2. Jalankan command berikut:
```
cd src
python main.py
```
Ikuti perintah yang terdapat dalam program

## Prerequisites
Berikut merupakan daftar prerequisite yang dibutuhkan pada program ini. Versi yang tertera merupakan versi yang digunakan author saat pembuatan program ini. 
* python 3.8.3
* pip 20.1.1
* PIL 7.1.2
* pyteserract 0.3.4


## Installing
**Install python**, Untuk install python, dapat mengunjungi [Website Python](python.org) dan download versi yang bersangkutan

**Install pip**,
1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
2. Jalankan command ini di dalam folder dimana get-pip.py berada
```
python get-pip.py
```

**Install Library**
1. Install tesseract melalui https://github.com/UB-Mannheim/tesseract/wiki
2. Simpan path dari tesseract yang di-install. Path default adalah: ``` C:\Users\[NAMA-USER]\AppData\Local\Tesseract-OCR ```. Perhatikan bahwa dalam kasus saya adalah ```C:\Program Files\Tesseract-OCR\tesseract.exe```
3. Jalankan command berikut dalam cmd
```
pip install pytesseract
```
4. Ubah ```pytesseract.pytesseract.tesseract_cmd``` pada ```fileHandler.py``` sesuai dengan path teserract anda

Keterangan: Library PIL automatis di-install saat install tesseract karena itu merupakan salah satu requirementnya

## Strategi Pencarian Solusi
Dalam mencari solusi, program ini menggunakan algoritma backtracking dengan memanfaatkan rekursif sebagai strategi utamanya. Algoritma heuristik akan mengecek setiap kotak yang masih kosng satu per satu dan menempatkan angka secara urut yang available pada kotak tersebut, lalu lanjut ke kotak berikutnya. Apabila kotak berikutnya tidak bisa menempatkan angka apapun, maka akan terjadi backtracking ke kotak sebelumnya dan akan menempatkan angka berikutnya yg available. Proses ini akan terus berulang hingga menemukan solusi dengan asumsi bahwa setiap test case memiliki solusinya. 

Untuk mempercepat keberjalanan algoritma, dilakukan optimisasi dengan mencatat candidate-candidate yang dapat ditempatkan (tidak terdapat nomor yang sama dalam row, column, atau subgrid yang sama) untuk setiap kotak yang masih kosong. Dengan begini, dalam pelaksanaan backtracking penempatan angka tidak akan mencoba dalam seluruh rentang 1-9 tetapi hanya yang masih memungkinkan saja sehingga mempersingkat pelaksanaan algoritma. Selain itu, diterapkan strategi naked single, yaitu sebuah kotak yang hanya memiliki 1 candidate akan di-assign dengan candidate tersebut terlebih dahulu, sebelum memulai algoritma backtracking sehingga simpul yang dibangkitkan dalam backtracking berkurang.

## Alasan Pemilihan Library
#### pyteserract
Pytesseract merupakan library OCR (Optical Character Recognition) yang paling populer di python sehingga merupakan pilihan utama saya dalam mengambil puzzle dari file gambar. Kelebihan yang saya rasakan antara lain merupakan penggunaannya yang mudah dan dokumentasinya yang banyak dibahas di internet (stackoverflow dsb) sehingga mempermudah saya dalam menggunakannya untuk pertama kali. Kekurangannya ada di sisi download yang membutuhkan langkah lebih banyak dari library biasanya. Saya belum menemukan kekurangan lain dalam penggunaan pytesseract sejauh ini.

#### PIL
PIL (Python Imaging Library) atau Pillow dalam versi baru, merupakan library yang digunakan untuk membuka, memanipulasi dan menyimpan gambar. Saya menggunakan library ini untuk memproses gambar puzzle sudoku karena ia merupakan salah satu requirements dari Library pytesseract sehingga mempersingkat waktu dalam install library (istilahnya sekalian). Kelebihannya adalah penggunaannya yang relatif mudah karena hal yang dibutuhkan dalam program ini hanya load dan crop gambar untuk dibaca oleh library pytesseract sehingga sesuai untuk penggunaan program ini. Kekurangannya dibanding library yang sejenis yaitu OpenCV adalah PIL tidak memiliki fungsionalitas seluas OpenCV, tetapi untuk tugas ini sudah lebih dari cukup.

Alternatif lain adalah OpenCV. Pada awalnya saya mencoba menggunakan OpenCV dan berencana untuk mengambil data puzzle dari gambar dengan cara detect kotak-kotak yang terdapat pada puzzle. Namun, karena saat melakukan treshold pada gambar susah didapatkan hasil yang baik untuk diproses, sehingga saya beralih ke strategi crop setiap kotak. Karena strategi ini bisa dilakukan oleh PIL, maka saya beralih menggunakan PIL.

## Referensi
Berikut merupakan referensi yang membantu saya dalam mengerjakan Program ini
[1] https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e
[2] https://www.youtube.com/watch?v=b123EURtu3I
[3] Jawaban Blckknght dalam https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
[4] https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
    
Info lebih jelas mengenai spesifikasi tugas dapat dilihan pada Repository yang saya fork