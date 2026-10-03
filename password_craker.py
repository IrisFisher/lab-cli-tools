def find_password(check):
    from zipfile import ZipFile
    import zlib
    for i in range (len(check)):
        try:
            with ZipFile('whitehouse_secrets.zip') as zf:
                password = check[i].encode('ascii')
                zf.extractall(pwd=password)
                return check[i]
        except (zlib.error, RuntimeError):
            if i%10000==0:
                print(i,'th attempt. Checking, ', check[i])

with open('Ashley-Madison.txt') as f:
    contents = f.read()
    options=contents.split()

password=find_password(options)
print('Password found:', password)
