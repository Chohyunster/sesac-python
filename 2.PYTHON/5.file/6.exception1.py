contents = ""

try:
    with open("file.txt", "w") as file:
        #contents = file.read()
        file.write('Hello')

except:
    print('알수 없는 오류가 발생했습니다.')

# except FileNotFoundError:
#     print("파일이 없습니다.")
# except PermissionError:
#     print("해당파일에는 쓰기 권한이 없습니다.")
# except IOError:
#     print("해당 파일에는 읽기쓰기 권한이 없습니다.")

print("파일내용:", contents)