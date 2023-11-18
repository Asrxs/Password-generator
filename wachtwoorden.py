import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&()+="

def generate_password(password_len):
    password = ''.join(random.choice(characters) for _ in range(password_len))
    return password

email = input("Voer uw e-mailadres in: ")
password_len = int(input("Hoe lang wilt u uw wachtwoord: "))

generated_password = generate_password(password_len)

# Schrijf e-mailadres en gegenereerd wachtwoord naar een tekstbestand
with open("ilikemen.txt", "a") as file:
    file.write(f"E-mailadres: {email}\n")
    file.write(f"Wachtwoord: {generated_password}\n")
    file.write("\n")

print("Uw wachtwoord is gegenereerd en opgeslagen in het bestand 'wachtwoorden.txt'.")
