import os
import subprocess


class Judas:
    def __init__(self):
        # Declaração das variáveis e constantes da classe
        self.charset = "utf-8"

    def listar_diretorio(self, caminho='.'):
        try:
            arquivos = os.listdir(caminho)
            for arquivo in arquivos:
                print(arquivo)
        except Exception as e:
            print(f"Erro ao listar o diretório: {e}")

    def ler_arquivo(self, caminho):
        try:
            with open(caminho, 'r', encoding=self.charset) as file:
                conteudo = file.read()
                print(conteudo)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def criar_arquivo(self, caminho, conteudo=''):
        try:
            with open(caminho, 'w', encoding=self.charset) as file:
                file.write(conteudo)
                print(f"Arquivo {caminho} criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o arquivo: {e}")

    def editar_arquivo(self, caminho, novo_conteudo):
        try:
            with open(caminho, 'a', encoding=self.charset) as file:  # 'a' de append
                file.write(novo_conteudo)
                print(f"Arquivo {caminho} editado com sucesso.")
        except Exception as e:
            print(f"Erro ao editar o arquivo: {e}")

    def executar_comando(self, comando):
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print(resultado.stdout)
        except Exception as e:
            print(f"Erro ao executar o comando: {e}")


if __name__ == "__main__":
    judas = Judas()
    judas.listar_diretorio()
    # Exemplo de leitura de diretorio: judas.listar_diretorio()
    # Exemplo de leitura de arquivo: judas.ler_arquivo('exemplo.txt')
    # Exemplo de criação de arquivo: judas.criar_arquivo('novo_arquivo.txt', 'Conteúdo inicial')
    # Exemplo de edição de arquivo: judas.editar_arquivo('novo_arquivo.txt', '\nMais conteúdo')
    # Exemplo de execução de comando: judas.executar_comando('ls')
