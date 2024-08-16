# Methods of Error Detection

## Parity Checks
- Uses the number of 1-bits in a byte
- Types:
    - Even - Even number of 1 bits
    - Odd - Odd number of 1 bits
- LMB is the parity bit
    - If number of 1's is even, parity bit is even

### Limitations
- 2 bits could change during transmission
    - No error found
- Bit / bits changed wouldn't be identified

### Parity Block
- Overcome the limitation, parity blocks would be used
- Any changes in bits would be identified through rows and columns

## Checksum
- Sender calculates the checksum value using an algorithm
- Receiver recalculates checksum value
- Receiver compares the value received 
    - Aren't matched: data resent

## Echo Check
- Once data sent, receiver resend the data back to the sender for verification
- Sender would compare received and original data

### Limitation
- Don't know if the error happened before or after the data is send

## Check Digits
- Calculated from the other digits in the data
- Check digit is the last digit of the code
- Used to identify mistypes

## Automatic Repeat Requests (ARQs)
- Uses acknowledgement and timeout
- Receiver check data for errors
    - None found: Positive acknowledgement
    - Error found: Negative acknowledgement; Data resent
- Sender uses timeout and waits for `x` time for acknowledgement
    - No acknowledgement: data resent
