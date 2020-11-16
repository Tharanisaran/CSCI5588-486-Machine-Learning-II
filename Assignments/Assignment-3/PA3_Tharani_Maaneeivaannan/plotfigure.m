subplot(2,1,1);
plot (Epo(1:200),train_Accuracy(1:200));
title('Classification Accuracy');
xlabel('Epoch');
ylabel('Accuracy');
hold on
plot (Epo(1:200), test_Accuracy(1:200));
subplot(2,1,2);
plot (Epo(1:200),train_Err(1:200));
title('MSE');
xlabel('Epoch');
ylabel('Error');
hold on
plot (Epo(1:200),test_Err(1:200));