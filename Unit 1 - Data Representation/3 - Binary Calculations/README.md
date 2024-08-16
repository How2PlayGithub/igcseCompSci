# Binary Calculations

## Notes:
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 0 (1 carry)
1 + 1 + 1 = 1 (1 carry)

## Overflow
When the solution exceeds the limit of given values

## Example

| | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |
|--|--|--|--|--|--|--|--|--|
| + | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| = | 1| 1| 0| 1| 0| 0| 1| 0|

## Logical Shifts
- Moving a binary value to the left or right
- The bit being emptied becomes a `0`

- Shifting left multiplies by 2
- Shifting right divides by 2

## Two's Complement
- Methods to represent *negative values*

i.e.
Make `1011 0101` negative using Two's Commplement

|1|0|1|1|0|1|0|1|
|--|--|--|--|--|--|--|--|
|0|1|0|0|1|0|1|0|
|0|1|0|0|1|0|1|1|

- First reverse all the bits
- Then add `1`
