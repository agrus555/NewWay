txt = "aopjefiouioeiomusneuichihumuceroijwdsnklfjioefjdaskf"
a_num = 0
o_num = 0
e_num = 0
i_num = 0
u_num = 0
for i in range(0, len(txt)):
    if "a" in txt[i]:
        a_num += 1
    elif "o" in txt[i]:
        o_num += 1
    elif "e" in txt[i]:
        e_num += 1
    elif "i" in txt[i]:
        i_num += 1
    elif "u" in txt[i]:
        u_num += 1
print(f"a_num = {a_num}")
print(f"o_num = {o_num}")
print(f"e_num = {e_num}")
print(f"i_num = {i_num}")
print(f"u_num = {u_num}")
