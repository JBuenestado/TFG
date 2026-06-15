This folder contains the data obtained of running the neural networks with the updated feature parameters. Each folder contains a different topology of the NN;
NN1 - 16:8:1
NN2 - 9:8:1
NN3 - 9:6:1
NN4 - 9:4:1
NN5 - 9:2:1

Inside each one there are folders labeled X_Y, where X & Y are M (Mixed) or P (Pure), X means the states the NN was trained on, Y the states the NN was tested on.

Inside each folder there are files labelled XY_0N_ZT, where X, Y, Z, T can be also M (Mixed) or P (Pure). X means the separable state the NN was trained on, Y the entangled state the NN was trained on, Z the separable states it was tested on and T the entangled states it was tested on.
This was done in case we decided to test on training (or testing) the network with different type of states for entangled and separable.

0N means the interval the matrix was trained on, N being from 0 to 4, being N the beginning of the interval, always in 0.1 intervals, so for example MM_02_PP means the NN was trained on Mixed (Separable and Entangled), with the entangled Negativity in the interval [0.2,0.3] and tested on Pure states (Separable and Entangled)

Each file contains the byproduct of the training of the NN with the said states and has been tested on all negativities of the ZT type of states.
