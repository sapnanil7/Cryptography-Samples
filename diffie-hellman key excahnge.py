prime =input("Enter a prime number: ")
generator =input("Enter a generator: ")
private_key_a =input("Enter private key for a: ")
private_key_b =input("Enter private key for b: ")

def publickeygenrator(prime, generator, private_key):
    public_key = (int(generator)**int(private_key))%int(prime)
    return public_key
choice = input("Enter 1 for private key a and 2 for private key b: ")

if (int(choice)==1):
    print (publickeygenrator(prime, generator, private_key_a))
elif (int(choice)==2):
    print (publickeygenrator(prime, generator, private_key_b))
else:
    print("Invalid choice")

def secretkeygenerator(prime, public_key, private_key):
    secret_key = (int(public_key)**int(private_key))%int(prime)
    return secret_key

choice = input("Enter 1 for private key a and 2 for private key b: ")
if (int(choice)==1):
    public_key_b = publickeygenrator(prime, generator, private_key_b)
    print (secretkeygenerator(prime, public_key_b, private_key_a))
elif (int(choice)==2):
    public_key_a = publickeygenrator(prime, generator, private_key_a)
    print (secretkeygenerator(prime, public_key_a, private_key_b))
else:
    print("Invalid choice")

