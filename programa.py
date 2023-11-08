import jwt
import datetime

now = datetime.datetime.now()
iat = int( now.timestamp() )
tomorrow = now + datetime.timedelta( days= 1 )
expireAt = int( tomorrow.timestamp() )

user = "paulo"
email ="pauloperozocolombia@gmail.com"
secret ="this_is_my_secret"

payload = {
    "user":user,
    "email":email,
    "iat":iat,
    "exp":expireAt
}

token = jwt.encode(payload,secret,algorithm="HS256")

print( token )