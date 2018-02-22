import os

# install virtualenv
os.system('pip install virtualenv')
# create virtualenv
os.system('virtualenv venv')
# activate the virtualenv
os.system('source venv/bin/activate')
# install python ext
os.system('code --install-extension ms-python.python')
