from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# MNIST 손글씨 데이터 다운로드
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

'''
수집데이터 포맷
# 55,000개의 학습데이터(mnist.train), 10,000개의 테스트 데이터(mnist.text), 5,000개의 검증데이터(mnist.validation)으로 나뉨
# 학습 이미지: mnist.train.images, 학습 라벨: mnist.train.labels
# 종속변수: ys(라벨), 독립변수: xs(이미지)
# 이미지는 28x28 = 784개의 벡터
'''

# 변수 설정
x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 활성화 함수(softmax)
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 손실함수(cross entropy) 설정
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# 학습비율 0.5로 경사하강법 적용
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()

# 학습 전 변수 초기화
tf.global_variables_initializer().run()

# 학습(1000번)
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# 결과 예측
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

# 결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))