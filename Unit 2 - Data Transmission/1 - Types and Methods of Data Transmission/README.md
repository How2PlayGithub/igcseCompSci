# Types and Methods of Data Transmission

## Data Packets
- Packet Structure
    - Header
    - Payload
    - Trailer

- Header
    - Contains the IP address of the sender and the receiver
    - Sequence number of the packet
    - Size of packet

- Payload
    - Contains the data

- Trailer
    - Includes a method of identifying the end of the packet
    - Error-checking methods

## Packet Switching
- Method of data transmission where the data is broken into *multiple packets*
- Packets are sent independently from start to end
- Packets are reassembled at the receiver's computer

| Advantages | Disadvantages |
|--|--|
|No need for a single line | Packet loss |
| Fix issue of busy / failed nodes | Prone to real-time streaming |
| High data transmission speed | Delay at the receivers end when packets are getting reordered |
| Easy to expand useage | |

## Data Transmission
- Simplex: one direction
- Half-duplex: both directions, one at a time
- Full-duplex: both directions, same time
- Serial data: data sent one bit at a time
- Parallel data: several bits are sent down several wires at once

## Serial vs Parallel

| Serial | Parallel |
|--|--|
|Better for long distances | Better for short distances |
| Cheap | Expensive |
| Used when size of data is small | Used when speed is needed |
| Slower | Faster |
