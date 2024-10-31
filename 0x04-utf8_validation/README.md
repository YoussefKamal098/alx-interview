# Project Documentation: 0x04. UTF-8 Validation

## Project Overview

The **0x04. UTF-8 Validation** project is a Python-based assignment that involves verifying if a given dataset represents valid UTF-8 encoding. The project covers essential programming concepts such as bitwise operations, UTF-8 encoding rules, and list manipulation in Python. Through this project, you will apply and strengthen your understanding of data encoding and character encoding schemes, specifically UTF-8.

## Concepts and Resources

1. **Bitwise Operations in Python**  
   - Mastery of bitwise manipulation, including operators such as AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and bit shifts (`<<`, `>>`).
   - Useful Resource: [Python Bitwise Operators Documentation](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

2. **UTF-8 Encoding Scheme**  
   - Familiarity with UTF-8 encoding patterns and how characters are represented with variable bytes (1 to 4 bytes).
   - Resources:
     - [UTF-8 on Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
     - [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
     - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

3. **Data Representation**  
   - Represent and handle byte-level data, specifically focusing on manipulating the least significant bits (LSB) of integers to validate byte data.

4. **List Manipulation in Python**  
   - Iterate through lists, access elements, and use list comprehensions to handle byte data for UTF-8 validation.

5. **Boolean Logic**  
   - Implement logical operations for decision-making based on bitwise checks of UTF-8 byte patterns.

---

## Requirements

### General Guidelines

- **Editors Allowed**: `vi`, `vim`, `emacs`
- **Execution Environment**: Code will be interpreted on Ubuntu 20.04 LTS with `python3 (version 3.4.3)`.
- **File Standards**:
  - All files should end with a new line.
  - Each file’s first line must be `#!/usr/bin/python3`.
  - **PEP 8** style (version 1.7.x) should be adhered to.
  - All files should be executable.
- **Documentation**: A `README.md` file at the root of the project directory is mandatory.

---

## Task Details

### UTF-8 Validation

Create a Python function that checks if a given list of integers represents a valid UTF-8 encoding.

#### Function Prototype
```python
def validUTF8(data: List[int]) -> bool:
```

#### Requirements
- **Parameters**:
  - `data`: A list of integers, with each integer representing one byte (8 bits) of data.
- **Return**: `True` if the list represents valid UTF-8 encoding, otherwise `False`.
- Each integer in `data` is interpreted as one byte (considering only the 8 least significant bits).
- UTF-8 encoded characters can be represented by 1 to 4 bytes.

#### Example
```bash
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
```
```bash

carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

---
# Additional Information

## What is Unicode?

Unicode is a standardized character encoding system that assigns unique code points to characters from various languages, symbols, and scripts. The main goal of Unicode is to provide a consistent way of encoding, representing, and handling text in computing systems.

- **Code Point**: A unique number assigned to each character in the Unicode standard. For example, the Unicode code point for the character 'A' is `U+0041`.

## UTF-8 Encoding

**Overview**: 
UTF-8 (8-bit Unicode Transformation Format) is a variable-length character encoding for Unicode. It uses one to four bytes to represent a character.

### How it Works:
- **Single Byte (1 byte)**: Represents ASCII characters (0 to 127).
  - Format: `0xxxxxxx`
- **Two Bytes (2 bytes)**: Represents characters in the range of 128 to 2047.
  - Format: `110xxxxx 10xxxxxx`
- **Three Bytes (3 bytes)**: Represents characters in the range of 2048 to 65535.
  - Format: `1110xxxx 10xxxxxx 10xxxxxx`
- **Four Bytes (4 bytes)**: Represents characters in the range of 65536 to 1114111.
  - Format: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

### Example:
Let's encode the character "€" (Euro sign), which has the Unicode code point `U+20AC`.

1. Convert `U+20AC` to binary: `0010 0000 1010 1100`.
2. Since this code point is greater than `0x7FF` (2047), it will be represented in three bytes:
   - The first byte will be `1110xxxx` (3 bytes), so we write `11100010`.
   - The next two bytes will be `10xxxxxx` (continuations), so we fill them in:
     - `10000010`
     - `10101100`

**Final UTF-8 Bytes**: `E2 82 AC` (Hexadecimal representation).

## UTF-16 Encoding

**Overview**: 
UTF-16 (16-bit Unicode Transformation Format) uses one or two 16-bit code units to represent characters. It can handle the full range of Unicode code points.

### How it Works:
- **Single Code Unit (2 bytes)**: Represents characters in the Basic Multilingual Plane (BMP), which covers the first 65,536 Unicode code points (from `U+0000` to `U+FFFF`).
- **Two Code Units (4 bytes)**: Represents characters outside the BMP (from `U+10000` to `U+10FFFF`). These characters are represented using surrogate pairs:
  - First surrogate (high): `110110xxxx xxxx` (from `U+D800` to `U+DBFF`).
  - Second surrogate (low): `110111xxxx xxxx` (from `U+DC00` to `U+DFFF`).

### Example:
Let's encode the character "€" (Euro sign), which has the Unicode code point `U+20AC`.

1. Convert `U+20AC` to hexadecimal: `20AC`.
2. Since `20AC` is within the BMP, it is represented with a single 16-bit code unit:
   - Binary representation: `0010 0000 1010 1100`.
3. Split into two bytes:
   - `00000010 10101100` => `00 20 AC`

**Final UTF-16 Bytes**: `00 20 AC`.

## UTF-32 Encoding

**Overview**: 
UTF-32 (32-bit Unicode Transformation Format) uses a fixed-length encoding scheme, where each character is represented by a single 32-bit (4-byte) code unit. This encoding is simple but can be space-inefficient.

### How it Works:
- Each Unicode code point is represented directly as a 32-bit integer.

### Example:
For the character "€" (Euro sign), which has the Unicode code point `U+20AC`:

1. The code point is represented in a 32-bit format:
   - Binary: `00000000 00000000 00000010 10101100` 
   - Padding it to 32 bits gives us `00000000 00000000 00000000 00101000 11011100`.

**Final UTF-32 Bytes**: `00 00 00 20 AC`.

## Comparison of UTF-8, UTF-16, and UTF-32

| Feature               | UTF-8                                     | UTF-16                            | UTF-32                          |
|-----------------------|-------------------------------------------|-----------------------------------|---------------------------------|
| **Storage Size**      | Variable (1 to 4 bytes)                  | Variable (2 or 4 bytes)          | Fixed (4 bytes)                |
| **Encoding Range**    | `U+0000` to `U+10FFFF`                   | `U+0000` to `U+10FFFF`           | `U+0000` to `U+10FFFF`         |
| **Efficiency**        | More efficient for ASCII (1 byte)        | More space-efficient for BMP      | Less efficient (always 4 bytes)|
| **Compatibility**     | Backward compatible with ASCII            | Not backward compatible           | Not backward compatible         |
| **Usage**             | Widely used on the web (HTML, JSON, etc.)| Common in Windows APIs            | Less common, mainly for internal processing |
| **Performance**       | Slower for characters > 127               | Faster for BMP                    | Fast due to fixed length        |

## Summary

- **UTF-8** is the most common encoding on the web, especially for ASCII characters, as it only uses one byte for these characters. It is variable-length and provides good compatibility.
- **UTF-16** is used in many operating systems and APIs, especially when dealing with Asian characters, due to its efficiency with BMP characters.
- **UTF-32** is rarely used but offers simplicity and direct mapping of Unicode code points, making it suitable for certain applications, especially those requiring high performance with fixed-size characters.

Understanding these differences is essential for choosing the appropriate encoding for your application, depending on the nature of the text data you're working with and the systems you're targeting. 
