id = input()
email = input()
password = input()
code = input()

valid = True

if len(id) != 7 or not (id[:3] == "CSE" and id[3] == "-" and
                        '0' <= id[4] <= '9' and '0' <= id[5] <= '9' and '0' <= id[6] <= '9'):
    valid = False

if valid and (email.count("@") != 1 or email[0] == '@' or email[-1] == '@' or email[-4:] != ".edu"):
    valid = False

if valid and (len(password) < 8 or not ('A' <= password[0] <= 'Z') or not (
    ('0' <= password[0] <= '9') or ('0' <= password[1] <= '9') or
    ('0' <= password[2] <= '9') or ('0' <= password[3] <= '9') or
    ('0' <= password[4] <= '9') or ('0' <= password[5] <= '9') or
    ('0' <= password[6] <= '9') or ('0' <= password[7] <= '9')
)):
    valid = False

if valid and (len(code) != 6 or not (code[:3] == "REF" and
                                    '0' <= code[3] <= '9' and '0' <= code[4] <= '9' and code[5] == '@')):
    valid = False

print("APPROVED" if valid else "REJECTED")