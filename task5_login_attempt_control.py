import time

correct_password = "python123"
max_attempts = 3
lock_seconds = 10

attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful. Welcome!")
        break

    attempts += 1
    remaining = max_attempts - attempts
    print("Incorrect password.")

    if remaining > 0:
        print("Attempts remaining:", remaining)

if attempts == max_attempts:
    print(f"Too many failed attempts. Access locked for {lock_seconds} seconds.")
    time.sleep(lock_seconds)
    print("Lock period ended. You can try again.")
