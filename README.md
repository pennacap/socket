## Socket
A socket wrapper in Python, in the form of a module

It is a port of https://github.com/lxzan/socket in Python

| Advantages           | Disadvantages      |
|----------------------|--------------------|
| Easy to understand   | Little inefficient |
| Not so bad over all  | Not very optimized |
|                      | Slightly insecure  |

#### Features 

There are quite a few features!

- a read event handler
- a write event handler 
- a transfer message parser 
- a request body

#### Performance 

From tests, an 4000 requests can be sent in 2 seconds with 4 workers

#### Usage  

##### Server 
```python
from server import Server
writer = "" #type: BaseWriter object or subclass object
reader = "" #type: BaseReader object or subclass object
app = Server(writer=writer,reader=reader)
app.run()  # max_listen still is a unused character

```


#### client 

**Work in Progress**


