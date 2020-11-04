str = "hello world and hello bytetube and hello dal and hello python"
def replaceHello(str):
    """
    the method is to replace all the hellos to 'hi'
    str:string
    """
    return(str.replace("hello","hi",100))
print(replaceHello(str))
