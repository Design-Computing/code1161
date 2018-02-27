import os
# install virtualenv

# create virtualenv
# on macOS /anaconda3/bin/conda create -y  --name codeenv python=3.6
os.system('conda create -y  --name codeenv python=3.6')
# try and install requests
os.system('pip install requests')
# install python ext
os.system('code --install-extension ms-python.python')
# install code runner
os.system('code --install-extension formulahendry.code-runner')
