# Binary Calculations

## Points to Note
**NOTE: Binary values cannot be calculated the same way denary are added.**
- 0 + 0 = 0
- 1 + 0/0 + 1= 1
- 1 + 1 = 0 (1 carry)
- 1 + 1 + 1 = 1 (1 carry)

## Overflow values
- When adding 2 values, if the answer goes past the limit of given values, it is called overflow.
- It shows that the memory doesn't have enough space to store the answer

## Adding 2 values
Take the binary sequence `1101110` and `11011110`. To add them together:
1. Convert both the bytes into 8 bits. In our case, it'll be `01101110` and `11011110`
2. Add the values. If the answer is 2, carry it over into the next column
|  Carry |     1    | 1 | 1 | 1 | 1 | 1 | 1 |   |   |
|--------|----------|---|---|---|---|---|---|---|---|
| Byte 1 |          | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| Byte 2 |          | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 |
|        | Overflow |   |   |   |   |   |   |   |   |
| Answer | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |

## Logical shifts
- A logical shift means to move a binary digit to either the left or the right
- The bit being **emptied** is going to become `0`

## Two's complements
Two's complements is:
- A method used to represent negative values in binary
- The MSB (most significant bit) is replaced from `128` to `-128` so the range of values of the two's complement bytes will be `-128 to 127`

## Converting binary into two complements
Take the example `1101100`. To convert binary into two complements:
1. Find the first `1` from the **right**. In our example, it'll be in the 3rd index
2. Switch each value after the `1`. In our example, it'll be `0010100` 
So, `0010100` is the complement of `1101100`

## Converting negative values into two complements
To convert binary to two complements:
1. Find the binary equivalent of the value ignoring the `-` sign
2. Convert the binary value into two's complement
3. Make the MSB 1 if it isn't already 1

## Converting two's complement value into denary
You do the same thing as normal, but the MSB will be changed to a negative.
For example `10111010`:
| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|------|----|----|----|---|---|---|---|
|   1  |  0 | 1  | 1  | 1 | 0 | 1 | 0 |

So, the denary value will be `-128 + 32 + 16 + 8 + 2` which equals to `-70`
