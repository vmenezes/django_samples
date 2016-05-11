# Sooner or later we all need to do requests...

This is not a Django project but a quick comparison between few ways
of doing requests on Python 2.7 and 3.4.

The sample code do the same 100 requests in 3 different ways:

- Using a traditional loop with a `requests.get()` call.
- Using `grequests` module, that is async.
- Using Python3 `concurrent` module, that is async.


My superficial findings:

- `grequests` and `concurrent` have same performance on Python 3.4.
- `concurrent` is not available on Python2.7.
- Async methods as `grequests` or `concurent` even on small scale as on this test are about *10x faster*.


To see with your own eyes:

```
virtualenv -p python2 env2
source env2/bin/activate
pip install requirements.txt
python script.py


deactivate

virtualenv -p python3 env3
source env3/bin/activate
pip install requirements.txt
python script.py
```
