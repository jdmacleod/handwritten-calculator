# MDAS Symbol Dataset

## Overview

This dataset consists of 6K images (1K images per class) of common handwritten mathematical symbols for multiplication, division, addition, and subtraction.

### MDAS Symbols

| Operation | Symbol Name | Symbol |
| --------- | ----------- | ------ |
| Addition | plus | &plus; |
| Division | obelus | &divide; |
| Division | slash | / |
| Multiplication | cross | &times; |
| Multiplication | dot | &sdot; |
| Subtraction | minus | &minus; |

The dataset was produced through a combination of handwriting the symbols (two different individuals) and then applying symmetry operations to augment the number of distinct images.

The images are partitioned into a training set (5K), a testing set (0.5K), and a validation set (0.5K).

### Unpacking ZIP Dataset

```bash
unzip mdas_symbols_v1.zip
ls -l symbols_partitioned
```

#### Directory Structure

- symbols_partitioned/
  - test
  - train
  - val

## License

The images are provided under the [MIT License](../LICENSE).
