import random

ai_choice = ["taş", "kağıt", "makas"]
user_choice = ["taş", "kağıt", "makas"]

user = input("TAŞ / KAĞIT / MAKAS: ").lower()

if not user:
    print("Sistem: Lütfen bir seçenek giriniz.")
elif user in user_choice:
    ai = random.choice(ai_choice)
    
    if ai == "taş" and user == "makas":
        print(f"Sistem: AI Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "taş" and user == "kağıt":
        print(f"Sistem: İnsan Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "taş" and user == "taş":
        print(f"Sistem: Berabere! (AI: {ai} - İnsan: {user})")
    elif ai == "makas" and user == "taş":
        print(f"Sistem: İnsan Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "makas" and user == "kağıt":
        print(f"Sistem: AI Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "makas" and user == "makas":
        print(f"Sistem: Berabere! (AI: {ai} - İnsan: {user})")
    elif ai == "kağıt" and user == "taş":
        print(f"Sistem: AI Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "kağıt" and user == "makas":
        print(f"Sistem: İnsan Kazandı! (AI: {ai} - İnsan: {user})")
    elif ai == "kağıt" and user == "kağıt":
        print(f"Sistem: Berabere! (AI: {ai} - İnsan: {user})")
else:
    print("Sistem: Lütfen sadece TAŞ / KAĞIT / MAKAS seçeneklerinden bir tanesini kullanın!")
