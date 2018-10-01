import tensorflow as tf

# x1_data =[73.,93.,89.,96.,73.]
# x2_data = [80.,88.,91.,98.,66.]
# x3_data = [75.,93.,90.,100.,70.]
#Matrix used
x_data = [[73.,80.,75.],[93.,88.,93.],[89.,91.,90.],[96.,98.,100.],[73.,66.,70.]]
y_data = [[152.],[185.],[180.],[196.],[142.]]
data=[[100,100,100]]
#placeholders for a tensor that will be always fed.
# x1 = tf.placeholder(tf.float32)
# x2 = tf.placeholder(tf.float32)
# x3 = tf.placeholder(tf.float32)

X=tf.placeholder(tf.float32, shape=[None,3])
Y=tf.placeholder(tf.float32, shape=[None,1])

# w1 = tf.Variable(tf.random_normal([1]),name='weight1')
# w2 = tf.Variable(tf.random_normal([1]),name='weight2')
# w3 = tf.Variable(tf.random_normal([1]),name='weight3')
W=tf.Variable(tf.random_normal([3, 1]), name='weight')
b=tf.Variable(tf.random_normal([1]), name='bias')

# hypothesis = x1*w1+x2*w2+x3*w3
# Matrix곱 사용
hypothesis = tf.matmul(X, W) + b
#cost/loss function cost최소화
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#Minimize. Need a very small learning rate for this data set
a = tf.Variable(1e-5)
optimizer =tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(5001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction: ", hy_val)

print('my score predict: ', sess.run(hypothesis, feed_dict={X: data}))