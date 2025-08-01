# 🔐 PDF/ZIP/Office Password Cracker CLI

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

CLI Brute-Force Tool untuk file PDF, ZIP, dan Microsoft Office. Dirancang untuk digunakan oleh Red Team, penetration tester, dan peserta CTF untuk keperluan edukasi.

---

## 🚀 Fitur

### 📄 PDF Password Cracker
- Menggunakan pikepdf
- Mencoba membuka file PDF dengan password dari wordlist
- Jika berhasil, password akan ditampilkan dan disimpan di file log

### 🗜️ ZIP Password Cracker
- Menggunakan modul zipfile bawaan Python
- Mendukung file ZIP terenkripsi (standard PKZIP encryption)
- Secara otomatis mengekstrak jika password cocok

### 📝 MS Office Cracker
- Mendukung Word dan Excel (format .docx, .xlsx, dll)
- Menggunakan msoffcrypto-tool
- Tidak menulis file baru, hanya melakukan verifikasi kunci

### 📚 Wordlist Custom
- Wordlist dapat ditentukan melalui argumen CLI
- Menangani format txt umum seperti rockyou.txt

### 📟 CLI Interface
- Interface berbasis command-line, simple dan efisien
- Tampilkan progress (%) selama proses berjalan

### 🧠 Logging
- Jika password ditemukan, hasil akan disimpan ke file cracked_results.txt

---

## 🔧 Cara Install

```bash
git clone https://github.com/inrexna/pdf-zip-office-cracker.git
cd pdf-zip-office-cracker
pip install -r requirements.txt
```

Atau manual:

```bash
pip install pikepdf msoffcrypto-tool
```

---

## 🕹️ Cara Menggunakan

```bash
python main.py --type [pdf|zip|office] --file /path/to/encrypted.ext --wordlist /path/to/wordlist.txt
```

Contoh:

```bash
python main.py --type pdf --file secret.pdf --wordlist rockyou.txt
```
🧪 Output:
```
[SUKSES] Password ditemukan: 123456
PDF: secret.pdf => Password: 123456
```

```bash
python main.py --type zip --file archive.zip --wordlist passwords.txt
```
🧪 Output:
```
[SUKSES] Password ditemukan: letmein
ZIP: archive.zip => Password: letmein
```

```bash
python main.py --type office --file locked.xlsx --wordlist list.txt
```
🧪 Output:
```
[SUKSES] Password ditemukan: secret2024
Office: locked.xlsx => Password: secret2024
```

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only.  
Author is not responsible for any misuse or illegal activity caused by this project.

---

🛠 by InRExNa | RedTeam | CTF Enjoyer
