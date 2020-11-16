test_CSqErr = 0; 
temp_Accuracy = [];

for j=1:size(test_X,1) 		    % for loop #1	
    test_Z{1} = [test_X(j,:) 1]';   % Load Inputs with bias=1
    %%% //(Note: desired output here) .....   	  % Load Corresponding Desired or Target output
    TYk   = test_Y(j,:);
    % // forward propagation 
    % //----------------------
    for i=1:length(L)-1
        T{i+1} = B{i}' * test_Z{i};
        if (i+1)<length(L)
            test_Z{i+1}=[(1./(1+exp(-T{i+1}))) ;1];
        else  
            test_Z{i+1}=(1./(1+exp(-T{i+1}))); 
        end 
    end  % //end of forward propagation 
    [max_value,digit_class] = max(test_Z{end});
    Identity_Y = eye(TK,TK);
    temp_Accuracy = [temp_Accuracy isequal(TYk,Identity_Y(digit_class,:))];
end  
temp_Accuracy_Percentage = sum(temp_Accuracy)/length(temp_Accuracy);
test_CSqErr = test_CSqErr+sum(sum(((test_Y_TRANS-test_Z{end}).^2),1));   
test_CSqErr = test_CSqErr/L(end);  % Normalizing the Error based on the number of output Nodes

test_CSqErr = (test_CSqErr) /(Nx);        % //Average error of N sample after an epoch 
test_mse = test_CSqErr;

if test_mse < test_Min_Error
    test_Min_Error = test_mse;
    test_Min_Error_Epoch = epoch;
end
 

