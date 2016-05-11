import requests
import grequests
import time


start_time = time.time()
print('Staring blocking requests...')

for i in range(100): 
    req = requests.get('http://google.com/#q=number{}'.format(i))
    print(req.url, req)

end_time = time.time()
print('#'*20)
print('{} secs.'.format(end_time - start_time))
print('#'*20)
print('Sleeping 10 secs to avoid network problems...')
time.sleep(10)




# Requires instalation of grequests and its dependencies
start_time = time.time()
print('Starting async grequests...')

reqs = []

for i in range(100): 
    reqs.append(grequests.get('http://google.com/#q=number{}'.format(i)))

responses = grequests.map(reqs)
print(responses)

end_time = time.time()
print('#'*20)
print('Took {} secs async.'.format(end_time - start_time))
print('#'*20)
print('Sleeping 10 secs to avoid network problems...')
time.sleep(10)




# This won't work on Python2
try:
    import concurrent.futures 

    start_time = time.time()
    print('Starting async requests with Python3 concurrent.futures...')

    def load_url(url, timeout):
        return requests.get(url, timeout = timeout)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        future_to_url = {executor.submit(load_url, 'http://google.com/#q=number{}'.format(url), 10): url for url in range(100)}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(exc)
            else:
                print(data.url, data)


    end_time = time.time()
    print('#'*20)
    print('Took {} secs async.'.format(end_time - start_time))
    print('#'*20)
except ImportError:
    print('concurrent.futures not available on Python2.7')