import hashlib

def read_file(path):
  file = open(path, 'r')
  text = file.readline()
  file.close()
  return text

def hash_md4(text):
  hash = hashlib.new("md4", 
         text.encode('utf-8')).hexdigest()
  return hash
  
def hash_md5(text):
  hash = hashlib.md5(text.encode('utf-8')).hexdigest()
  return hash
  
def hash_sha1(text):
  hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
  return hash
  
def hash_sha256(text):
  hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
  return hash

def hash_sha512(text):
  hash = hashlib.sha3_512(text.encode('utf-8')).hexdigest()
  return hash

def hash_blake(text):
  hash = hashlib.blake2b(text.encode('utf-8')).hexdigest()
  return hash




  