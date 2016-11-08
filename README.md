# craigslist

Python wrapper for craigslist.

## Disclaimer

- This library is not associated with Craigslist.
- Please read the Craigslist [terms of use](https://www.craigslist.org/about/terms.of.use.en).

## Install
```
pip3 install git+https://github.com/AlJohri/craigslist.git
```

## Usage

This library is a WIP.

```
craigslist --help
```

```
craigslist washingtondc --postal 20071 --distance 1 --has_picture --availability within_30_days
```

## Development

### Setup

```
mkvirtualenv craigslist -p python3
pip install --editable .
pip install -r requirements-dev.txt
```
