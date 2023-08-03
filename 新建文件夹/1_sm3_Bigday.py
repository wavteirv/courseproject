import hashlib
import random

def generate_random_message():
    # 生成 4 字节（32 位）的随机消息
    return bytes([random.randint(0, 255) for _ in range(4)])

def hash_message(message):
    # 使用减弱的SM3哈希函数进行哈希
    return hashlib.new("sm3", message).digest()

def naive_birthday_attack(num_attempts):
    # 执行生日攻击
    hash_table = {}
    for _ in range(num_attempts):
        message = generate_random_message()
        digest = hash_message(message)
        if digest in hash_table:
            message2 = generate_random_message()
            while hash_message(message2) == digest:
                message2 = generate_random_message()
            return message, message2, digest
        hash_table[digest] = message

    return None, None, None

if __name__ == "__main__":
    num_attempts = 2**25  # 生日攻击尝试的次数
    message1, message2, digest = naive_birthday_attack(num_attempts)

    if message1 and message2:
        print("生日攻击成功!")
        print("消息1: ", message1.hex())
        print("消息2: ", message2.hex())
        print("哈希值: ", digest.hex())
    else:
        print("生日攻击失败.")
