# AiMySearch [![Build Status](https://travis-ci.org/egusahiroaki/aimysearch.svg?branch=master)](https://travis-ci.org/egusahiroaki/aimysearch)

AiMySearch is tool for fuzzy search.

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

## License

MIT
