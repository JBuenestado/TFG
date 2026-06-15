This folder contains the plots of outputs of the neural network program, organised in different sections. The raw data is in "results" folder. The following test is the README from that folder that explains everyfolder



The results in CrossSetsTest are the results of training and testing the network with Set 1 and testing with Set 1, Set 2 and Set 3 (one by one). Set 1 is based on generated data and received from Daniel Manzano. Set 2 is the same but transformed by Euler's rotations with operate_matrix notebook with the same angles for all Set 1. Set 3 the same but with different angles for every matrix. Th

NN contains the data obtained to compare the results from running different neural networks. In its README file there is detailed information.

BCE contains the results of the running of neural networks, with the NN being the same as in the previous folder. In its README file there is detailed information.

The results in PureMixed_training are the results of training the network with Set 1 and testing with Set 1, Set 2 and Set 3 (all at the same time). The two letters indicate if trained with Mixed (M) or Pure (P), the first means the separable state and the second the entangled state. The numbers indicate the negativity interval it was trained with, 0X in [0.X,0.X+1] so if its 01 it means is the interval [0.1,0.2].  The final letter indicates if the separable state in the test set was Mixed or Pure. Cross tested states (tested on separable pure and entangled mixed or viceversa) was studied but not included in final results.