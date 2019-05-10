from sympy import *
import numpy as np
import random

A = Matrix([
    [1,2,0,4],
    [0,1,1,2],
    [2,3,4,2],
    [1,34,5,6]
    ])

x = Matrix([
    [8,12],
    [5,15],
    [12,0]
    ])

def passwdToMatrix(passwd):
    passwd = [ord(char) for char in passwd]
    while len(passwd)%np.sqrt(len(passwd)) != 0.0:
        passwd.append(-1)
    n = int(np.sqrt(len(passwd)))
    passwd = np.array(passwd).reshape(n,n)
    return passwd


def toMatrix(A, msg, debug=False):
    dim = np.array(A).shape
    if debug: print('Shape: ',dim, 'Length of Msg: ',len(msg))
    chunks = []
    while len(msg)%dim[0] != 0:
        msg +='*'
    i_last = 0
    for i in range(len(msg)//dim[1],len(msg)+1,len(msg)//dim[1]):
        chunks.append(msg[i_last:i])
        i_last = i
    if debug: print('Chunks: ',chunks)
    T = []
    for i in chunks:
        T.append(list(i))
    if debug: print('String Space: ',T)
    T = np.array(T)
    X = np.zeros(T.shape,dtype=int)
    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            X[i][j] = ord(T[i][j])
    return Matrix(X)

def toText(X):
    X = np.array(X)
    text = ''
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            text += chr(X[i][j])
    return text

def MsgtoText(X):
    X = np.array(X)
    text = ''
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            text += str(X[i][j])+','
    return text

    
def encrypt(passwd, msg):
    return passwd*msg

def decrypt(passwd, cipher):
    return passwd.inv()*cipher

def test(debug=False):
    msg = ''.join([chr(random.randint(1,255)) for i in range(100)])
    X = toMatrix(A, msg)
    if debug: print('Encoded : ',X)
    e = encrypt(A,X)
    if debug: print('Encrypted: ',e)
    d = decrypt(A,e)
    if debug: print('Decrypted : ', d )
    if debug: print('Decoded : ', toText(d))
    if d==X:
        return True

def cli():
   print('Matrix Substitution Encryption')
   choice = input('Encrypt/Decrypt (E/D) <<< ')
   if choice.lower() in ['e', 'encrypt']:
       msg = input('Message <<< ')
       passwd = input('Password <<< ')
       
       passwd = passwdToMatrix(passwd)
       msg = toMatrix(passwd,msg)
       e = encrypt(passwd,msg)
       print(MsgtoText(e))
   elif choice.lower() in ['d', 'decrypt']: 
       cipher = input('Cipher <<< ')
       password = input('Password')
       

if __name__ == '__main__':
    cli()
