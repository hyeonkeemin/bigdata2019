import tensorflow as tf

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[2,2,2],[2,2,2],[2,2,2]]

t_mat1 = tf.constant(mat1)
t_mat2 = tf.constant(mat2)

result = tf.matmul(t_mat1, t_mat2)

with tf.Session() as sess:
    _result = sess.run(result)
    print(_result)