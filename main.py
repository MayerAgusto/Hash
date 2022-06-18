from hash import *

methods_hash = [
  "MD4", "MD5", "SHA1","SHA256","SHA512", "BLAKE"
]
method_output = ["Ingresar texto  manualmente", 
                 "Ingresar mediante archivo"]

def show_methods():
  for i in range(0,len(methods_hash)):
    print(i," = ", methods_hash[i])
    
def show_output():
  for i in range(0,len(method_output)):
    print(i," = ", method_output[i])

def make_hash(code_method, text):
  hash_text = ""
  if code_method == 0:
    hash_text = hash_md4(text)
  if code_method == 1:
    hash_text = hash_md5(text)
  if code_method == 2:
    hash_text = hash_sha1(text)
  if code_method == 3:
    hash_text = hash_sha256(text)
  if code_method == 4:
    hash_text = hash_sha512(text)
  if code_method == 5:
    hash_text = hash_blake(text)
    
  return hash_text
  
def calculator():
  text = ""
  print("CALCULADORA")
  print("TIPOS DE METODOS HASH")
  show_methods()
  hash_type = input("Ingresa el tipo de metodo: ")
  print("Selecciono: " + methods_hash[int(hash_type)])
  print()
  print("Tipos de entrada")
  show_output()
  output = input("Ingrese el formato de entrada: ")
  print("Selecciono: " + method_output[int(output)])
  print()
  
  if(int(output) == 0):
    typed_text = input("Ingrese el texto: ")
    hash_result = make_hash(int(hash_type),typed_text)
    print("Resultado ="," ",hash_result)
  else:
    file_text = input("Ingrese nombre del archivo: ")
    text = read_file(file_text)
    hash_result = make_hash(int(hash_type),text)
    print("Resultado ="," ",hash_result)

calculator()
