import os
import pyaes

def decrypt_file(file_name, key):
    """
    Função para descriptografar um arquivo.
    :param file_name: Nome do arquivo criptografado.
    :param key: Chave de descriptografia (16 bytes).
    """
    if not os.path.exists(file_name):
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
        return

    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Inicializar o AES para descriptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado com sucesso: {new_file_name}")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

# Configuração de execução
if __name__ == "__main__":
    file_name = "teste.txt.ransomwaretroll"  # Nome do arquivo criptografado
    key = b"testeransomwares"  # Chave de descriptografia (16 bytes)
    decrypt_file(file_name, key)
