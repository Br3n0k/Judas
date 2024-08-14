import os
import shutil
import subprocess
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv


# Class ChangeHandler - Classe para manipulação de eventos em arquivos e diretórios
class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Arquivo alterado: {event.src_path}")

    def on_created(self, event):
        print(f"Arquivo criado: {event.src_path}")

    def on_deleted(self, event):
        print(f"Arquivo deletado: {event.src_path}")


# Classe Judas - Classe principal do projeto
class Judas:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Configura as variáveis de ambiente
        self.charset = "utf-8"
        self.api_key_openweathermap = os.getenv("API_KEY_OPENWEATHERMAP")

    def listar_diretorio(self, caminho='.'):
        try:
            arquivos = os.listdir(caminho)
            for arquivo in arquivos:
                print(arquivo)
        except Exception as e:
            print(f"Erro ao listar o diretório: {e}")

    def criar_diretorio(self, caminho):
        try:
            os.makedirs(caminho, exist_ok=True)
            print(f"Diretório {caminho} criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o diretório: {e}")

    def remover_diretorio(self, caminho):
        try:
            os.rmdir(caminho)
            print(f"Diretório {caminho} removido com sucesso.")
        except Exception as e:
            print(f"Erro ao remover o diretório: {e}")

    def monitorar_diretorio(self, caminho='.'):
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, path=caminho, recursive=True)
        observer.start()
        print(f"Monitorando alterações em: {caminho}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def mover_arquivo(self, caminho_origem, caminho_destino):
        try:
            os.rename(caminho_origem, caminho_destino)
            print(f"Arquivo movido de {caminho_origem} para {caminho_destino}.")
        except Exception as e:
            print(f"Erro ao mover o arquivo: {e}")

    def copiar_arquivo(self, caminho_origem, caminho_destino):
        try:
            shutil.copy(caminho_origem, caminho_destino)
            print(f"Arquivo copiado de {caminho_origem} para {caminho_destino}.")
        except Exception as e:
            print(f"Erro ao copiar o arquivo: {e}")

    def renomear_arquivo(self, caminho_origem, novo_nome):
        try:
            os.rename(caminho_origem, novo_nome)
            print(f"Arquivo {caminho_origem} renomeado para {novo_nome}.")
        except Exception as e:
            print(f"Erro ao renomear o arquivo: {e}")

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
            with open(caminho, 'a', encoding=self.charset) as file:
                file.write(novo_conteudo)
                print(f"Arquivo {caminho} editado com sucesso.")
        except Exception as e:
            print(f"Erro ao editar o arquivo: {e}")

    def remover_arquivo(self, caminho):
        try:
            os.remove(caminho)
            print(f"Arquivo {caminho} removido com sucesso.")
        except Exception as e:
            print(f"Erro ao remover o arquivo: {e}")

    def executar_comando(self, comando):
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print(resultado.stdout)
        except Exception as e:
            print(f"Erro ao executar o comando: {e}")

    def obter_clima(self, cidade):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.api_key_openweathermap}&units=metric&lang=pt"
        try:
            resposta = requests.get(url)
            dados = resposta.json()
            if dados.get('cod') == 200:
                temperatura = dados['main']['temp']
                descricao = dados['weather'][0]['description']
                print(f"Clima em {cidade}: {descricao.capitalize()}, {temperatura}°C")
            else:
                print(f"Erro ao obter dados do clima: {dados.get('message')}")
        except Exception as e:
            print(f"Erro ao acessar a API: {e}")


if __name__ == "__main__":
    # Instanciação da classe
    judas = Judas()

    # Exemplo de uso
    # Listar arquivos do diretório atual do projeto como teste
    # judas.listar_diretorio()

    # Exemplo de manipulação de diretórios
    # judas.criar_diretorio('novo_diretorio')
    # judas.remover_diretorio('novo_diretorio')

    # Exemplo de manipulação de arquivos
    # judas.ler_arquivo('arquivo.txt')
    # judas.criar_arquivo('novo_arquivo.txt', 'Conteúdo inicial')
    # judas.editar_arquivo('novo_arquivo.txt', '\nMais conteúdo')
    # judas.remover_arquivo('novo_arquivo.txt')
    # judas.mover_arquivo('arquivo.txt', 'novo_diretorio/arquivo.txt')
    # judas.copiar_arquivo('arquivo.txt', 'novo_diretorio/arquivo_copiado.txt')
    # judas.renomear_arquivo('novo_diretorio/arquivo_copiado.txt', 'novo_diretorio/arquivo_renomeado.txt')

    # Exemplo de execução de comando
    # judas.executar_comando('ls')

    # Exemplo de uso
    # Teste a função de obter clima
    #judas.obter_clima('Goiânia')

    # Exemplo de monitoramento de diretório
    judas.monitorar_diretorio()