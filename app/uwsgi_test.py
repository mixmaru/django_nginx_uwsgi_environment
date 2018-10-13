def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    rvalue = b"Hello World\n"
    rvalue += b"\tTest\n"
    rvalue += b"\tJan/13/2017\n"
    return [rvalue]