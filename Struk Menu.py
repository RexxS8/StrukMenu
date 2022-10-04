#Andri Martin - 064002200010
#program pembuatan menu kedai coffee
print("kedai coffee")
print("====================")
print ("MENU KEDAI COFFEE")
print("DAFTAR MAKANAN")
print('\t\t\t1.nasi ikan bakar : Rp 35.000,-')
print('\t\t\t2.nasi goreng : Rp 20.000,-')
print('\t\t\t3.ikan goreng : Rp 30.000,-')
print('\t\t\t4.ayam bakar : Rp 30.000,-')
print('\t\t\t5.ayam goreng : Rp 20.000,-')
print("====================")
print("DAFTAR MINUMAN")
print('\t\t\t1.es kopi susu Rp 7.000,-')
print('\t\t\t2.es kopi hitam Rp 5.000,-')
print('\t\t\t3.ice coffe puter Rp 10.000,-')
print('\t\t\t4.lemon tea Rp 7.000,-')
print('\t\t\t5.ice tea Rp 5.000,-')

#user = int(input("Pilih menu  : "))
nama = input("Masukan Nama Anda: ")
makanan = int(input("\nPilih menu Makanan: "))
minuman = int(input("Pilih menu Minuman: "))

sub_harga = 0
print("\n------------------------------------\n")
print("Rincian pesanan" , nama , ":")

if makanan == 1 :
    print("- nasi ikan bakar")
    sub_harga = sub_harga + 35000
    #print("total harga : ", sub_harga )
    
elif makanan == 2 :
    print("- nasi goreng")
    sub_harga = sub_harga + 20000
    #print("total harga : ", sub_harga)
    
elif makanan == 3 :
    print("- ikan goreng")
    sub_harga = sub_harga + 30000
    #print("total harga : ", sub_harga)
    
elif makanan == 4 : 
    print("- ayam bakar")
    sub_harga = sub_harga +30000
    #print("total harga : ", sub_harga)

elif makanan == 5 :
    print("- ayam goreng")
    sub_harga = sub_harga + 20000
    #print ("total harga : ", sub_harga)
        
else :
    print("pilihan anda tidak ada dalam menu")



if minuman == 1 :
    print("- es kopi susu")
    sub_harga = sub_harga + 7000
    print("total harga : ", sub_harga )
    
elif minuman == 2 :
    print("- es kopi hitam")
    sub_harga = sub_harga + 5000
    print("total harga : ", sub_harga)
    
elif minuman == 3 :
    print("- ice coffee puter")
    sub_harga = sub_harga + 10000
    print("total harga : ", sub_harga)
    
elif minuman == 4 : 
    print("- lemon tea")
    sub_harga = sub_harga +7000
    print("total harga : ", sub_harga)

elif minuman == 5 :
    print("- ice tea")
    sub_harga = sub_harga + 5000
    print ("total harga : ", sub_harga)
        
else :
    print("pilihan anda tidak ada dalam menu")