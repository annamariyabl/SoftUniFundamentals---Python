import re
n = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
for i in range(n):
    barcode = input()
    match = re.findall(pattern,barcode)
    if match:
        product_code = ''
        for j in match[0]:
            if j.isdigit():
                product_code += j
        if product_code == '':
            print(f"Product group: 00")
        else:
            print(f"Product group: {product_code}")
    else:
        print("Invalid barcode")