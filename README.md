# Photography Analyzer

A simply script to run analysis and get insight on my use of equipment and settings in my practice of photography.


## Install

### Prerequisites

This script runs on Python3, and requires the following libraries: `Pillow`, [`PyExifInfo`][pyexifinfo]`tqdm`, `matplotlib`, `seaborn`,  and `pandas`.

### Install with Git

You can install this by simply cloning the repository with:

```
git clone https://github.com/fsoubelet/PhotoCrawl.git
```


## Usage

Usage is simple and goes as:

```
python photo_crawl.py
```

This script will call for you to provide the absolute path to where your images are stored.
An example for me on macos could be `Users/myusername/path/to/files` (do not include the last `/`).
Once provided with a path, the script will crawl files, extract exif and output a file named `insight.jpg` with plotted insight.


## TODO

- [x] Handling raw files.
As of right now, the script only manages images in the `jpg` format since `Pillow` does not hangle raw files.
- [x] Handling subfolders when looking for files.
- [x] Output all insight in a single plot.

## Output example

Here is an example of what the script outputs:

<p align="center">
  <a href="https://xkcd.com/1319/">
    <img src="https://github.com/fsoubelet/PhotoCrawl/blob/master/insight_1.jpg"/>
  </a>
</p>

<p align="center">
  <a href="https://xkcd.com/1319/">
    <img src="https://github.com/fsoubelet/PhotoCrawl/blob/master/insight_2.jpg"/>
  </a>
</p>

## License

Copyright &copy; 2019 Felix Soubelet. [MIT License][license]

[license]: https://github.com/fsoubelet/PhotoCrawl/blob/master/LICENSE 
[pyexifinfo]: https://github.com/guinslym/pyexifinfo
