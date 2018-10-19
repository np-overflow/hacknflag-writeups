# Source Code

To be able to solve this challenge, you would need to know that compiling an exe from python source code is not a good idea for source protection.

If compiled using pyinstaller or py2exe, there are numerous tools to reverse the compilation.

To get started, you would need the pyinstaller extractor script. It can be found on sourceforge.

Run `$ python pyinstxtractor.py give-me-the-flag.exe`

Then navigate to the extracted folder and you should see the give-me-the-flag file.

Running `$ file give-me-the-flag` would reveal that it is a data file.

Simply open the file and look for the flag using `$ strings give-me-the-flag | grep HNF`

## flag

`HNF{H0w_d1D_y0u_se3_my_5OURc3_k0D3}`
