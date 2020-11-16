% ////////// load datasets
load train.txt
train_X = train(1:end,2:end);
train_Y = train(1:end,1:1) == 1:10;

load test.txt
test_X = test(1:end,2:end);
test_Y = test(1:end,1:1) == 1:10;

[Nx,P] = size(train_X); % // Nx = # of sample in X, P= # of feature in X
% load Y.txt      % // Target Output
[Ny,K] = size(train_Y); % // Ny = # of target output in Y, K= # of class for K classes when K>=3 otherwise, K=2 in this binary case now

[TNx, TP] = size(test_X);
[TNy, TK] = size(test_Y);

% Optional: Since input and output are kept in different files, it is better to verify the loaded sample size/dimensions.
if Nx ~= Ny 
      error ('The input/output sample sizes do not match');
end
% Optional
if L(1) ~= P
       error ('The number of input nodes must be equal to the size of the features'); 
end 
% Optional
if L(end) ~= K
       error ('The number of output node should be equal to K');
end

% Optional: Since input and output are kept in different files, it is better to verify the loaded sample size/dimensions.
if TNx ~= TNy 
      error ('The input/output sample sizes do not match');
end
% Optional
if L(1) ~= TP
       error ('The number of input nodes must be equal to the size of the features'); 
end 
% Optional
if L(end) ~= TK
       error ('The number of output node should be equal to K');
end 