#возвращает документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку

bind = "0.0.0.0:8080"
workers = 3
user = "nobody"

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    li = env[QUERY_STRING].split("&")
    resp = [el+"\r\n" for el in string]
    return resp
