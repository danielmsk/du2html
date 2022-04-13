# du2html

**du2html** is a tool to generate human-readable html report from du (disk usage in linux and macos) result.

[<img src="https://img.shields.io/pypi/v/du2html.svg">](https://pypi.org/project/du2html/)
[<img src="https://img.shields.io/pypi/dm/du2html.svg">](https://pypi.org/project/du2html/)

## Installation

- from [pypi](https://pypi.org/project/du2html/)

```
pip install du2html
```

- from [github](https://github.com/danielmsk/du2html)

```
pip install https://github.com/danielmsk/du2html/raw/main/dist/du2html-0.0.5-py3-none-any.whl
```

### Dependency

This **du2html** doesn't need any other package:

## Options

```
optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i IN, --in IN        input du result file
  -t TOTALSIZE, --totalsize TOTALSIZE
                        total hard disk size (ex: 32t, 100G, 200g)
  -o OUT, --out OUT     output html file
```

## Usage

### Make HTML report

```
du2html -i du_result.txt -t 32t -o du_out.html
```

![](https://raw.githubusercontent.com/danielmsk/du2html/master/docs/screenshot1.png?token=GHSAT0AAAAAABS6DQNIN5LA7MWDY4OFLSYKYSWHKFQ)

## Version History

- 0.0.5 (2022-04-13)
  - add relative path for js and css in template html
- 0.0.4 (2022-04-13)
  - debug
- 0.0.3 (2022-04-13)
  - debug util.py
- 0.0.2 (2022-04-13)
  - update README.md
- 0.0.1 (2022-04-12)
  - first released.
