# DataShare - Simple library for data sharing between scripts and public functions calling.

# Installation.
Install code,<br>
Delete LICENSE, README, readme.txt (optionaly),<br>
Unpack datashare to "$PYTHON_PATH\lib\",<br>
Done!

# Examples.
Let's create "server and client".

post.py
```python
from datashare import DataCenter


# Creating data center.
appdata = DataCenter(
  1920,
  1080,
  'Name',
  '%Path',
  False
)
```

get.py
```python
from datashare import Get


data = Get('post') # "post" - post.py
settings = data.get('appdata') # "appdata" - data center name
```

Result.
```
(1920, 1080, 'Name', '%Path', False)
```

So, how you can see, now we maked this data public, and every script can get it.
Let's create "server and client", but with functions and simple app example.

post.py
```python
from datashare import FunctionsCenter


funcs = FunctionsCenter(
  lambda: print('Welcome!'),
  lambda: print('Sorry!')
)
```

client.py
```python
from datashare import FunctionsCaller


userinp = input('You are older that 18?: ').lower()
functions = FunctionsCaller('post')

functions.callif('funcs', userinp == 'yes', 1, False)
functions.callif('funcs', userinp == 'no', 2, False)
```

Run it.
```
You are older that 18?: Yes
Welcome!

You are older that 18?: no
Sorry!
```

Get version.
```python
from datashare import DATASHARE_VERSION

print(DATASHARE_VERSION)
```

# Conclusion.
So, how you can see, how strong and simple this library! When need to use this library? When you need create public data or function(s) for another scripts, it's like a database. This library in BETA, so you can spectate bugs, errors, or typing errors, sorry for that, we fix all soon!

# End.
Thank you for reading, i hope you liked my library, good luck, bye!
