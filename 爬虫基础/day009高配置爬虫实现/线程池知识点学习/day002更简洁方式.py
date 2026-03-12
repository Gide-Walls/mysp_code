from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x*x

with ThreadPoolExecutor(max_workers=5)as executor:
    results=executor.map(square,[1,2,3,5,6,6,8,8])
    
    for result in results:
        print(result)