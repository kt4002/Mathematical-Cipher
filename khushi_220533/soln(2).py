#assignment 1_ques.2(b)___decrypting a cipher

def Decrypt(c):
  """Decrypts a message using a Caesar cipher and tries all possible keys.
  Inputs:
      c: The encrypted message (string).
  Returns:
      A list of possible decrypted messages, one for each key.
  """
  possible_messages = []
  for key in range(26):
    message = ""
    for char in c:
      if char.isalpha():
        shifted = ord(char) - key
        if char.isupper():
          message += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
          message += chr((shifted - ord('a')) % 26 + ord('a'))
      else:
        message += char
    possible_messages.append(message)
  return possible_messages

# Get encrypted message input
encrypted_message = input("Enter the encrypted message: ")

# Decrypt with all possible keys
decrypted_messages = Decrypt(encrypted_message)

# Print all possible decrypted messages
print("\nPossible Decrypted Messages:")
for message in decrypted_messages:
  print(message)
