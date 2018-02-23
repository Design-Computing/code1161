import os
# install virtualenv

# create virtualenv
os.system('conda create -n codeenv python=3.6 anaconda')
# activate the virtualenv
os.system('source activate codeenv')
# try and install requests
os.system('pip install requests')
os.system('code --install-extension ms-python.python')
# install python ext
