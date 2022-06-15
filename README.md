# AutoML Benchmark
The AutoML Benchmark provides an overview and comparison of open-source AutoML systems
# Steps
## Installation Linux Ubuntu
### Pre-requisites
To run the benchmark, you will need:
- Python 3.7+
- PIP3

###  Installation
- Download Folder: SystemMetaLearning

```sh
sudo apt-get update
sudo apt install python3-venv
sudo apt-get install python3-virtualenv
```
## Installation Windows
### Pre-requisites
To run the benchmark, you will need:
- [Python](https://www.python.org/downloads/release/python-375/) - Python
```sh
cd SystemMetaLearning
```
Create a virtual environment Linux Ubuntu:
```sh
python3 -m venv ./venv
source venv/bin/activate
```
Create a virtual environment Windows:
```sh
python3 -m venv ./venv
source venv\Scripts\activate
```
Then pip install the dependencies:

```sh
python -m pip install -r requirements.txt
```

### Quickstart

```sh
python3 runbenchmark.py autoweka exampletest test
```


