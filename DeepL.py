__author__ = 'Bhavin.Parekh'
import tensorflow as tf
x = tf.constant(2)
y1=x+300
y2=x=66
y=y1+y2
sess = tf.Session("grpc://localhost:7777")
print(sess.run(y))


