print(f"{'PROGRAM KONVERSI TEMPERATUR SUHU':^50}")
print(f"{'='*50 : ^50}")

suhu = int(input("Masukkann Suhu :"))
print("1. Celcius \n2. Reamur \n3. Farhenheit \n4. Kelvin")
pilih = int(input("Pilih Jenis Suhu:"))

print(f"{'='*50 : ^50}")
print(f"{'NILAI SUHU':^50}")
print(f"{'='*50 : ^50}")

if pilih == 1:
    print(f"Suhu Dalam Celcius    : {suhu}")
    reamur = suhu * 4/5
    print(f"Suhu Dalam Reamur     : {reamur}")
    farhenheit = suhu * 9/5 + 32
    print(f"Suhu Dalam Farhenheit : {farhenheit}")
    Kelvin = suhu + 273
    print(f"Suhu Dalam Kelvin     : {Kelvin}")
elif pilih == 2:
    print(f"Suhu Dalam Reamur       : {suhu}")
    celcius = suhu * 5/4
    print(f"Suhu Dalam Celcius      :{celcius}")
    farhenheit  = suhu * 9/4  +32
    print(f"Suhu Dalam Farhenheiuit :{farhenheit}")
    kelvin = suhu * 5/4 +273
    print(f"Suhu Dalam Kelvin       : {kelvin}")
elif pilih == 3:
    print(f"Suhu Dalam Farhenheit : {suhu}")
    celcius = (suhu - 32) *5/9
    print(f"Suhu Dalam Celcius    : {celcius}")
    reamur = (suhu - 32) * 4/9
    print(f"Suhu Dalam Reamur     : {reamur}")
    kelvin = celcius + 273
    print(f"Suhu Dalam Kelvin     : {kelvin}")
elif pilih == 4:
    print(f"Suhu Dalam Kelvin       : {suhu}")
    celcius = suhu  - 273
    print(f"Suhu Dalam Celcius      : {celcius}")
    reamur =  (suhu  - 273) * 4/5
    print(f"Suhu Dalam Reamur       : {reamur}")
    farhenheit = 9/5 * (suhu - 273) +  32
    print(f"Suhu Dalamm Farhenheiit : {farhenheit}")
