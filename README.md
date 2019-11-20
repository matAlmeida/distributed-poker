# Distributed Poker

Created by `Matheus Almeida` and `Gabriel Goes`.

## Developing

This project uses `Python 3.7`.

Before you start code you will need to setup the virtual environment. In order to do this install `Pipenv` using one of the following commands:

```sh
$ brew install pipenv # for Mac OSX
$ pip3 install pipenv # for Unix
$ pip install pipenv  # for Windows
```

If you are in Unix add the following lines at the end of your `.bash_profile`:

```sh
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

If you are on Windows use the following command:

```sh
set PATH=%PATH%;set PATH=%PATH%;'c:\users\<YOUR_WINDOWS_USER>\appdata\local\programs\python\<PYTHON_FOLDER>\Scripts'
```

`Note: Check your python folder name, it will be something like "python37-32"`

Now you can start the virtual environment and install the dependencies

```sh
$ pipenv --python 3.7
$ pipenv install
$ pipenv shell  # to start the virtual env
```

`Note: While installing the dependencies you may get stuck on "Locking", it is ok.`

To get out of the virtual environment type `exit`.