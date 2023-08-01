import hashlib
import random
import time

def generate_random_message():
    # 生成 4 字节（32 位）的随机消息
    return bytes([random.randint(0, 255) for _ in range(4)])

def hash_message(message):
    # 使用减弱的SM3哈希函数进行哈希
    return hashlib.new("sm3", message).digest()

def rho_attack(num_attempts):
    # Rho方法攻击
    start_time = time.time()

    for _ in range(num_attempts):
        message = generate_random_message()
        h1 = hash_message(message)

        for _ in range(num_attempts):
            message2 = generate_random_message()
            h2 = hash_message(message2)

            if h1 == h2:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return message, message2, h1, elapsed_time

    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, None, None, elapsed_time

if __name__ == "__main__":
    num_attempts = 2**20  # 尝试的次数
    message1, message2, digest, elapsed_time = rho_attack(num_attempts)

    if message1 and message2:
        print("Rho方法攻击成功!")
        print("消息1: ", message1.hex())
        print("消息2: ", message2.hex())
        print("哈希值: ", digest.hex())
        print("运行时间: {:.4f} 秒".format(elapsed_time))
    else:
        print("Rho方法攻击失败.")
