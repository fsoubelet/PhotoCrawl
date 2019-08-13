# Photography Analyzer

A simply script to run analysis and get insight on my use of equipment and settings in my practice of photography.


## Install

### Prerequisites

This script runs on Python3, and calls the `tqdm`, `matplotlib` and `pandas` packages as requirements.

### Install with Git

You can install this by simply cloning the repository with:

```
git clone https://github.com/fsoubelet/PhotoCrawl.git
```


## Usage

Usage is simple and goes as:

```
python photo_analyzer.py
```

This script will call for you to provide the absolute path to where your images are stored, and output several plots for insight.


## TODO

- [ ] Handling raw files.
As of right now, the script only manages images in the `jpg` format since `Pillow` does not hangle raw files.
- [x] Handling subfolders when looking for files.


## License

Copyright &copy; 2018 Felix Soubelet. [MIT License][license]

[license]: https://github.com/fsoubelet/PhotoCrawl/blob/master/LICENSE 
