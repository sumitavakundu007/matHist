# matHist
A python package to plot normalized histogram using Python3-Matplotlib

It reads a data file which has only one column with a string as header. It the data file doesn't contain a header, it will skip the first line.

## Contributor
- [Sumitava Kundu](https://github.com/sumitavakundu007/), [IACS, Kolkata](http://www.iacs.res.in/).

## Installation
### Prerequisites
1. [python3 or higher](https://www.python.org/download/releases/3.0/)
2. [Python3-numpy](https://numpy.org/)
3. [Python3-matplotlib](https://matplotlib.org/)

#### Using PyPI
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matHist.

```bash
pip install matHist
```

#### Using source code
```bash
git clone https://github.com/sumitavakundu007/matHist.git
tar -xvf matHist-X.X.X
cd matHist-X.X.X
python3 setup.py install --user
```

## Usage

```python
import matHist
matHist.mat_hist_func("input_file.dat", "output_file.png")
```
#### It will ask for few inputs to plot histogram like number of bins (bins), bar width, histogram color etc.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
