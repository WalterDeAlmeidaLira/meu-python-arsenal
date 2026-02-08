# main.py
import argparse
import sys
from automation.pdf_tools.pdf_handler import PDFHandler

def main():
    parser = argparse.ArgumentParser(
        description="Python Arsenal - Ferramentas de Automação e Estudos"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    pdf_info_parser = subparsers.add_parser("pdf-info", help="Exibe informações de um PDF")
    pdf_info_parser.add_argument("file", type=str, help="Caminho do arquivo PDF")

    pdf_unlock_parser = subparsers.add_parser("pdf-unlock", help="Remove a senha de um PDF")
    pdf_unlock_parser.add_argument("file", type=str, help="Caminho do arquivo PDF protegido")
    pdf_unlock_parser.add_argument("--password", "-p", required=True, type=str, help="Senha do arquivo")
    pdf_unlock_parser.add_argument("--output", "-o", type=str, help="Caminho de saída (opcional)", default=None)

    args = parser.parse_args()

    if args.command == "pdf-info":
        try:
            handler = PDFHandler(args.file)
            info = handler.get_info()
            print("\nInformações do PDF:")
            for k, v in info.items():
                print(f"  - {k.capitalize()}: {v}")
        except Exception as e:
            print(f"Erro: {e}")

    elif args.command == "pdf-unlock":
        try:
            handler = PDFHandler(args.file)
            handler.unlock_pdf(password=args.password, output_path=args.output)
        except Exception as e:
            print(f"Erro Crítico: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()