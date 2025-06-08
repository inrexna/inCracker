import zipfile
from src.core import logger, load_wordlist, print_progress, write_result_to_file


def crack_zip(file_path, wordlist_path):
    logger(f"Memulai brute force ZIP: {file_path}", level="INFO")

    if not zipfile.is_zipfile(file_path):
        logger("File bukan ZIP valid.", level="ERROR")
        return

    passwords = load_wordlist(wordlist_path)
    total = len(passwords)

    with zipfile.ZipFile(file_path) as zf:
        for i, password in enumerate(passwords):
            try:
                print_progress(i + 1, total)
                zf.extractall(pwd=bytes(password, 'utf-8'))
                logger(f"\n[SUKSES] Password ditemukan: {password}", level="SUCCESS")
                write_result_to_file(f"ZIP: {file_path} => Password: {password}")
                return password
            except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                continue
            except Exception as e:
                logger(f"\n[ERROR] Gagal membuka ZIP: {e}", level="ERROR")
                break

    logger("\n[!] Password tidak ditemukan di wordlist.", level="WARN")
