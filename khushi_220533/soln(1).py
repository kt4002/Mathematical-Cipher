""" Assignment 1_Question_2(a) """

def Enc(m, k):
  """Encrypts a message using a shift or Caesar cipher.
 inputs:
      m: The message to encrypt (string).
      k: The shift key (integer).
  Returns:
      The encrypted message (string).
  """
  cipher = ''
  for char in m:
    if char.isalpha():
      shifted = ord(char) + k
      if char.isupper():
        cipher += chr((shifted - ord('A')) % 26 + ord('A'))
      else:
        cipher += chr((shifted - ord('a')) % 26 + ord('a'))
    else:
      cipher += char
  return cipher

def get_message_and_encrypt(): #  takes user input for message and key, for encrypting the message and returns the encrypted message

  message = input("Enter message to encrypt: ")
  while True: 
    try:
      key = int(input("Enter key (integer between 0 and 25): "))
      if 0 <= key <= 25:
        break  
      else:
        print("Invalid key. Please enter a number between 0 and 25.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  encrypted_message = Enc(message, key)
  return encrypted_message

# user input
encrypted_message = get_message_and_encrypt()
print("Encrypted message:", encrypted_message)
