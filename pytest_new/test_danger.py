# coding: utf-8
from itsdangerous import URLSafeSerializer
auth_s = URLSafeSerializer("secret key", "auth")
token = auth_s.dumps({"id": 5, "name": "itsdangerous"})
print token

data = auth_s.loads(token)
print data["name"]