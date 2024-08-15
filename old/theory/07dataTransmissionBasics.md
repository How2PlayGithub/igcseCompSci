# Data Transmission Basics

## Types and Methods
- Packet Structure
    - Header
        - Contains IP address of the sender and the receiver
        - The sequence number of the packet
        - Size of packet
    - Payload
        - Contains the data
    - Trailer
        - Methods of identifying end of packet
        - Err-checking method

- Packet Switching
    - Method of data transmission where the data is broken into multiple packets
    - Packets sent independently from start to end
    - Reassembled at the receivers PC

| Advantages | Disadvantages |
|------------|---------------|
|no need to make single line of communication | packets could be lost |
|possible to overcome failed or busy nodes | more prone to errors in real-time streaming |
| high data transmission speed | delay at the recievers end when packets are being reassembled |
| easy to expand | |

## Data Transmission
- Simplex: 
    - only one direction
- Half-duplex:
    - both direction but not simultaneously
- Full-duplex:
    - both directions and simultaneously

**NOTE: SERIAL IS FASTER THAN PARALLEL IRL**
- Serial data transmission:
    - data sent one bit at a time
- Parallel data transmission:
    - data sent 1 byte at a time

## Comparison
**NOTE: THIS IS THEORETICAL**

| Serial | Parallel |
|--------|----------|
| better for long distances | better for short distances |
| cheaper | expensive |
| size of transmission is small | used when speed is needed |
| slower | faster |
