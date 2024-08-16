# Compression

## Lossless Compression
- All data from original files are reconstructed
- No data lost
- Algorithm used to compress
- Repeated patterns/text are grouped together in indexes

### Run-Length Encoding
- Reduces the file size of a string of identical data
- Repeated string encoded into 2 values
    - 1st value is the number of identical data items
    - 2nd value is the code of data item
- RLE only effective when theres a long string of repeated bits

## Lossy Compression
- Eliminates unnecessary data
- Impossible to get original file back
- Reduce file quality
- Image resolution and Color depth are reduced
