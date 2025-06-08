# src/pdf_cracker.py
import pikepdf
from src.core import logger, load_wordlist, print_progress, write_result_to_file


def crack_pdf(file_path, wordlist_path):
    logger(f"Memulai brute force PDF: {file_path}", level="INFO")

    passwords = load_wordlist(wordlist_path)
    total = len(passwords)

    for i, password in enumerate(passwords):
        try:
            print_progress(i + 1, total)
            with pikepdf.open(file_path, password=password):
                logger(f"\n[SUKSES] Password ditemukan: {password}", level="SUCCESS")
                write_result_to_file(f"PDF: {file_path} => Password: {password}")
                return password
        except pikepdf._qpdf.PasswordError:
            continue
        except Exception as e:
            logger(f"\n[ERROR] Gagal membuka PDF: {e}", level="ERROR")
            break

    logger("\n[!] Password tidak ditemukan di wordlist.", level="WARN")
