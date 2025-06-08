# src/office_cracker.py
import msoffcrypto
import io
from src.core import logger, load_wordlist, print_progress, write_result_to_file


def crack_office(file_path, wordlist_path):
    logger(f"Memulai brute force Office: {file_path}", level="INFO")

    passwords = load_wordlist(wordlist_path)
    total = len(passwords)

    for i, password in enumerate(passwords):
        try:
            print_progress(i + 1, total)
            with open(file_path, "rb") as f:
                office_file = msoffcrypto.OfficeFile(f)
                office_file.load_key(password=password)
                office_file.decrypt(io.BytesIO())  # try to decrypt in memory
                logger(f"\n[SUKSES] Password ditemukan: {password}", level="SUCCESS")
                write_result_to_file(f"Office: {file_path} => Password: {password}")
                return password
        except Exception:
            continue

    logger("\n[!] Password tidak ditemukan di wordlist.", level="WARN")
