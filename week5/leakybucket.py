bucket_size = int(input("Enter bucket capacity: "))
out_rate = int(input("Enter outgoing rate: "))
n = int(input("Enter number of time cycles: "))

packets = []

print("Enter incoming packets:")
for i in range(n):
    p = int(input())
    packets.append(p)

remaining = 0

print("\n" + "-" * 70)
print("{:<15} {:<15} {:<15} {:<10} {:<10}".format(
    "Clock", "Packet Size", "Accept", "Sent", "Remaining"
))
print("-" * 70)

for i in range(n):

    incoming = packets[i]

    # Check bucket capacity
    if remaining + incoming <= bucket_size:
        accept = incoming
        remaining += incoming
    else:
        accept = "Dropped"
        incoming = 0

    # Send packets at constant rate
    sent = min(remaining, out_rate)
    remaining -= sent

    print("{:<15} {:<15} {:<15} {:<10} {:<10}".format(
        i + 1, packets[i], accept, sent, remaining
    ))

print("-" * 70)
print("\nPackets remaining in bucket:", remaining)
