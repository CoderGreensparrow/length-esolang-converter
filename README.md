# length-esolang-converter
A different way of writing code in the esoteric programming language *Length*
## What is this?
This repository contains a python script. This python script can convert programs written in the esoteric programming language *Length* to what I call **semi-length code**. This code is probably more readable than pure *Length* code.
### What is semi-length code?
**Semi-length code** is not an official name, but it refers to writing *Length* with the names of the commands from the [wiki article of Length](https://esolangs.org/wiki/Length).
## Example
Lets say you have this [truth-machine](https://esolangs.org/wiki/Truth-machine) code from the article:
```123456789
1234567890123456789012345
123456
1234567890123456789012345
12345678
12345678901234567890
12345678901
1234567890123
12345678901234
123456789012345
1234567890123456789012345

123456789012345
12345678901234
123456789012354678901234567890
1234567890123456789012345
1
123456789012345
12345678901234
123456789012345
```
Now let's convert it to **semi-length code**:
```inp
push 6
push 8
mul
sub
cond
gotou 15
push 0
outn
gotou 30
push 1
outn
gotou 15
```
## Usage
### Conversion
Using a command line interface is recommended. Example: command prompt on Windows<br>
***Make sure Python 3+ is installed on your computer***<br>
If not [get it from here](https://www.python.org/downloads/)
###### Windows
1. Type the route to the python file (ex. C:\Users\User\Documents\LengthConverter.py
2. After a SPACE type len-to-semi or semi-to-len. **len-to-semi**: converts the contents of the file to semi-length and prints them out to the console **semi-to-len**: converts the contents of the file to length and prints them out to the console
3. After another SPACE type the route to the file you want to convert
4. Press ENTER
###### Mac
Sorry, but if someone know how to do it, thanks for the help!
###### Linux
See the message above
### How to write semi-length
***Knowing how to write Length before knowing how to rite semi-length is recommended***<br>
[Go to the article about Length](https://esolangs.org/wiki/Length) and go to the Instruction Set section. There's a table containing the commands of Length. Normallyyou would write code by the character counts of the lines (see the note above). But with semi-length, you write whats in the Name coloumn to write the command. If a command has a property you write it in the same line after the command with a space inbetween like this:`push 0`
