# Questions
Good answers:
https://gist.github.com/OxiBo/1f5f19d3aa7da1de0de73f89435e49cf#:~:text=The%20first%202%20bytes%20of,ASCII%20or%200x4D42%20in%20hexadecimal.
https://github.com/JGTR/cs50/blob/master/pset4/questions.txt#:~:text=7.,an%20unsigned%2016%20bit%20int.

## What's `stdint.h`?

`stdint.h` — заголовочный файл стандартной библиотеки языка Си, введённый стандартом C99. Заголовочный файл объявляет несколько целочисленных типов и макросов.

<stdint.h> is a header file in the C standard library that has to be included in a program, if you need to
declare sets of integer types having specified widths, and define corresponding sets of macros. 
It shall also define macros that specify limits of integer types corresponding to types defined in other standard headers. 
The exact-width types and their corresponding ranges are only included in that header if they exist for that specific compiler/processor.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

These functions are a cross-platform implementation of a standard data type.
`uint8_t` is an unsigned int of 8 bits, `uint32_t` is an unsigned long long, `int32_t` is a signed long long, and a `uint16_t` is an unsigned 16 bit int.

Using uint8_t, uint32_t, int32_t, and uint16_t in a program is needed to make it clear that you intend to use data in specific way and 
your data type is going to be of certain ranges. Using those types will let you use data within the ranges you need, 
also knowing how wide your data type is going to be (for exapmple: uint32_t is going to be exactly 32 bits
with the maximum value 2^32-1 which equals 4,294,967,295)

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

`BYTE` is 1 byte, `DWORD` is 4 bytes, `LONG` is 4 bytes, `WORD` is 2 bytes

BYTE (uint8_t) is 8 bits (1 byte);
DWORD (uint32_t) is 32 bits (4 bytes);
LONG (int32_t) is 32 bits (4 bytes);
WORD (uint16_t) is 16 bits(2 bytes)

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The first two bytes of any BMP file should be "B", "M" in ASCII; 66, 77 - decimal, 42, 4D - hexadecimal.

The first two bytes of any BMP file are used to identify the file. A typical application reads this block (the first two bytes) first to ensure that the file is actually a BMP file and that it is not damaged. 
The first 2 bytes of the BMP file format are the character "B" and "M" in ASCII or 0x4D42 in hexadecimal.
All of the integer values are stored in little-endian format (i.e. least-significant byte first).

## What's the difference between `bfSize` and `biSize`?

bfSize describes the entire file size in bytes, whereas biSize is the size of BITMAPINFOHEADER in bytes.

bfSize (is a member (field) of the BITMAPFILEHEADER structure (struct) which contains information about the type, size, and layout of a file that contains a DIB) represents the size, in bytes, of the bitmap file.
biSize (is a member (field) of the BITMAPINFOHEADER structure (struct) which contains information about the dimensions and color format of a DIB) represents the number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

Negative biHeight means the bitmap is is a top-down DIB with the origin at the upper left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the number of bits-per-pixel. The biBitCount member of the BITMAPINFOHEADER structure 
determines the number of bits that define each pixel and the maximum number of colors in the bitmap.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Fopen is supposed to return a file pointer for the new file. We check if it is not equal to NULL to make sure 
we get legitimate pointer back. Reasons why fopen might return NULL (not limited to):
- the file doesn't exist;
- the file is opened in a mode that doesn't allow other accesses;
- the network is down;
- the file exists, but you don't have permissions;
- fopen cannot return legitimate pointer back.

## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

Argument 1 in fread function means that fread will read one element from a given file, namely reads infile's BITMAPFILEHEADER, infile's BITMAPINFOHEADER, RGB triple from infile.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
(4-(3*3(RGBTRIPLE equals 3 bytes)%4)%4=3. so int paddling is equals 3. 
If the width is 3, padding is necessary since the scanline must be a multiple of 4.
3 bytes are added to bring the scanline to 12 bytes. 
(3 pixels) × (3 bytes per pixel) + (3 bytes of padding) = 12 bytes, which is indeed a multiple of 4.

## What does `fseek` do?

Fseek allows to remind or fast-forward within a file (changes the location of the file pointer).
In copy.c fseek skips over padding, if any, and looks for the next pixel.

## What is `SEEK_CUR`?

This is an integer constant which, when used as the whence argument to the fseek function, specifies that the padding provided 
is relative to the current file position. SEEK_CUR moves file pointer position to given location.
(The value of whence must be one of the constants SEEK_SET, SEEK_CUR, or SEEK_END, 
to indicate whether the offset is relative to the beginning of the file, the current file position, 
or the end of the file, respectively.)
(Function: int fseek (FILE *stream, long int offset, int whence).
