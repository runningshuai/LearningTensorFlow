import tensorflow as tf
import numpy as np
# 一行两列
m1 = tf.constant([[3,4]])
print(np.shape(m1),type(m1))
# 两行一列
m2 = tf.constant([[2],[3]])
print(np.shape(m2),type(m2))
product = tf.matmul(m1,m2)
print(product)
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()# 手动关闭
# 会自动关闭图
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
