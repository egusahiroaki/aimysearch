# AiMySearch [![PyPI version](https://badge.fury.io/py/aimysearch.svg)](https://badge.fury.io/py/aimysearch) [![Build Status](https://travis-ci.org/egusahiroaki/aimysearch.svg?branch=master)](https://travis-ci.org/egusahiroaki/aimysearch)

AiMySearch is a tool for fuzzy search. This is useful for detecting typos.

## Installation

install it yourself as:

    $ pip install aimysearch

## Usage

```py
target = "コンピューター"
text = "昨日コンピューターを買ったので、古いコンピュータは友人にあげた。"
s = search.AiMySearch(target, text)
s.run()

# [{'text': '古いコンピュータは友', 'index': 16, 'length': 7}]
```

A third argument is used for choosing the length N-character string fragments. The minimum length of fragments is the same as target word.

A forth argument is match rate in texts.

```py
target = "hogehoge"
text = "hogehogfugafugapiyopihogehugepiyo"
s = search.AiMySearch(target, text, 0, 0.8)
s.run()

# [{'index': 0, 'length': 8, 'text': 'hogehogf'}, {'index': 21, 'length': 8, 'text': 'hogehuge'}]
```

## License

MIT
