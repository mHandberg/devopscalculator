import functions_framework
@functions_framework.http
def calculate_http(request):
    """HTTP Cloud Function.
    Args:
        op - operation type [addition, subtraction, multiplication, division]
        a  - the a value
        b  - the b value
    Returns:
        The computed value
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        operation = request_json['op']
    elif request_args and 'name' in request_args:
        operation = request_args['op']
    else:
        return "Err"
    return f"The result of operation is: ${operation(a,b)}"

def addition(a,b):
    
     
     return a+b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
res = addition(a,b)
print(res)
    
    
    
def subtraction(a,b):
    
     return a-b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
res = subtraction(a,b)
print(res)
    ...
    
def multiplication(a,b):
    return a*b
    
def division(a,b):
    return (a / b)
    
