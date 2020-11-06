import json

#kullanıcının ismini girdiği kısım
first_name=str(input("isminizi giriniz : "))
if(first_name==""):
    print("boş değer girdiniz")
    first_name=str(input("isminizi giriniz : "))

#kullanıcının soyismini girdiği kısım    
last_name=str(input("soyisminizi giriniz : "))
if(last_name==""):
    print("boş değer girdiniz")
    last_name=str(input("soyisminizi giriniz : "))

    
    
#kullanıcının cinsiyetini girdiği kısım  
gender=str(input("cinsiyetinizi giriniz : "))
if(gender==""):
    print("boş değer girdiniz")
    gender=str(input("cinsiyetinizi giriniz : "))

#kullanıcının adresini girdiği kısım   
address=str(input("adresinizi giriniz : "))
if(address==""):
    print("boş değer girdiniz")
    address=str(input("adresinizi giriniz : "))

    
#kullanıcının numarasını girdiği kısım   
number=int(input("numaranızı giriniz : "))
if(number==""):
    print("boş değer girdiniz")
    number=str(input("numaranızı giriniz : "))

    
#kullanıcının TC Kimlik numarasını girdiği kısım   
ssn=int(input("TC kimlik numaranızı giriniz : "))
if(ssn==""):
    print("boş değer girdiniz")
    ssn=str(input("TC kimlik numaranızı giriniz : "))

    
    
    
#kullanıcının doğum tarihini girdiği kısım    
dateofbirth=int(input("dogum tarihinizi giriniz : "))
if(dateofbirth==""):
    print("boş değer girdiniz")
    dateofbirth=str(input("dogum tarihinizi giriniz : "))

       
    
#kullanıcının jsona dönecek bilgilerinin bulunduğu  kısım
person=[
    {
    "ad":first_name,
    "soyad":last_name,
    "cinsiyeti":gender,
    "adresi":address,
    "numarasi": number,
    "kimlik_numarasi":ssn,
    "dogum_yili":dateofbirth,
   
   
        
    }
]

#kullanıcının bilgilerini json olarak dönüştürüp 
# #sonrasında da dosyaya yazdığı kısım
file=open("person.json","w",encoding="utf8")
file.writelines(json.dumps(person , ensure_ascii=False))

file.close()
