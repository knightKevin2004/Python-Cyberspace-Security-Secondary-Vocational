import base64
flag="mTyqm7wjODkrNLcWl0eqO8K8gc1BPk1GNLgUpI=="
a="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321/+"
b64l="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
a=flag.translate(str.maketrans(a,b64l))
print(base64.b64decode(a).decode())