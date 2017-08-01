#!/usr/bin/env python3
import tensorflow as tf
def varible_aummaries(var,scope):
    with tf.name_scope('summaries'):
        with tf.name_scope(scope):
            mean=tf.reduce_mean(var)
            tf.summary.scalar('mean',mean)
            with tf.name_scope('stddev'):
                stddev=tf.sqrt(tf.reduce_mean(var-mean))
            tf.summary.scalar('stddev',stddev)
            tf.summary.scalar('max',tf.reduce_max(var))
            tf.summary.scalar('min',tf.reduce_min(var))
            tf.summary.histogram('histogram',var)



def my_dense(scope,inputs,w_shape,layer="layer1",activation='relu',bn=False,is_training=None):
    initializer=tf.truncated_normal_initializer( mean=0.0, stddev=0.0001)
    with tf.variable_scope(scope+layer):

        weights=tf.get_variable('weight',w_shape,initializer=initializer)
        biases=tf.get_variable('biases',[w_shape[1]],initializer=tf.constant_initializer(0.0))
        if activation=='relu' :hidden=tf.nn.relu(tf.matmul(inputs,weights)+biases,name=layer)
        if activation=='tanh' :hidden=tf.nn.tanh(tf.matmul(inputs,weights)+biases,name=layer)
        if activation=='softplus': hidden= tf.nn.softplus(tf.matmul(inputs,weights)+biases,name=layer)
        if bn:hidden_bn=tf.layers.batch_normalization( hidden,
                training=is_training, name='hidden_bn')
        

        # s_layer1=tf.layers.batch_normalization(layer_1,training=self.is_training, name='s_layer_1')
        if not (scope.startswith('global')):
            varible_aummaries(weights,'weight')
            varible_aummaries(biases,'biases')
            varible_aummaries(hidden,layer)
            if bn :varible_aummaries(hidden_bn,'hidden_bn')

        if bn :return hidden_bn
        else:return hidden
