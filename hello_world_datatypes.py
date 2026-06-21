print("=" * 60)
print("VŠECHNY DATOVÉ TYPY V PYTHONU")
print("=" * 60)

# 1. INT (celá čísla)
print("\n1. INT (Celá čísla):")
integer = 42
negative_int = -100
print(f"   Kladné: {integer}")
print(f"   Záporné: {negative_int}")
print(f"   Typ: {type(integer)}")

# 2. FLOAT (desítková čísla)
print("\n2. FLOAT (Desítková čísla):")
decimal = 3.14
scientific = 1.5e-3
print(f"   Normální: {decimal}")
print(f"   Vědecký zápis: {scientific}")
print(f"   Typ: {type(decimal)}")

# 3. STR (řetězce)
print("\n3. STR (Řetězce):")
text = "Ahoj Python!"
multiline = """Toto je
víceřádkový
řetězec"""
print(f"   Text: {text}")
print(f"   Víceřádkový: {multiline.replace(chr(10), ' ')}")
print(f"   Typ: {type(text)}")

# 4. BOOL (logické hodnoty)
print("\n4. BOOL (Logické hodnoty):")
true_value = True
false_value = False
print(f"   True: {true_value}")
print(f"   False: {false_value}")
print(f"   Typ: {type(true_value)}")

# 5. LIST (seznamy - měnitelné)
print("\n5. LIST (Seznamy - měnitelné):")
my_list = [1, 2, 3, "čtyři", 5.0, True]
print(f"   Seznam: {my_list}")
print(f"   Typ: {type(my_list)}")

# 6. TUPLE (n-tice - neměnitelné)
print("\n6. TUPLE (N-tice - neměnitelné):")
my_tuple = (10, 20, 30, "čtyřicet")
print(f"   Tuple: {my_tuple}")
print(f"   Typ: {type(my_tuple)}")

# 7. DICT (slovníky - klíč: hodnota)
print("\n7. DICT (Slovníky - klíč: hodnota):")
my_dict = {"jméno": "Jan", "věk": 30, "město": "Praha"}
print(f"   Slovník: {my_dict}")
print(f"   Typ: {type(my_dict)}")

# 8. SET (množiny - bez duplikátů)
print("\n8. SET (Množiny - bez duplikátů):")
my_set = {1, 2, 3, 3, 4, 4, 5}  # Duplikáty se ignorují
print(f"   Množina: {my_set}")
print(f"   Typ: {type(my_set)}")

# 9. FROZENSET (neměnná množina)
print("\n9. FROZENSET (Neměnná množina):")
my_frozenset = frozenset([1, 2, 3, 3, 4])
print(f"   Frozen set: {my_frozenset}")
print(f"   Typ: {type(my_frozenset)}")

# 10. BYTES (bajty - neměnné)
print("\n10. BYTES (Bajty - neměnné):")
my_bytes = b"Ahoj"
print(f"   Bytes: {my_bytes}")
print(f"   Typ: {type(my_bytes)}")

# 11. BYTEARRAY (pole bajtů - měnitelné)
print("\n11. BYTEARRAY (Pole bajtů - měnitelné):")
my_bytearray = bytearray(b"Ahoj")
print(f"   Bytearray: {my_bytearray}")
print(f"   Typ: {type(my_bytearray)}")

# 12. COMPLEX (komplexní čísla)
print("\n12. COMPLEX (Komplexní čísla):")
complex_num = 3 + 4j
print(f"   Komplexní číslo: {complex_num}")
print(f"   Typ: {type(complex_num)}")

# 13. RANGE (rozsah - iterátor)
print("\n13. RANGE (Rozsah - iterátor):")
my_range = range(1, 6)
print(f"   Range: {list(my_range)}")
print(f"   Typ: {type(my_range)}")

# 14. NONE (prázdná/nulová hodnota)
print("\n14. NONE (Prázdná/nulová hodnota):")
none_value = None
print(f"   None: {none_value}")
print(f"   Typ: {type(none_value)}")

print("\n" + "=" * 60)
