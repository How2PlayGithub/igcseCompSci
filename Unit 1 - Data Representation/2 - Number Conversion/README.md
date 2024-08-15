# Number Conversions

## Binary to Denary

| 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |
|--|-|-|-|-|-|-|-|
128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

The denary is `128 + 32 + 16 + 2 + 1 = 179`

## Denary to Binary
132

132 - 128 = 4

4 - 4 = 0

Thus the binary is: `1000 0100`

## Binary to Hexadecimal
| 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |
|--|-|-|-|-|-|-|-|

- Take the first 4 bits (nibble)

|1 | 0 | 1 | 1 |
|--|--|--|--|
|8 | 4 | 2 | 1 |

- Convert into Denary
`8 + 2 + 1 = 11`

- Convert into Hexadecimal
`11 = B`

- Take the next 4 bits (nibble)

|0 | 0 | 1 | 0 |
|-|-|-|-|
|8 | 4 | 2 | 1 |

- Convert into Denary
`2`

- Convert into Hexadecimal
`2 = 2`

- Put them together

Giving the hexadecimal, `B2`

## Hexadecimal to Binary

A3

- Take the first value and change it into denary
`10`

- Convert the first value into binary

| 1 | 0 | 1 | 0 |
|--|--|--|--|

- Take the second value and change it into denary
`3`

- Convert it into binary

|0 | 0 | 1 | 1 |
|--|--|-|-|

Thus the binary is `1010 0011`

## Denary to Hexadecimal
132
- Divide by 16
`132 / 16 = 8 r 4`

Thus the hexadecimal is `84`

## Hexadecimal to Denary

B2
- Take the first value and multiply by 16
`11 x 16 = 176`

- Add the second value to the first value
`176 + 2 = 178`

Thus the denary is `178`
