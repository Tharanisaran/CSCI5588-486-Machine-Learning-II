CSqErr = 0; 		
% // forward propagation
for i=1:length(L)-1
     T{i+1} = B{i}' * Z{i};
     if (i+1)<length(L)
       Z{i+1}=[(1./(1+exp(-T{i+1}))); ones(Nx,1)'];
     else  
       Z{i+1}=(1./(1+exp(-T{i+1}))); 
     end 
end  

CSqErr = CSqErr+sum(sum(((Y_TRANS-Z{end}).^2),1));   
CSqErr = CSqErr/L(end);  % Normalizing the Error based on the number of output Nodes
Z_TRANS = Z{end}';

temp_Accuracy = [];
for i=1:size(train_Y,1)
    Train_ZK = Z_TRANS(i,:);
    Train_YK = train_Y(i,:);
    [train_value, digit_class] = max(Train_ZK);
    Identity_Y = eye(K,K);
    temp_Accuracy = [temp_Accuracy isequal(Train_YK,Identity_Y(digit_class,:))];
end
temp_Accuracy_Percentage = sum(temp_Accuracy)/length(temp_Accuracy);
% // Compute error term delta 'd' for each of the node except the input unit
% // -----------------------------------------------------------------------
d{end} = (Z{end}-Y_TRANS).*Z{end}.*(1-Z{end}); % // delta error term for the output layer.

 for i=length(L)-1:-1:2
     W=Z{i}(1:end-1,:).*(1-Z{i}(1:end-1,:)); D= d{i+1}';
     for m = 1:Nx                             
         d{i}(:,m)=W(:,m).*sum((D(m,:).*B{i}(1:end-1,:)),2);  % // sum(A, 2) => row wise sum of matrix A
     end
 end              

% // Now we will update the parameters/weights
for i=1:length(L)-1
    W = Z{i}(1:end-1,:);   V1 = zeros(L(i),L(i+1));   V2 = zeros(1,L(i+1));    D = d{i+1}';
    for m = 1:Nx
        V1 = V1 + (W(:,m)*D(m,:));   V2 = V2 + D(m,:);     
    end
    B{i}(1:end-1,:)=B{i}(1:end-1,:)-(alpha/Nx).*V1;             
    B{i}(end,:) = B{i}(end,:)-(alpha/Nx).*V2;  			
end 

CSqErr = (CSqErr) /(Nx);        % //Average error of N sample after an epoch 
mse = CSqErr;

if mse < train_Min_Error
    train_Min_Error = mse;
    train_Min_Error_Epoch = epoch;
end
% end %//while end
