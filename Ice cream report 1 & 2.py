# Membaca data dari file icecream.txt
with open('icecream.txt', 'r') as file:
    lines = file.readlines()

# Membuat dictionary untuk menyimpan data
ice_cream_data = {}
stores = ['Store 1', 'Store 2', 'Store 3']

for line in lines:
    flavor, *sales = line.strip().split(':')
    ice_cream_data[flavor] = [float(sale) for sale in sales]

# Fungsi untuk mencetak laporan
def print_report():
    print("Ice Cream Sales Report")
    print("-----------------------")
    
    total_by_flavor = {}
    total_by_store = [0, 0, 0]
    
    for flavor, sales in sorted(ice_cream_data.items()):
        print(f"\n{flavor.capitalize()}:")
        flavor_total = 0
        for i, sale in enumerate(sales):
            print(f"  {stores[i]}: ${sale:.2f}")
            flavor_total += sale
            total_by_store[i] += sale
        print(f"  Total: ${flavor_total:.2f}")
        total_by_flavor[flavor] = flavor_total
    
    print("\nSummary:")
    print("--------")
    for flavor, total in total_by_flavor.items():
        print(f"{flavor.capitalize()} total: ${total:.2f}")
    
    print("\nStore Totals:")
    for i, total in enumerate(total_by_store):
        print(f"{stores[i]}: ${total:.2f}")

# Cetak laporan ke konsol
print_report()

# Tulis laporan ke file
with open('ice_cream_report.txt', 'w') as file:
    # Mengalihkan output standar ke file
    import sys
    original_stdout = sys.stdout
    sys.stdout = file
    
    print_report()
    
    # Mengembalikan output standar
    sys.stdout = original_stdout

print("\nLaporan telah ditulis ke file 'ice_cream_report.txt'")