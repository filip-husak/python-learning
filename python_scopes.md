# Scope v Pythonu

## Klíčový rozdíl oproti C#

Python **nemá block scope** (na rozdíl od C#). Scope je vázaný na **funkci**, ne na `{ }` blok.

```python
def test():
    if True:
        x = 10
    print(x)  # funguje, vytiskne 10 -- x "přežije" mimo if
```

V C# by `x` mimo `if` neexistovalo. V Pythonu ano, protože `if`, `for`, `while` **nevytváří nový scope**.

---

## LEGB pravidlo

Python hledá jméno proměnné v tomto pořadí:

1. **L**ocal – uvnitř aktuální funkce
2. **E**nclosing – v obalující (vnější) funkci, pokud jde o vnořenou funkci
3. **G**lobal – na úrovni modulu (souboru)
4. **B**uilt-in – vestavěné (`len`, `print`, `range`, ...)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)      # local

    inner()
    print(x)          # enclosing

outer()
print(x)               # global
```

---

## `global` klíčové slovo

Bez `global` nelze uvnitř funkce **přepisovat** globální proměnnou (jen číst).

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Bez `global counter` by přiřazení `counter += 1` vyhodilo `UnboundLocalError` -- Python by `counter` považoval za lokální proměnnou (protože se do ní ve funkci přiřazuje), ale ještě by neměla hodnotu.

---

## `nonlocal` klíčové slovo

Používá se u **vnořených funkcí**, když chceš měnit proměnnou z obalující funkce (ne globální).

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = make_counter()
print(c())  # 1
print(c())  # 2
```

`global` → jde až na úroveň modulu.
`nonlocal` → jde jen o jednu úroveň výš (enclosing).

---

## Časté chyby

### `UnboundLocalError`

```python
x = 5

def broken():
    print(x)   # chyba!
    x = 10
```

Python vidí přiřazení `x = 10` kdekoliv ve funkci a **automaticky považuje `x` za lokální v celé funkci** -- i na řádcích před přiřazením. Proto `print(x)` selže.

### List comprehension má vlastní scope

Od Pythonu 3 mají comprehensions (`[x for x in ...]`) svůj vlastní scope, na rozdíl od `if`/`for`.

```python
[i for i in range(5)]
print(i)  # NameError: i neexistuje mimo comprehension
```

---

## Shrnutí

| Klíčové slovo | Co dělá |
|---|---|
| (nic) | čtení proměnné podle LEGB |
| `global x` | přiřazení míří na globální `x` |
| `nonlocal x` | přiřazení míří na `x` v obalující funkci |

**Pravidlo:** pokud se do proměnné ve funkci **přiřazuje**, Python ji bez `global`/`nonlocal` považuje za lokální -- pro celou funkci, i před samotným přiřazením.
