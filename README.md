# FlashText CJK

A fork of [FlashText](https://github.com/vi3k6i5/flashtext) with fixes for CJK (Chinese, Japanese, Korean) language support.

[![PyPI version](https://badge.fury.io/py/flashtext-cjk.svg)](https://badge.fury.io/py/flashtext-cjk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why This Fork?

The original FlashText has a bug where **adjacent keywords in CJK text are not properly extracted**. This is because CJK languages don't use spaces as word boundaries.

### The Problem

```python
from flashtext import KeywordProcessor

kp = KeywordProcessor()
kp.add_keyword('雅詩蘭黛')  # Estée Lauder
kp.add_keyword('小棕瓶')    # Advanced Night Repair

text = '推薦雅詩蘭黛小棕瓶超好用'
result = kp.extract_keywords(text)
# Original FlashText: ['雅詩蘭黛']  ❌ Missing '小棕瓶'
```

### The Fix

```python
from flashtext import KeywordProcessor

kp = KeywordProcessor()
kp.add_keyword('雅詩蘭黛')
kp.add_keyword('小棕瓶')

text = '推薦雅詩蘭黛小棕瓶超好用'
result = kp.extract_keywords(text)
# FlashText CJK: ['雅詩蘭黛', '小棕瓶']  ✅ Both extracted!
```

## Installation

```bash
pip install flashtext-cjk
```

Or install from GitHub:

```bash
pip install git+https://github.com/termdock/flashtext-cjk.git
```

## Usage

The API is 100% compatible with the original FlashText:

```python
from flashtext import KeywordProcessor

# Create processor
kp = KeywordProcessor()

# Add keywords
kp.add_keyword('Python')
kp.add_keyword('機器學習', 'Machine Learning')

# Extract keywords
text = 'I love Python and 機器學習'
keywords = kp.extract_keywords(text)
# ['Python', 'Machine Learning']

# Extract with span info
keywords_with_span = kp.extract_keywords(text, span_info=True)
# [('Python', 7, 13), ('Machine Learning', 18, 22)]

# Replace keywords
new_text = kp.replace_keywords(text)
# 'I love Python and Machine Learning'
```

## Performance

FlashText uses the Aho-Corasick algorithm with O(n) time complexity, making it extremely fast for keyword extraction from large texts.

| Benchmark | FlashText | Regex |
|-----------|-----------|-------|
| 1000 keywords, 1M chars | ~0.1s | ~10s+ |

## Changes from Original

- **Fixed**: Adjacent keyword extraction in CJK languages
- **Maintained**: Full API compatibility
- **Maintained**: All original features (fuzzy matching, etc.)

## Credits

This project is a fork of [FlashText](https://github.com/vi3k6i5/flashtext) created by [Vikash Singh](https://github.com/vi3k6i5).

The original FlashText algorithm is described in the paper: [Replace or Retrieve Keywords In Documents at Scale](https://arxiv.org/abs/1711.00046)

## License

MIT License - see [LICENSE](LICENSE) file.

The original copyright belongs to Vikash Singh (2017). This fork is maintained by [termdock](https://github.com/termdock).
