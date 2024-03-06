# Installing Python on a Mac
[home](/readme.md)
1. Install python using a python env manager on a mac
    ```bash
        curl https://pyenv.run | bash
    ```
1. Follow output instructions
    ```bash
        #Add this to ~/.zshrc
        export PYENV_ROOT="$HOME/.pyenv"    # Set the pyenv root directory
        [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH" # Add pyenv to the path
        eval "$(pyenv init -)"  # Load pyenv automatically by adding
        eval "$(pyenv virtualenv-init -)"   # pyenv virtualenv
    ```
1. Restart shell
1. Test pyenv install
    ```bash
        pyenv -v
    ```
1. Install python ~~3.7.6~~ 3.9.19
    ```bash
        #This failed, 3.9 is the first version to support M1
        pyenv install 3.7.6
        #Use this instead
        pyenv install 3.9.18
        
        #Check for listing
        pyenv versions
        #Set to global version
        pyenv global 3.9.18
        #Check that setting worked
        python --version    #Python3.9.18

        #Upgrade PIP, python package manager
        pip --version
        #You got PIP with your python install, update it
        pip install --upgrade pip
    ```