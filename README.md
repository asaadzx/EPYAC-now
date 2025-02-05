# EPYAC-now
THIS repo is how to install a Locally ai model with hugging face on termux and instraction 

You need to install termux from here ---> Termux](https://termux.com/)

***First Update termux and pkgs***
```
pkg update && pkg upgrade 
```
***Second Install Dependecies***
```
pkg install python git wget
```
***Third install AI framwork Pytourch***
```
pip install torch torchvisoin 

#For hugging face 
pip install -U "huggingface_hub[cli]"

``` 
#For quick start 
```
pip install transformers
```
**Clone repo**
```
git clone https://github.com/asaadzx/EPYAC-now
```
**Run Quick_start file**
```
python Quick_start
```
