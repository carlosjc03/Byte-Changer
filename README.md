# Byte-Changer
Exchanges program position bytes as a cheat engine and also, from an initial memory address, finds out the memory addresses corresponding to those bytes. Ideal for making cheats for NDS or 3DS!

In Cheat Engine, **byte positions are reversed** compared to how they actually have to look when making a cheat. For example if you wanna make a cheat based on the cheat engine values, you have to reverse them.

![image](https://github.com/user-attachments/assets/4a9b1823-380a-4991-94ec-4ea4f9d2e761)

As you can see in the capture, the values ​​are **CD CC 70 43**. However, if we put these values ​​as is in our determined memory address (for example let's suppose that the address is 084C0B30), in theory we should write 084C0B30 CDCC7043, **but it's NOT like that**. If you write that, **what will actually be written to your memory address is this:**

![image](https://github.com/user-attachments/assets/f8c3b2ed-b3ee-40b7-960f-9d4e2bad69a3)

This is usually not a problem for cheats that only take 1 or 2 lines of code. The problem is when the cheat takes up many lines, where having to manually reverse the text is quite tedious.

This is where this program really comes in handy. Simply enter **all the bytes you want to include in your code** **and the base memory address**, **and the program will be able to generate a cheat with all the correct values ​​in just a few seconds.**

The program also checks if the number of bytes is valid, by checking if the total number of bytes is divisible by 8 (because 8 are the characters in each line of a Nintendo Cheat).

You have also to consider these things:
<ol>You have to write your base address **without first two numbers**, that is, if your address is **084C0B30**, you must write only **4C0B30** or the cheat will be wrong. This is done beacuse in Citra and some 3ds games, you need to fix the address with D3000000 XX000000 (where XX is the first **two numbers** of your base address) or the cheat won't work. By default first two bytes are fixed to be 14 (like if the adress will be 144C0B30), but you can change it writing your desired value </ol>
<ol>You can modify some parameters of this program to suit your need. For example you can modify the number of characters of each line, meaning you can use this program to make cheats for other platforms</ol>


