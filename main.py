MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
seleccion = int(input("Hola, bienvenido al convertidor codigo morse \n Por favor selecciona 1 para encriptar o 2 para desencriptar"))
if(seleccion == 1):
  def encrypt(message):
      cipher = ''
      for letter in message:
          if letter != ' ':
              cipher += MORSE_CODE_DICT[letter] + ' '
          else:
              cipher += ' '
      return cipher
  letras = input("ingrese la frase que quieres traducir 📚 : ").upper()
  message = letras
  result = encrypt(message)
  print(result)
elif(seleccion == 2):
  def decrypt(message):
      message += ' '
      decipher = ''
      citext = ''
      for letter in message:
          if letter != ' ':
              i = 0
              citext += letter
          else:
              i += 1
              if i == 2:
                  decipher += ' '
              else:
                  decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                  citext = ''
      return decipher
  
  codigo = input("Coloca la frase: ")
  message = codigo
  result = decrypt(message)
  print(result)
else:
  print("seleccion incorrecta ❌")
  