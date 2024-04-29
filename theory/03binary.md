# Binary
## Basic Definitions:
- 1 bit: a single 0 or 1
- 1 byte: 8 bits / one character of text
- 1 nibble: 4 bits / half a byte
- 1 KiB (kilibyte): 1024 bytes
- 1 MiB (mebibyte): 1024 KiB
- 1 GiB (gibibyte): 1024 MiB
- 1 TiB (tebibyte): 1024 GiB
- 1 PiB (pebibyte): 1024 TiB
- 1 EiB (exbibyte): 1024 PiB

## What is the binary number system?
Computers use a **binary number system** consisting of only 0's and 1's
Computers only take **2 states**:
- Off (0)
- On (1)
This format is used for storing:
- Text
- Numbers
- Images
- Sounds
- Program Instructions

## Differences between '-obyte'/'-abyte' and '-ibyte'
A '-obyte' or '-abyte' is a number ending in '0'. For example:
- 1 megabyte is 1,000,000 bytes
- 1 kilobyte is 1,000 bytes
Meanwhile, a '-ibyte' is a 1024 unit. For example:
- 1 kilibyte is 1024 bytes
- 1 mebibyte is 1,048,576 bytes (1024 * 1024)

## How to calculate number of combinations:
A bit is always 2^x (power of) where x is the number of bits. For example:
- 1 bit: 2 combinations
- 2 bits: 4 combinations (2^2)
- 3 bits: 8 combinations (2^3)
etc

## What is denary and binary?
Denary is a base 10 number system (0-9) while Binary is a base 2 number system(0, 1)

## Convert from binary to denary
Take the binary '10101101'
1. Count the total number of digits. In this case, it has 8. So the '1' at the very left will have the value: 2^(8-1)
2. Find the next one. Count the number of digits (including it) after. In this case, it has 6. So the value will have 2^(6-1)
3. Repeat this process. 

At the end, the added values will be:
```
2^(8-1) + 2^(6-1) + 2^(4-1) + 2^(3-1) + 2^(1-1)
```
The value of this will be: `173`
So, the binary `10101101` will be `173` in denary.

## Convert denary to binary
Take the dinary '103'
1. Find the highest number possible with 2^x. In this case, it is 2^6. So at the very least, it will have 6 numbers.
` 100000`
2. 2^6 is 64. Minus the initial with the calculated, so 103 - 64 = 39. The next possible is 2^5 (32)
3. Repeat
At the end, it will be
```
2^6 + 2^5 + 2^2 + 2^1 + 2^0
```
So, the binary will be `1100111` for the denary `103`.

## Most and least significant
- The most significant bit (MSB) is the bit with the `largest` value.
- The least significant bit (LSB) is the bit with the `smallest` value.
