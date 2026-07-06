# Python – String Methods (zápisky)
 
Přehled užitečných metod pro práci s řetězci (`str`) v Pythonu. Ke každé je krátký popis a příklad.
 
---
 
## `split(separator)`
 
Rozdělí řetězec podle zadaného oddělovače na seznam (list) řetězců. Pokud oddělovač nezadáš, rozdělí se podle mezer.
 
```python
my_str = 'hello world'
 
split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```
 
---
 
## `join(iterable)`
 
Spojí prvky iterovatelného objektu (např. listu) do jednoho řetězce, odděleného zadaným separátorem.
 
```python
my_list = ['hello', 'world']
 
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```
 
---
 
## `startswith(prefix)`
 
Vrátí `True`/`False` podle toho, zda řetězec začíná zadaným prefixem.
 
```python
my_str = 'hello world'
 
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```
 
---
 
## `endswith(suffix)`
 
Vrátí `True`/`False` podle toho, zda řetězec končí zadaným sufixem.
 
```python
my_str = 'hello world'
 
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```
 
---
 
## `find(substring)`
 
Vrátí index prvního výskytu podřetězce, nebo `-1`, pokud ho nenajde.
 
```python
my_str = 'hello world'
 
world_index = my_str.find('world')
print(world_index)  # 6
```
 
---
 
## `count(substring)`
 
Vrátí počet výskytů podřetězce v řetězci.
 
```python
my_str = 'hello world'
 
o_count = my_str.count('o')
print(o_count)  # 2
```
 
---
 
## `capitalize()`
 
Vrátí nový řetězec, kde první znak je velký a zbytek malý.
 
```python
my_str = 'hello world'
 
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```
 
---
 
## `isupper()`
 
Vrátí `True`, pokud jsou všechna písmena velká, jinak `False`.
 
```python
my_str = 'hello world'
 
is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```
 
---
 
## `islower()`
 
Vrátí `True`, pokud jsou všechna písmena malá, jinak `False`.
 
```python
my_str = 'hello world'
 
is_all_lower = my_str.islower()
print(is_all_lower)  # True
```
 
---
 
## `title()`
 
Vrátí nový řetězec, kde je první písmeno každého slova velké.
 
```python
my_str = 'hello world'
 
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```