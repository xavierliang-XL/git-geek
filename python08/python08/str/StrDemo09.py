str = "hello world and hello bytetube and hello dal and hello python"
beginIndex=str.index("hello")
endIndex= str.index("bytetube")
def findTheHelo(str):
    """
    the method is to find the 'hello' word by using begin index and end index from a string
    str:string
    """
    return (str.count("hello",beginIndex,endIndex))
