import tensorflow as tf
a = tf.Variable([1,2])
b = tf.constant([4,5])
add = tf.add(a,b)
sub = tf.subtract(a,b)

# 变量需要初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(add),sess.run(sub))
