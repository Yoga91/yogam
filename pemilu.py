voters_KTP = {
    "v_1" : ["Tony", 3471019911212],
    "v_2" : ["Anto", 3471019921415],
    "v_3" : ["Boby", 3471019931617],
    "v_4" : ["Hendra", 3471019941718],
    "v_5" : ["Budi", 3471019951819]
    }

paslon = ['ANIES BASWEDAN', 'PRABOWO SUBIANTO', 'GANJAR PRANOWO']

def pemilu(paslon):
    print("\n======= CALON PRESIDEN =======")
    for index, item in enumerate(paslon, start=1):
        print(f'\n{index}. {item}')

print("\n===== SELAMAT DATANG DI APLIKASI PEMILU 2024 =====")
def pilih(voters_KTP):
    for k in voters_KTP:
        print("\nNama :", voters_KTP[k][0], "\t", "NIK :", voters_KTP[k][1], "\t",
              "KEY :", k)

pilih(voters_KTP)   

pilihan = (input('\nMasukkan KEY anda : '))
pemilih = pilihan
print("\nKey anda :", pemilih)

if pilihan in ['v_1', 'v_2', 'v_3', 'v_4', 'v_5']:
    print("\nAKSES ANDA DITERIMA")

else:
    print("\nAKSES ANDA DITOLAK")

pemilu(paslon)
pilihanmu = (input("\nSilahkan Isi Pilhan Anda (1/2/3) :"))
    
if pilihanmu == "1":
    print("\nSELAMAT !\n", "\nANDA TELAH MEMILIH ANIES BASWEDAN\n")
    print("TERIMA KASIH ATAS PARTISIPASINYA DALAM PEMILU 2024")

elif pilihanmu == "2":
    print("\nSELAMAT !\n", "\nANDA TELAH MEMILIH PRABOWO SUBIANTO\n")
    print("TERIMA KASIH ATAS PARTISIPASINYA DALAM PEMILU 2024")

elif pilihanmu == "3":
    print("\nSELAMAT !\n", "\nANDA TELAH MEMILIH GANJAR PRANOWO\n")
    print("TERIMA KASIH ATAS PARTISIPASINYA DALAM PEMILU 2024")