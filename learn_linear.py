#coding=utf-8
import numpy as np
import tensorflow as tf
num_point = 1000 
vectors_set = []
for i in xrange(num_point):
    x1 = np.random.normal(0.0,0.03)
    y1 = x1*0.1 +0.3+ np.random.normal(0.0,0.03)
    vectors_set.append([x1,y1])
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]
#print vectors_set
W = tf.Variable(tf.random_uniform([1],-1.0,1.0),name='W')
b = tf.Variable(tf.zeros([1]),name='b')
y = W*x_data+b
print y
loss = tf.reduce_mean(tf.square(y-y_data),name='loss')
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss,name='train')
sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

print "W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss)
for step in xrange(20):
    sess.run(train)
    # 输出训练好的W和b
    print "W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss)
writer = tf.train.SummaryWriter("./tmp", sess.graph)