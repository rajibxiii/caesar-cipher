#### Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text, shift):
#     shiftedLetters = ""

#     for i in range (0, len(text)):
#           letterIndex = alphabet.index(text[i])
#           shiftedLetterIndex = (letterIndex + shift)
#           if (shiftedLetterIndex > len(alphabet)):
#                shiftedLetterIndex -= len(alphabet)
#           shiftedLetters+=alphabet[shiftedLetterIndex]
    
#     print(shiftedLetters)

# def decrypt (text, shift):
#      shiftedLetters = ""

#      for i in range (0, len(text)):
#           letterIndex = alphabet.index(text[i])
#           shiftedLetterIndex = (letterIndex - shift)
#           if (shiftedLetterIndex < 0):
#                shiftedLetterIndex += len(alphabet)
#           shiftedLetters+=alphabet[shiftedLetterIndex]
#      print (shiftedLetters)

def caesar (text, shiftAmount, cipherDirection):
     if (shiftAmount >= len(alphabet)):
          shiftAmount %= len(alphabet)
     if (cipherDirection == "decode"):
          shiftAmount *= -1

     shiftedLetters = ""
     for i in range (0, len(text)):
          if text[i] not in alphabet:
            shiftedLetters+=text[i]
          else:
            letterIndex = alphabet.index(text[i])
            shiftedLetterIndex = (letterIndex + shiftAmount)

            if (shiftedLetterIndex < 0):
                shiftedLetterIndex += len(alphabet)
            if (shiftedLetterIndex > len(alphabet)):
                shiftedLetterIndex -= len(alphabet)

            shiftedLetters+=alphabet[shiftedLetterIndex]
            
     print (shiftedLetters)


shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if (direction == "encode" or direction == "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text=text, shiftAmount=shift, cipherDirection=direction)
    else:
        print ("Wrong input")

    restart = input("\nDo you want to continue? (y/n): ")

    if (restart) == "n":
        shouldContinue = False
    elif (restart) == "y":
        shouldContinue = True
    else:
        print ("Wrong input")