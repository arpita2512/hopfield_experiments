##############
Introduction
##############

This is an implementation of the Hopfield Network. Pattern recovery experiments are performed using 
`MNIST <http://yann.lecun.com/exdb/mnist/>`_ dataset. Results are compared with Asynchronous approach of Hopfield and 
Self-Organising Map. 

++++++++++++++++++
Hopfield Network
++++++++++++++++++

Hopfield networks are recurrent neural networks that serve as autoassociative memory systems. This means that they can store 
patterns and retrieve them later from noisy input. 

For this implementation, the Hebb rule is used to train the network. This approach can be summarized as: 
**Neurons that fire together, wire together**. Training requires input vectors to be -1 or 1, so MNIST images are 
binarized while preprocessing.

For pattern recovery, the **synchronous approach** is used, which applies the :math:`sign(x)` function to the multiplication of the 
weight matrix by the input vector.

Limitations
*************

+++++++++++++++++++++
Self-Organising Map 
+++++++++++++++++++++
