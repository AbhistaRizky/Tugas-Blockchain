import sha3
from base64 import encode
from attr import has

print("Tugas untuk penerapan Keccak 256")
raw_message = input("Masukkan kata-kata yang akan dikirim: ")
print("Pesan Awal: \n", raw_message)
encrypted = raw_message.encode()
obj_encrypted = sha3.keccak_256(encrypted)
print("Pesan yang sudah dienkripsi: \n", obj_encrypted.hexdigest())