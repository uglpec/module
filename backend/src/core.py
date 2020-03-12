from flask import Flask, jsonify
import login
import scanner
import hashlib, os, sys

app = Flask(__name__)
appKey = "17cb166f71686aca8456fdd837187452"

if __name__ == '__main__':
    secret = os.getenv('secretKey')
    usrKey = hashlib.md5(secret.encode('utf-8')).hexdigest()
    if usrKey != appKey:
      sys.exit("error key!")
    else:
      print("\n Welcome To UGLPeC backend systems ... \n apps started in few minutes ... \n")
      app.run(debug=True, host='0.0.0.0')
