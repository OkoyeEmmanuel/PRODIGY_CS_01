# the user has options to encrypt or decrypt a message or exit the program
validnumber = False

while validnumber == False:
   print('============================')
   print('Welcome to the Caesar Cipher Program')
   print('============================')
   print('Options:')
   print('1. Encrypt')
   print('2. Decrypt')     
   print('3. Exit')
   print('============================') #just so the options are clear
   option= input('Choose an Option(1,2,3): ')  
   if option == '1':
      plaintext = input('Enter the message to encrypt: ')
      encryptkey = input('Enter the encryption shift key: ')
      encrypted = ''
      for x in plaintext:
         if x.isalpha():
          encrypted = encrypted + chr(ord(x) +int(encryptkey))
         else:
          encrypted = encrypted + x
      print('Encrypted Message: ' + encrypted)
   elif option == '2':
      encryptedmessage = input('Enter the message to decrypt: ')
      decrypted = ''
      decryptkey = input('Enter the decryption shift key: ')
      for x in encryptedmessage:
         if x.isalpha():
            decrypted = decrypted + chr(ord(x) - int(decryptkey))
         else:
            decrypted = decrypted + x
      print('Decrypted Message: ' + decrypted)
   elif option == '3':
      validnumber = True


print('Have a great day, Bye!')
exit()