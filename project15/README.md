# Project15: implement sm2 2P sign with real network communication
首先，需要实现SM2签名和验证算法。这包括生成密钥对、签名消息和验证签名的功能。接下来，使用Python的socket库来模拟服务器和客户端之间的网络通信。服务器将等待客户端连接，并接收客户端发送的消息。客户端将发送消息到服务器，接收服务器返回的签名，并进行签名验证。

由于过长无法截完全所以用文字形式呈现了结果。
### 运行结果：server

等待客户端连接...

接收到客户端连接： ('127.0.0.1', 55892)

接收到消息： Hello, SM2!

服务器签名： a0f498c39a1e0ed29b22c66fc99032e2d005a64d0d6ee2ab1fc40a63d0b495e0b9b0623c870c6f69ed542d4db69968d4d93757b051dd29b601b827ea0c7b608

### 运行结果：client

接收到服务器签名： a0f498c39a1e0ed29b22c66fc99032e2d005a64d0d6ee2ab1fc40a63d0b495e0b9b0623c870c6f69ed542d4db69968d4d93757b051dd29b601b827ea0c7b608

签名验证结果： True

