# pythonTest
get modules working

## Push #1

Set up repo and get individual scripts working correctly

```
MyProject/
    ThingOne/
        getAPI.py
    ThingTwo/
        getAPI.py
```

Running either python script, each pulls a generation of data from the pokemon api. Notice that both scripts are extemely similar
`python ThingOne/getAPI.py` gets Gen1 data from public API with a GET request

## Push #2

Attempting to follow documentation: https://docs.python.org/3/tutorial/modules.html#packages
Modify repo to include a common.py file and empty __init__.py files in every directory

```
MyProject/
    __init__.py
    common.py
    ThingOne/
        __init__.py
        getAPI.py <-- modified to use common.py for api_base variable
    ThingTwo/
        __init__.py
        getAPI.py
```

Running ThingOne/getAPI.py now will result in an error message like:

> Traceback (most recent call last):
>
>   File "c:\Users\Greenjam94\Code\pythonTest\MyProject\ThingOne\getAPI.py", line 3, in <module>
> 
>    from MyProject import common
> 
> ModuleNotFoundError: No module named 'MyProject'

## Notes from veender
From [How to Fix ModuleNotFoundError and ImportError](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c):

- A python module is a single file with a .py extension.
- A python package is a folder that contains at least one python module. For python2, a package requires a __init__.py file

This is not the only way to solve this, I am not a Python expert, etc.

Your PYTHONPATH is important. I wasn't able to get this to work in either my Windows or Ubuntu environments without adding the project filepath to that environment variable. 

Good luck!
