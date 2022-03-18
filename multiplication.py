def calculate_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        #operation = request_json['op']
        return request_json['a'] + request_json['b']
    elif request_args and 'name' in request_args:
        #operation = request_args['op']
        return request_args['a'] + request_args['b']



import functions_framework
@functions_framework.http
def multiplication_http(request):
    ...