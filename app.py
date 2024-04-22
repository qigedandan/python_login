import json


def load_users():
    try:
        with open("db.txt", "r") as file:
            return json.load(file)
    except:
        print("无法读取用户信息，请检查文件是否存在。")
        exit()


def save_users(users):
    with open("db.txt", "w") as file:
        json.dump(users, file)


def register():
    username = input("请输入用户名: ")
    users = load_users()
    if username in users:
        print("用户名已存在，请重新注册。")
        return
    while True:
        password = input("请输入密码: ")
        if not password.isalnum() or len(password) < 8 or len(password) > 16:
            print("密码必须只包含字母和数字，并且长度在8到16位之间，请重新输入。")
        else:
            confirm_password = input("请再次输入密码: ")
            if password != confirm_password:
                print("两次输入的密码不匹配，请重新输入。")
            else:
                users[username] = password
                save_users(users)
                print("注册成功！")
                return


def login():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    users = load_users()
    if username not in users or users[username] != password:
        print("用户名或密码错误，请重新登录。")
        return
    print("登录成功！欢迎回来，" + username)


def main():
    while True:
        print("1. 注册")
        print("2. 登录")
        print("3. 退出")
        choice = input("请选择操作: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
