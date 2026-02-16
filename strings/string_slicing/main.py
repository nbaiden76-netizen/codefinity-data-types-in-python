full_name = "  Ada Lovelace  "
sentence = "The (quick) brown-fox jumps over 13 lazy dogs!"
email = "  Support@Example.COM \n"
SEP = " | "

# 1) Trim spaces
name_clean = full_name.___

# 2) Check "quick" (case-insensitive)
has_quick = "quick" ___ sentence.___

# 3) Text inside parentheses
start = sentence.___("(")
end = sentence.___(")")
inside_parens = sentence[___]

# 4) Count 'o' (case-insensitive)
o_count = sentence.___.___("o")

# 5) Domain after '@'
email_clean = email.___.___()
at_pos = email_clean.___("@")
domain = email_clean[___]

# 6) Summary string
report = f"{___}{SEP}{___}{SEP}{___}"

print(name_clean, has_quick, inside_parens, o_count, domain)
print(report)