B=cell(length(L)-1,1);  % forming the number of Beta/weight matrix needed in between the layers

for i=1:length(L)-1     % Assign uniform random values in [-0.7, 0.7] 
      B{i} = [1.4.*rand(L(i)+1,L(i+1))-0.7];	
end 
%Let us allocate places for Term, T 
T = cell(length(L),1);
for i=1:length(L)
	T{i} = ones (L(i),1);
end

%Let us allocate places for activation, i.e., Z for train data 
Z = cell(length(L),1);
for i=1:length(L)-1
	Z{i} = zeros(L(i)+1,1); % it does not matter how do we initialize (with '0' or '1', or whatever,) this is fine!
end
Z{end} = zeros(L(end),1);  % at the final layer there is no Bias unit

%Let us allocate places for activation, i.e., Z for test data 
test_Z = cell(length(L),1);
for i=1:length(L)-1
	test_Z{i} = zeros (L(i)+1,1); % it does not matter how do we initialize (with '0' or '1', or whatever,) this is fine!
end
test_Z{end} = zeros(L(end),1); 

%Let us allocate places for error term delta, d
d = cell(length(L),1);
for i=1:length(L)
	d{i} = zeros(L(i),1);
end
			
Z{1} = [train_X ones(Nx, 1)]';  
Y_TRANS = train_Y';   	   

% test_Z{1} = [test_X ones(TNx,1)]';
test_Y_TRANS = test_Y';