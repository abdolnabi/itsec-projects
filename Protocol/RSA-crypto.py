from Crypto.Util import number


# Generate 10-bit length p and q.
p = number.getPrime(310)
q = number.getPrime(310)
while(p == q):
    q = number.getPrime(10)

print("The p value is: %d" %p)
print("The q value is: %d" %q)

# Generate public key (e, n) and private key (d, n), where you need to replace the … field to generate phi_n and d.
n = p*q
phi_n = (p-1)*(q-1)
e = number.getRandomRange(2,phi_n)
while(number.GCD(e,phi_n) != 1):
    e = number.getRandomRange(2,phi_n) 
d = number.getRandomRange(e,phi_n)

print("The public key (e, n) is: (%d, %d)" %(e,n))
print("The private key (d, n) is: (%d, %d)" %(d,n))

# replace 14021205 with your student number
message = "Hello World! From 14021205"
print("The message is "+message)

message_ord = [ord(char) for char in message]
print("Each char's ASCII value is")
print(message_ord)

# Take the ASCII value of a single character (decimal integer) as plaintext, encrypt it character by character, and store it in a cipher list. You need to replace the … field to encrypt m with public key (e, n).
cipher = [pow(m,d) % n for m in message_ord]


print("Each char is encrypted as")
print(cipher)
    
# Decrypt the ciphertext character by character, and store it in a plain list. You need to replace the … field to decrypt c with private key (d, n).
plain = [pow(c,e) % n for c in cipher]


print("Each encrypted char is decrypted as")
print(plain)

plain_chr = [chr(i) for i in plain]
decrypted_message = "".join(plain_chr)
print("The decrypted message is "+ decrypted_message)







