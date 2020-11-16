initialization
load_dataset
activation
while ((train_mse > target_mse) && (epoch < Max_Epoch))
    training
    train_Err = [train_Err mse];
    train_Accuracy = [train_Accuracy temp_Accuracy_Percentage];
    testing
    test_Err = [test_Err test_mse];
    test_Accuracy = [test_Accuracy temp_Accuracy_Percentage];
    Epo = [Epo epoch]; 
    epoch  = epoch+1
end % //while_end

train_Min_Error
train_Min_Error_Epoch  
test_Min_Error
test_Min_Error_Epoch

plotfigure

train_Err_Table = train_Err';
test_Err_Table = test_Err';

%//=============================================================================================================================
%//The NN Node and structure needs to be saved, i.e. save L
%     L
	
%// Now the predicted weight B with least error should be saved in a file to be loaded and to be used for test set/new prediction

%    for i=1:max(size(B))
%        B{i}
%    end 