# the user has options to encrypt or decrypt a message or exit the program
print('Welcome to the Caesar Cipher Program')


validnumber = False

while validnumber == False:

   print('1. Encrypt')
   print('2. Decrypt')     
   print('3. Exit')
   option= input('Choose an Option(1,2,3): ')  
   if option == '1':
      plaintext = input('Enter the message to encrypt: ')
      encrypted = ''
      for x in plaintext:
         if x.isalpha():
          encrypted = encrypted + chr(ord(x) +1)
         else:
          encrypted = encrypted + x
      print('Encrypted Message: ' + encrypted)
   elif option == '2':
      encryptedmessage = input('Enter the message to decrypt: ')
      decrypted = ''
      for x in encryptedmessage:
         if x.isalpha():
            decrypted = decrypted + chr(ord(x) -1)
         else:
            decrypted = decrypted + x
      print('Decrypted Message: ' + decrypted)
   elif option == '3':
      validnumber = True


print('Bye!')
exit()