# valid_parentheses
solution to find if parentheses and brackets are valid (opening and close)

## How it works

check the string against the dictionary, characters should match.

step1: 
check if the stack actually has value

step2:
check the last value of the input

step3:
compare against the dictionary (which maps the values properly)

```
(
(
[
[
{
{
```

## Results

Swap out `input_string` to test

with `input_string = "()[]{}"`:
```
» python3 main.py
True
```

with `input_string = "("`:
```
» python3 main.py
False
```