# main.py
import argparse
from src.pdf_cracker import crack_pdf
from src.zip_cracker import crack_zip
from src.office_cracker import crack_office
from src.core import logger


def main():
    parser = argparse.ArgumentParser(
        description="🔐 PDF/ZIP/Office Cracker | by redteam & CTF player",
        usage="python main.py --type [pdf|zip|office] --file FILE --wordlist WORDLIST"
    )

    parser.add_argument('--type', required=True, choices=['pdf', 'zip', 'office'], help='Tipe file target')
    parser.add_argument('--file', required=True, help='Path ke file target')
    parser.add_argument('--wordlist', required=True, help='Path ke wordlist')

    args = parser.parse_args()

    try:
        if args.type == 'pdf':
            crack_pdf(args.file, args.wordlist)
        elif args.type == 'zip':
            crack_zip(args.file, args.wordlist)
        elif args.type == 'office':
            crack_office(args.file, args.wordlist)
        else:
            logger("[!] Tipe tidak dikenali", level="ERROR")
    except KeyboardInterrupt:
        logger("[!] Dibatalkan oleh user.", level="ERROR")
    except Exception as e:
        logger(f"[!] Terjadi error: {str(e)}", level="ERROR")


if __name__ == '__main__':
    main()
