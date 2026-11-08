def main():
    print("=== KALKULATOR DISKON BELANJA ===")
    
    try:
        harga_awal = float(input("Masukkan harga total (Rp) : "))
        diskon = float(input("Masukkan persentase diskon (%) : "))
        
        potongan = harga_awal * (diskon / 100)
        total_bayar = harga_awal - potongan
        
        print("\n--- RINCIAN PEMBAYARAN ---")
        print(f"Harga Awal  : Rp {harga_awal:,.2f}")
        print(f"Potongan    : Rp {potongan:,.2f} ({diskon}%)")
        print(f"Total Bayar : Rp {total_bayar:,.2f}")
        
    except ValueError:
        print("\n[Error] Input harus berupa angka yang valid!")

if __name__ == "__main__":
    main()