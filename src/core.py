import time
import sys
import os


def logger(msg, level="INFO"):
    prefix = {
        "INFO": "[*]",
        "SUCCESS": "[+]",
        "ERROR": "[!]",
        "WARN": "[~]"
    }.get(level.upper(), "[*]")
    print(f"{prefix} {msg}")


def load_wordlist(path):
    if not os.path.exists(path):
        logger(f"Wordlist tidak ditemukan: {path}", level="ERROR")
        raise FileNotFoundError("Wordlist tidak ditemukan")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip() != ""]


def print_progress(current, total):
    percent = (current / total) * 100
    bar = ('#' * int(percent // 2)).ljust(50)
    sys.stdout.write(f"\r[Cracking] |{bar}| {percent:.2f}%")
    sys.stdout.flush()


def write_result_to_file(result, output_file="cracked_results.txt"):
    with open(output_file, "a") as f:
        f.write(result + "\n")
