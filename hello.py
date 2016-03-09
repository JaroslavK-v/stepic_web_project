#возвращает документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку

def application(env, start_response):
start_response('200 OK', [('Content-Type', 'text/plain')])
return ["Hello!"]
