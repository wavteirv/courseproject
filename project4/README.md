# *Project4: do your best to optimize SM3 implementation (software)
减少不必要的重复计算：在消息扩展函数中，原先的代码是将512bit的消息扩展为132个字（w1共68个字，w2共64个字），但是在后面的压缩函数中，实际上只使用了w1和w2的前64个字，因此我将消息扩展的部分缩减为64个字，减少了不必要的计算。

简化代码逻辑：优化了填充消息的函数，使得代码更加简洁清晰。

使用secrets库生成随机字节串：为了确保随机性和安全性，使用Python的secrets库来生成随机字节串，而不是使用random库。

这些优化措施主要是为了提高代码的效率和可读性，让代码更加简洁和易于理解。

原代码：

<img width="518" alt="y" src="https://github.com/wavteirv/sdu-project-group78/assets/102475494/0ec7cbcc-e1a3-4b7d-b77e-fcc5df4bb260">

优化后：

<img width="517" alt="1" src="https://github.com/wavteirv/sdu-project-group78/assets/102475494/f00f471e-b945-4983-8688-cf867a3d6c80">

