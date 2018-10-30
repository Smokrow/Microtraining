call conda remove --name jupyter --all
call conda create python=3.6 -n jupyter
call activate jupyter
call conda install -y -c anaconda jupyter
call conda install -c conda-forge -y tensorflow
call conda install -c conda-forge -y opencv
call conda install -c conda-forge -y matplotlib
