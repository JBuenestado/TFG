There should be four folders in this file. NN is used as short for Neural Network.

Feature and matrices are analogous, the first is used to train NN using 9 parameters (features of the density matrices) and the second to train NN using 32 parameters (whole density matrices that describe the entangled quantum state between two qubits. Inside those there is a notebook that runs the whole simulation, the input data used by the NN and the modules that are used in order to run the NN. Each folder should contain a README file that explain every folder and its files.

Results is the folder that contains the raw outputs of those two notebooks, organised in four folders depending of the objective of the experiment we wanted in a specific case. There have been more than a thousand simulations so there are files in accordance.

Plots contains the results folder expressed as graphics that can be easily understood. There are more graphics, depicting every case of the TW/TO possibility as well as of the negativity intervals.

The generate_quantum_states notebook is an updated and corrected version of the original used by J. Ureña in "Entanglement detection with classical deep neural networks" as it was incorrect in the generation of entangled and mixed states. It is used to generate the data in input_data inside the working folders. Separable density matrices were received from Daniel Manzano.

The operate_matrix is used to transform the generated or received data, using the rotation method for the CrossSetsTest experiment or the feature for the transformed density matrices. It is also used to check the negativity (and therefore the entanglement) of the test matrices, to check if the input data is correct.

The plots notebook was used to generate graphics into the Plots folder of the original Dara.

Transpose_numbers.py was used to make files for the previous notebook, using the output of the NN.