def check_vowels():
    # Código a implementar utilizando input.
print("ingrese un nombre:")
txt=input()
a="a"in txt.lower()
e="e"in txt.lower()
i="i"in txt.lower()
o="o"in txt.lower()
u="u"in txt.lower()
print(f"contiene a: {a}")
print(f"contiene e: {e}")
print(f"contiene i: {i}")
print(f"contiene o: {o}")
print(f"contiene u: {u}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
