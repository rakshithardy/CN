def crc(data, generator):
    data = list(map(int, data))
    generator = list(map(int, generator))

    for i in range(len(data) - len(generator) + 1):
        if data[i] == 1:
            for j in range(len(generator)):
                data[i + j] ^= generator[j]

    return ''.join(map(str, data[-(len(generator)-1):]))


# TRANSMITTER
msg = input("Enter message: ")
gen = input("Enter generator polynomial: ")

# Append zeros
data = msg + '0' * (len(gen) - 1)

# Calculate remainder
remainder = crc(data, gen)

# Transmitted data
transmitted = msg + remainder

print("\n--- TRANSMITTER ---")
print("Message:", msg)
print("Generator:", gen)
print("CRC Remainder:", remainder)
print("Transmitted Data:", transmitted)


# RECEIVER
received = input("\nEnter received data: ")

check = crc(received, gen)

print("\n--- RECEIVER ---")
print("Remainder:", check)

if int(check, 2) == 0:
    print("No Error Detected")
else:
    print("Error Detected")