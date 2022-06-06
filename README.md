# password-generator
A cheap password generator CLI. Creates a specified number of passwords each of a particular length (random with replacement).

## Usage
### CLI
```
$ python passgen.py 
```

The output will be a password with default settings for number of characters (16) and number of passwords (1):
```
generated 1 :   9rUe(5.$W=Tp*2V(
```

Alternatively we can pass arguments for number the of passwords to create (using flag `-n`) and length of each password (using flag `-len`):
```
$ python passgen.py -n 5 -len 32
```

This creates 5 passwords, each with a length of 32 characters:
```
generated 1 :   %:!8mU)(%*CJ?LLCIKGWQus7RqlP#YZ4
generated 2 :   5M6c2.mf5wn?.DQ/i[W:2#Kq#$ezJshn
generated 3 :   KNSvPiAFrZuTqhN4P)LJ!MvVwP<aZ)O,
generated 4 :   <#&/JLtdWycm4iIiVu8v$£JSDB4/unfU
generated 5 :   ]*%-E!zE"yuBMKySGFUrOV!OupWIVx&3
```

### In code
The `gen_pass` and `make_passwords` functions can also be used in a script, although `make_passwords` only prints out the generated passwords for the purpose of the CLI (above), so `gen_pass` would be more useful:
```python
>>> from passgen import gen_pass, make_passwords
>>> gen_pass()
'r.<B9D£"zx:j]K/h'
>>> gen_pass(50) # make a 50 character password
'Z*IPJ|A]c6.XHJGPa5p?sjW6v,@gTkDn#j&/?AH(>Ujol?qe)]'
```

The specific characters used can also be changed:
```python
>>> custom_chars = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσΤτΥυΦφΧχΨψΩω'
>>> gen_pass(24, fromchars=custom_chars)
'ΖνΥΟΚΖΦΓυπδχΝνΜφΓΠμψκΧρΚ'
```
