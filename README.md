<h1 align="center">
  <b>photocrawl</b>
</h1>

A simple package to run analysis and get insight on my use of equipment and settings in my practice of photography.

## Install

This code is compatible with all currently supported Python versions, and requires that you have the great [ExifTool][exiftool] package by Phil Harvey in your `PATH`.
You can install it in your virtual enrivonment with:

```bash
python -m pip install photocrawl
```

## Usage

With this package installed in the activated enrivonment, it can be called through `python -m photocrawl` or through a newly created `photocrawl` command.

Detailed usage goes as follows:

```bash
 Usage: python -m photocrawl [OPTIONS] [IMAGES]                                   
                                                                                  
 Crawl and ensemble of pictures to run analysis of their metadata and get insight 
 on one's use of equipment and settings in their practice of photography.         
                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────╮
│   images      [IMAGES]  Location, relative or absolute, of the images          │
│                         directory you wish to crawl.                           │
│                         [default: None]                                        │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────╮
│ --output-dir                                 TEXT  Location, either relative   │
│                                                    or absolute, of the output  │
│                                                    directory.                  │
│                                                    [default: outputs]          │
│ --show-figures          --no-show-figures          Whether or not to show      │
│                                                    figures when plotting       │
│                                                    insights.                   │
│                                                    [default: no-show-figures]  │
│ --save-figures          --no-save-figures          Whether or not to save      │
│                                                    figures when plotting       │
│                                                    insights.                   │
│                                                    [default: no-save-figures]  │
│ --log-level                                  TEXT  The base console logging    │
│                                                    level. Can be 'debug',      │
│                                                    'info', 'warning' and       │
│                                                    'error'.                    │
│                                                    [default: info]             │
│ --install-completion                               Install completion for the  │
│                                                    current shell.              │
│ --show-completion                                  Show completion for the     │
│                                                    current shell, to copy it   │
│                                                    or customize the            │
│                                                    installation.               │
│ --help                                             Show this message and exit. │
╰────────────────────────────────────────────────────────────────────────────────╯
```

The script will crawl files, extract EXIF information and output insights visualizations named `insight_1.png` and `insight_2.png` in a newly created `outputs` folder (or a folder named as you specified).

## Output example

Here is an example of what the script outputs:

![Example_1](example_outputs/insight_1.jpg)

![Example_2](example_outputs/insight_2.jpg)

## TODO

- [x] Handling raw files.
- [x] Handling subfolders when looking for files.
- [x] Output all insight in a single/two plot.
- [x] Implement proper logging.
- [x] Make into a package.
- [x] Make callable as a python module (`python -m photocrawl ...`).
- [x] Improving the command line experience.

---

<div align="center">
  <sub><strong>Made with ♥︎ by fsoubelet</strong></sub>
  <br>
  <sub><strong>MIT &copy 2019 Felix Soubelet</strong></sub>
</div>


[exiftool]: https://www.sno.phy.queensu.ca/~phil/exiftool/
