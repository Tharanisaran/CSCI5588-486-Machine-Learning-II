%L=[256 65 10]; % // Defining the layers: Total of 1 layers, # of nodes are 2, 2, 2, 2 respectively from input to output layer
%L=[256 66 86 10]; % // Defining the layers: Total of 2 layers,
L=[256 66 76 86 96 72 10]; % // Defining the layers: Total of 5 layers,
%L=[256 65 68 74 75 79 81 85 87 91 96 10];   % // Defining the layers: Total of 10 layers, 
alpha = 0.2;   % //usually alpha < 0, ranging from 0.1 to 1
target_mse=0.0001; % // one of the exit condition
Max_Epoch=2000;  % // one of the exit condition
epoch=0;       % // 1 epoch => One forward and backward sweep of the net for each training sample 
Epo=[];

%variables for storing train data results
train_Min_Error = Inf;
train_Min_Error_Epoch = -1;
train_mse = Inf;      % // initializing the Mean Squared Error with a very large value.
train_Err = [];
train_Accuracy = [];

%variables for storing test data results
test_Min_Error = Inf;
test_Min_Error_Epoch = -1;
test_mse = Inf;
test_Err = [];
test_Accuracy = [];