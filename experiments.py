# -*- coding: utf-8 -*-
"""
CS 231N Project: 3D CNN with Optical Flow Regularization
Experiments
Created on Sun Mar  1 14:47:40 2015

@author: Kevin Chavez
"""
from src.convnet3d.cnn3d import ConvNet3D
from src.convnet3d.solver import Solver

video_shape = (16,240,320)
batch_size = 4
seed = 1234

# Baseline A: Small CNN
smallnet = ConvNet3D("small-net",video_shape,batch_size,seed=seed)
smallnet.add_train_data("data/traindb.lmdb")
smallnet.add_val_data("data/valdb.lmdb")
smallnet.add_conv_layer("conv1",(5,7,7),8)
smallnet.add_pool_layer("pool1",(2,2,2))
smallnet.add_conv_layer("conv2",(3,3,3),16)
smallnet.add_pool_layer("pool2",(2,2,2))
smallnet.add_conv_layer("conv3",(3,3,3),16)
smallnet.add_pool_layer("pool3",(2,2,2))
smallnet.add_conv_layer("conv4",(3,3,3),16)
smallnet.add_pool_layer("pool4",(2,2,2))
smallnet.add_fc_layer("fc1",128,0.5)
smallnet.add_softmax_layer("softmax",101)

reg = 5e-3
reg_params = {
    "conv1_W": reg,
    "conv2_W": reg,
    "conv3_W": reg,
    "conv4_W": reg,
    "fc1_W": reg,
    "softmax_W": reg}

lr_params = {
    "rate": 1e-9,
    "decay": 0.95,
    "step": 2000}

rmsprop_decay = 0.99
snapshot_params = {
    "dir": "models/smallnet",
    "rate": 500}

solver = Solver(smallnet,reg_params,lr_params,rmsprop_decay)
solver.train(20000,snapshot_params,validate_rate=500,loss_rate=1)
