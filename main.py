import random

ai_choice = ["taş", "kağıt", "makas"]
user_choice = ["taş", "kağıt", "makas"]

user = input("TAŞ / KAĞIT / MAKAS: ").lower()

if not user:
    print("Sistem: Lütfen bir seçenek giriniz.")
elif (user in user_choice):
    ai = random.choice(ai_choice)
    
    if (ai == "taş" and user == "makas"):
        print("Sistem: AI Kazandı!")
    elif (ai == "taş" and user == "kağıt"):
        print("Sistem: İnsan Kazandı!")
    elif (ai == "taş" and user == "taş"):
        print("Sistem: Berabere!")
    elif (ai == "makas" and user == "taş"):
        print("Sistem: İnsan Kazandı!")
    elif (ai == "makas" and user == "kağıt"):
        print("Sistem: AI Kazandı!")
    elif (ai == "makas" and user == "makas"):
        print("Sistem: Berabere!")
    elif (ai == "kağıt" and user == "taş"):
        print("Sistem: AI Kazandı!")
    elif (ai == "kağıt" and user == "makas"):
        print("Sistem: İnsan Kazandı!")
    elif (ai == "kağıt" and user == "kağıt"):
        print("Sistem: Berabere!")
    else:
        print("HATA!")
else:
    print("Sistem: Lütfen sadece TAŞ / KAĞIT / MAKAS seçeneklerinden bir tanesini kullanın!")
