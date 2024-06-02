# Methods of Error Detection

## Parity Check
- It uses the number of 1-bits in a byte
- Type types:
    - Even - Even number of 1 bits
    - Odd - Odd number of 1 bits

e.g
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
|-|-|-|-|-|-|-|-|

- The LMB is the parity bit
- As the number of 1's (4) is even, it'll be set to even (0)

**Limitations**
- 2 bits may change during transmission
    - Error won't be detected
- Bits changed won't be identified

**Parity Blocks**
- To overcome limitations, parity blocks are used

e.g
| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | |
|-|-|-|-|-|-|-|-|-|
| A | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| B | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| C | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 |
| D | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 |
| E | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| | 1 | 1 | 1 |0 | 0 | 1 | 1 | 1 |

## Checksum
- Whenever a block of of data needs to be sent, the sender would calculate the checksum using an algorithm 
- Once the data is sent, the receiver would calculate the checksum again with the:
    - Same data
    - Same algorithm
- The receiver checks the value received with the value calculated 
- If unmatched, a request is sent to resend the data

## Echo Check
- Once the data is sent, the receiver would send the data back for verification
- The sender would compare the received and the original for errors

**Limitations**
- We don't know if the error occurred when sending it back or not

## Check Digit
- Calculated from all the other digits in the data (ex-codes)
- Check digit is the last digit of the code
- Generally used to identify mistyping errors:
    
    e.g 

    6372 as 6379

    8432 as 842

    9382 as 9823

## Automatic Repeat Requests (ARQs)
- Uses:
    - Acknowledgement 
    - Timeouts
- Makes sure the user receives the data
- Receiver would check for errors
    - If none is found:
        - Positive acknowledgement
    - Else:
        - Negative acknowledgement
        - Data resent
- Sender uses timeouts to wait for x time for the acknowledgement
- If no acknowledgement, the data is sent again to the receiver
