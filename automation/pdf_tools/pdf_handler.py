import os
from pypdf import PdfReader, PdfWriter
from typing import Optional

class PDFHandler:
    """
    Classe utilitária para manipulação de arquivos PDF.
    Suporta leitura de metadados e remoção de senhas.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

    def get_info(self)-> dict:
        """
        Retorna metadados do PDF.
        """
        try:
            render = PdfReader(self.file_path)
            info = render.metadata
            return{
                "paginas": len(render.pages),
                "autor": info.author if info else "Desconhecido",
                "titulo": info.title if info else "Sem título",
                "encriptado": render.is_encrypted
            }
        except Exception as e:
            return {"erro": str(e)}

    def unlock_pdf(self, password: str, output_path: Optional[str] = None):
        """
        Remove a senha de um arquivo PDF.           
        """

        try:
            reader = PdfReader(self.file_path)

            if reader.is_encrypted:
                print(f"O arquivo está protegido. Tentando desbloquear com a senha: '{password}'...")
                if not reader.decrypted(password):
                    print("Senha incorreta!")
                    return False
            else:
                print("O arquivo não está protegido.")

            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            
            if not output_path:
                output_path = self.file_path.replace(".pdf", "_unlocked.pdf")

            with open(output_path,'wb') as f:
                writer.write(f)
            
            print(f"Sucesso! Arquivo salvo em: {output_path}")
            return True
        except Exception as e:
            print(f"Erro ao ler PDF: {e}")
            return False



        
