def mod():
  number = input("Input a prime number ")
  c = checknum(number)
  if not c:
    print("Enter a prime number")
    return mod()
  number = int(number)
  if number > 2:
    for i in range(2, number):
        if (number % i) == 0:
          print("Not a prime number, try again")
          return mod()
    else:
      print("That is a prime number")
      return number
  else:
    print("Please enter a higher number")
    return mod()

def root():
  proot = input("Please enter a prime number that is less than the first ")
  c = checknum(proot)
  if not c:
    print("Input a number")
    return root()
  proot = int(proot)
  if number > proot:
    first = (proot ** 1) % number
    last = (proot ** number) % number
    if first == last:
      print("That is a primitive root")
      return proot
    else:
      print("That is not a primitive root, try again")
      return root()
  else:
    print("This number must be less than the first number, try again")
    return root()

def checknum(x):
  if (x.isnumeric()):
    return True
  else:
    return False

def integer(y):
  if (checknum(y)):
    return y
  else:
    i = input("Enter an integer: ")
    return integer(i)


print("Welcome to the python Diffie-Hellman key exchange walkthough.\n")
input("(Press enter to continue)\n")
print("This program will walk through the Diffie-Hellman key exchange with you, while doing all the hard calculations along the way!\n")
input("(Press enter to continue)\n")
print("Now for some history, in 1976 this scheme was published by Whitfield Diffie and Martin Hellman. It was one of the earliest publiches works on the idea of private key with a corresponding public key.\n")
print("Diffie-Hellman key exchange provided the basis for future protocols like TLS/SSL and was shortly followed by a similear scheme called RSA.\n")
input("(Press enter to continue)\n")
print("We will start our story out with Alice and Bob, two people who wish to communicate privatly but who do not have an agreed upon private key before the conversation.\n")
input("(Press enter to continue)\n")
print("First Alice and Bob need to agree on a prime number to use as a modulus.\n")
print("Let's have you select that now\n")
number = int(mod())
print("You have chosen the number %s" % number)
print("Now we need to choose a primitive root modulo %s\n" % number)
print("Any prime number less than the modulo should work\n")
root = int(root())
print("You have choosen %s" % root)
print("So now we have a modulus, %s, and a base, %s" % (number, root))
print("Now Alice must choose a secret integer, it can be any number.\n")
alice = input("Choose a secert integer for Alice ")
alice = int(integer(alice))
print("Now Bob must choose a secret integer.\n")
bob = input("Choose an integer for Bob, it can be any number ")
bob = int(integer(bob))
print("So now Alice has a secret integer %s and Bob has a secret integer %s\n" % (alice, bob))
print("But how will they come up with a shared secret key? They didn't know what the other would choose.\n")
input("(Press enter to continue)\n")
print("This is where the math comes in.\n")
print("Alice takes her secret number, %s, and uses the base %s, like this %s ^ %s" % (alice,root,root,alice))
print("Then Alice uses the modulus %s ^ %s mod %s"% (root,alice,number))
a = (root ** alice) % number
print("And we get %s, this is what we will send to Bob.\n" % a)
input("(Press enter to continue)\n")
print("Bob does the same, %s ^ %s mod %s\n" % (root,bob,number))
b = (root ** bob) % number
print("And gets %s, we send this to Alice.\n" % b)
input("(Press enter to continue)\n")
print("Now we need to calculate the shared secret key.\n")
input("(Press enter to continue)\n")
print("Alice will take the key that Bob sent her, %s, and use it like this %s ^ %s mod %s\n" % (b,b,alice,number))
aa = (b ** alice) % number
print("Alice gets %s, this is the shared secret key, but let's see if Bob gets the same one.\n" % aa)
input("(Press enter to continue)\n") 
print("Bob does this, %s ^ %s mod %s\n" % (a,bob,number))
bb = (a ** bob) % number
print("He gets %s, which should be the same as Alice\n" % bb)
print("Now you can see that without sharing their secret keys, Alice and Bob were able to develop a shared secret key.")
input("(Press enter to end the program)\n")
#source: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
