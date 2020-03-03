## DevOps Lab -  PYTHON SYNTAX 
### Kirill Baravoy

#### Home task: 03_Classes_and_Packaging 

**_Description of the package_** <br>
This package displays the following host information:
Overall CPU load

● Overall memory usage

● Overall virtual memory usage

● IO information

● Network information 

**_How to install package_** <br>
1) git clone https://github.com/borovoykirill/devops_lab.git
2) cd devops_lab
2) pip install wheel
3) python3 setup.py bdist_wheel --universal
4) After that you can copy file snapshot*.whl from folder dist and there enter command "pip install *file-name.whl*"
5) Type command - snapshot
6) In your current directory will appear JSON with info about host.

**_How to uninstall package_** <br>
Type command - pip uninstall *snapshot*.whl*
