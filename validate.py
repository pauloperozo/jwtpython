import jwt

token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicGF1bG8iLCJlbWFpbCI6InBhdWxvcGVyb3pvY29sb21iaWFAZ21haWwuY29tIiwiaWF0IjoxNjk5NDIxMTI3LCJleHAiOjE2OTk1MDc1Mjd9.iDdw8TnSZddN5Fq_LQS9zkrQtbUbHYBjEQatUNEt-mU"
secret ="this_is_my_secret"

try:
    payload = jwt.decode( token ,secret , algorithms=["HS256"])
except jwt.exceptions.ExpiredSignatureError:
    print("Token Expirado")
except jwt.exceptions.InvalidSignatureError:
    print("Firma No Valida")
except jwt.exceptions.DecodeError:
    print("Token No Valido")
else:
    print("Token Valido")