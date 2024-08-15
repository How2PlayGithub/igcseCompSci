# CPU

## What is the CPU?
- The central processing unit is the center of all modern computers

## Architectures
- It has 4 base architectures:
    - Processor: contains the ALU (Arithmetic Logic Unit)
    - Control Unit: controls the operation of the memory and processor and io devices
    - Arithmetic Logic Unit: carries out the logic system
    - System Clock: produce timing signals on the control bus

## Buses
- 3 main bus types:
    - Address bus
    - Data bus
    - Control bus

The address bus is **unidirectional** 
Data and control bus are both **bi-directional**

## Immediate Access Storage
- Stores instructions that need to be processed that the CPU takes
- 6 main registers

| Register | Abbreviation |
|---|---|
| CIR | current instruction register |
| MAR | memory address register |
| MDR | memory data register |
| PC | program counter |
| ACC | accumulator |

- They all have different functions:
    - CIR: stores the instructions the CPU is currently using
    - MAR: stores the memory address of the instruction. copies and sends to the MDR
    - MDR: stores data from MAR and sends to CIR
    - PC: stores the address of the next instruction
    - ACC: where temporary data is held

- Here's the flow diagram:

![flow diagram](/src/images/immediateAccessStorageFlowDiagram.png)

(taken from GeekforGeeks)

## Fetch-Execute

- 2 terms:
    - opcode: actual instruction for the CPU
    - operand: value that the instruction uses or changes
    - instruction set: set of instructions that the CPU can process. It's in machine code

- There are 3 main steps:
    - fetch
    - decode
    - execute
    
- The first step (fetch) has 5 steps:
    - memory address in MAR is sent to the address bus
    - instructions / data is sent to the CPU through the data bus
    - instructions / data saved in MDR
    - instructions / data copied to CIR
    - program counter += 1

- The second step (decode) has 1 steps:
    - instructions decoded by control unit
        - opcode
        - operand

- The last step (execute) has 2 steps:
    - instructions executed by ALU
        - opcode run on the operand
    - result stored in ACC OR written to memory


- There are 3 concepts:
    - instructions are stored in main memory
    - instructions are fetched, decoded and executed **by the processor**
    - programs can be moved to, and from the main memory

- The memory concept:
    - memory is divided into partitions
    - each partition consists of an address and its contents e.g

    | memory location | content |
    |---|---|
    |10110101 | 00101100 |

## CPU's speed
- There are 4 main things that affect a CPU's speed:
    - Internal Clock
    - Data Buses
    - Cache
    - Cores

### System's Clock
- defines the clock cycle that is merged with all computer operations
- increasing clock speed increeases processing speed
- **does not** mean an increase in performance

- overclocking:
    - it is:
        - using a clock speed **higher** that he computer was designed for
    
    | pros | cons |
    |---|---|
    | increases processing speed | operations become unsynchronised |
    | increase performance in tasks such as rendering | overheating of the cpu |

    - operations being unsynchroised leads to frequent crashes and it being unstable

### Data Busses
- wider the data bus, the higher performance

### Cache
- located in the CPU
- allows for faster access
- stores frequently used instructions that need to be accessed faster
- improves CPU performance

**EXTRA FOR CACHE**
- There are 3 levels of cache

- Level 1 cache:
    - fastest and smallest of the 3
    - holds the cata currently in use by the CPU

- Level 2 cache:
    - holds less data that level 3 cache
    - faster access speeds
    - holds a copy of the most recently accessed data that is **NOT CURRENTLY IN USE**

- Level 3 cache:
    - largest and slowest of the caches
    - twice as fast as DDR4 RAM
    - first CPU cache location to store data after it is moved from RAM

### Cores
- more cores, faster performance
- more core used -> more communication -> data cables
- reduce performance if there are too many
