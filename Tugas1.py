import random
import sys

# Buat DES Table nya

# Table Permutasi awal
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

# Table Permutasi akhir
FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

# Ekspansi table 32 bit -> 48 bit
E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

# Buat Box S nya
S_BOX = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ],
    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ],
    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ],
    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ],
    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ],
    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ],
    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ],
    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ],
]

# Permutasi setelah S-box
P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

# PC-1 (Permutasi pilihan 1)
PC_1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 (Permutasi pilihan 2)
PC_2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Angka pergeseran setiap ronde
SHIFT_SCHEDULE = [
    1,1,2,2,2,2,2,2,
    1,2,2,2,2,2,2,1
]


# Fungsi pembantu
def string_to_bit_array(text):
    """Mengubah string menjadi daftar bit"""
    array = []
    for char in text:
        binval = bin(ord(char))[2:].rjust(8, '0')
        array.extend([int(x) for x in binval])
    return array

def bit_array_to_string(array):
    """Mengubah daftar bit menjadi string"""
    res = ''.join([str(x) for x in array])
    chars = []
    for i in range(0, len(res), 8):
        byte = res[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def permute(block, table):
    """Mempermutasikan blok dengan tabel yang diberikan"""
    return [block[x-1] for x in table]

def xor(t1, t2):
    """Melakukan operasi XOR pada dua daftar"""
    return [x ^ y for x, y in zip(t1, t2)]

def shift_left(block, n):
    """Menggeser blok ke kiri sebanyak n"""
    return block[n:] + block[:n]

def split(block, n):
    """Membagi blok menjadi dua bagian"""
    return block[:n], block[n:]

def s_box_substitution(block):
    """Menerapkan substitusi S-box"""
    result = []
    for i in range(8):
        chunk = block[i*6:(i+1)*6]
        row = (chunk[0] << 1) + chunk[5]
        col = (chunk[1] << 3) + (chunk[2] << 2) + (chunk[3] << 1) + chunk[4]
        val = S_BOX[i][row][col]
        binval = bin(val)[2:].rjust(4, '0')
        result.extend([int(x) for x in binval])
    return result

def generate_keys(key):
    """Menghasilkan 16 kunci putaran"""
    key = string_to_bit_array(key)
    key = permute(key, PC_1)
    left, right = split(key, 28)
    keys = []
    for shift in SHIFT_SCHEDULE:
        left = shift_left(left, shift)
        right = shift_left(right, shift)
        combined = left + right
        round_key = permute(combined, PC_2)
        keys.append(round_key)
    return keys

def pad(text):
    """Menambahkan padding pada teks agar panjangnya kelipatan 8"""
    pad_len = 8 - (len(text) % 8)
    return text + (chr(pad_len) * pad_len)

def unpad(text):
    """Menghapus padding dari teks"""
    pad_len = ord(text[-1])
    return text[:-pad_len]

def des_encrypt_block(block, keys):
    """Mengenkripsi satu blok dengan DES"""
    block = permute(block, IP)
    left, right = split(block, 32)
    for i in range(16):
        expanded_right = permute(right, E)
        temp = xor(expanded_right, keys[i])
        temp = s_box_substitution(temp)
        temp = permute(temp, P)
        temp = xor(left, temp)
        left, right = right, temp
    combined = right + left
    encrypted = permute(combined, FP)
    return encrypted

def des_decrypt_block(block, keys):
    """Mendekripsi satu blok dengan DES"""
    block = permute(block, IP)
    left, right = split(block, 32)
    for i in range(15, -1, -1):
        expanded_right = permute(right, E)
        temp = xor(expanded_right, keys[i])
        temp = s_box_substitution(temp)
        temp = permute(temp, P)
        temp = xor(left, temp)
        left, right = right, temp
    combined = right + left
    decrypted = permute(combined, FP)
    return decrypted

def des_encrypt(plaintext, key):
    """Mengenkripsi plaintext menggunakan DES"""
    plaintext = pad(plaintext)
    key = key[:8]  # DES menggunakan kunci 8-byte
    keys = generate_keys(key)
    encrypted = []
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        block = string_to_bit_array(block)
        encrypted_block = des_encrypt_block(block, keys)
        encrypted.extend(encrypted_block)
    return ''.join([str(x) for x in encrypted])

def des_decrypt(ciphertext, key):
    """Mendekripsi ciphertext menggunakan DES"""
    key = key[:8]
    keys = generate_keys(key)
    decrypted = []
    for i in range(0, len(ciphertext), 64):
        block = ciphertext[i:i+64]
        block = [int(x) for x in block]
        decrypted_block = des_decrypt_block(block, keys)
        decrypted.extend(decrypted_block)
    decrypted_text = bit_array_to_string(decrypted)
    return unpad(decrypted_text)

def generate_random_key():
    """Menghasilkan kunci acak 8 karakter"""
    return ''.join([chr(random.randint(0, 255)) for _ in range(8)])

def main():
    print("=== Selamat Datang Di User Interfase Enkripsi dan Dekripsi ===")
    key = generate_random_key()
    while True:
        print("\nPilih Opsi:")
        print("1. Enkripsi Kata")
        print("2. Dekripsi Kata")
        print("3. Tampilkan Key Saat ini")
        print("4. Generate Key Baru")
        print("5. Exit")
        choice = input("Pilih (1-5): ")
        if choice == '1':
            plaintext = input("Masukkan String: ")
            ciphertext = des_encrypt(plaintext, key)
            print(f"Teks telah terenkripsi (binary): {ciphertext}")
        elif choice == '2':
            ciphertext = input("Masukkan binary nya: ")
            if len(ciphertext) % 64 != 0:
                print("Invalid Bukan 64 bits.")
                continue
            decrypted = des_decrypt(ciphertext, key)
            print(f"Text Dekripsi: {decrypted}")
        elif choice == '3':
            print(f"Key Saat ini: {''.join(['{:02x}'.format(ord(c)) for c in key])}")
        elif choice == '4':
            key = generate_random_key()
            print("Key baru berhasil dibuat.")
        elif choice == '5':
            print("Selamat Tinggal!")
            sys.exit()
        else:
            print("Pilihan Salah, Silahkan Coba Lagi.")

if __name__ == "__main__":
    main()
