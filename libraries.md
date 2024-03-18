# Python Standard Library
[home](readme.md)
[Documentation](https://docs.python.org/3/library/index.html)

## Importing Libraries
```python
    import math #imports everything in the math library
    from math import pi, ceil #direct import only what we need
    from math import sqrt as squareRoot #rename the import
    from math import * #least preferred, global direct import
```

## A Few Name Drops
* [math](https://docs.python.org/3/library/math.html): Mathiness
* [argparse](https://docs.python.org/3/library/argparse.html): Easy to write user-friendly command-line interfaces
* [json](https://docs.python.org/3/library/json.html): JSON encoder and decoder
* [os](https://docs.python.org/3/library/os.html): Operating system interface
* [sys](https://docs.python.org/3/library/sys.html): System specific paarameters and functions
* [pdb](https://docs.python.org/3/library/pdb.html): Python debugger

# Python Third Party Modules
Manage with `pip`
```shell
    pip --version   # supports a specific version

    #Install a package
    pip install boto3   #AWS client

    #List installed packages
    pip freeze
    pip freeze > requirements.txt #Stores off install list
    pip install --user -r requirements.txt #Install required packages
```
# Virtual Environments
## Run a Virtual Environment
Run isolated scenarios in virtual environments
```shell
    mkdir ~/venvs #create a directory to store your virtual environments
    python -m venv venvs/pg #make a "pg" virtual environment
    ls ~/venvs/pg/bin   #there is an activate file here
    source ~/venvs/pg/bin/activate #this will start your venv
    deactivate  #exit virtual environment
```
## Manage an environment
```shell
    pip install pipenv
    #within project directory
    pipenv --python pythonVersion
    ls  #Pipfile, this is basically your python version of package.json
    pipenv shell #launches your venv, since the path to the activate is obtuse
    #within your venv
    pipenv install whatever
    exit #exit your pipenv environment
```
