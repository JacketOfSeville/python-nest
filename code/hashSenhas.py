import hashlib

password = "SenhaMuitoSegura"

hash_object = hashlib.sha256() # Cria um objeto de hash SHA256
hash_object.update(password.encode()) # Adicionar a senha ao objeto de hash
hex_dig = hash_object.hexdigest() # Obter o hash resultante em formato hexadecimal

print("Hash da senha:", hex_dig) # Exibir o hash resultante