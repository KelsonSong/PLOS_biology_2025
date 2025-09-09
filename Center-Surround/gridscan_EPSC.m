clear
close all

a = input('enter file number >>   ' , 's');
b = strcat(a,'.abf');

x = abfload(b);
stim = x(:,3,:);
current = x(:,1,:);
stim_y = reshape(stim, [4040400 1]);
current_y = reshape(current, [4040400 1]);
tout = (0:4040399)*(1/20000);

Ft_current_y = smooth(current_y,20);

dt_stim = 20196;
load stim_point2 

% figure, plot(tout,current_y,'k')
for i = 1:100
    t_int_current(i,1:20001) = stim_tout(i):1:stim_tout(i)+20000;
    current_int(i,:) = Ft_current_y(t_int_current(i,:));
    h = hist(current_int(i,:)); h_max = max(h); 
    baseline(i) = mean(Ft_current_y((stim_tout(i)-1000):stim_tout(i)));
    EPSC(i,:) = (( baseline(i)-current_int(i,:)));
    MAX_EPSC(i) = (max(EPSC(i,:)));    
end

MAX_EPSC = abs(MAX_EPSC);
NORM_EPSC = (MAX_EPSC)./max((MAX_EPSC)); 
% amp_norm_index = 0.05; % pA 


 amp_norm_index = input('normalised threshold 0.15 >>   ');
% amp_norm_index = 50; % pA 
% activation_code = find(NORM_EPSC > amp_norm_index);
activation_code = find((NORM_EPSC) > amp_norm_index );

figure, plot(tout,current_y,'k',tout, stim_y, 'r')
hold on, plot(tout(stim_tout(activation_code)),30,'rs')

N_cells = length(activation_code);

load MAP_GRIDSCAN
MAP_GRIDSCAN = MAP_GRIDSCAN';
RE_MAP = reshape(MAP_GRIDSCAN',1,100);


active_cell = RE_MAP(activation_code);


% active_cell = sort(active_cell,'descend');
active = zeros(100,1);
for i = 1:length(active_cell)
    active(active_cell(i)) = 1;
end

k = 0;
for i = 1:10
    for j = 1:10
        k = k+1;
        ACT(i,j) = active(k);
    end
end

SURROUND = 1-ACT;

THRES = num2str(amp_norm_index);
ss1 = 'traces';
s2 = '.png';
F1 = strcat(a,ss1,THRES,s2);
H1 = figure;
plot(tout,current_y,'k',tout, stim_y+50, 'b')
hold on, plot(tout(stim_tout(activation_code)),30,'rs')
saveas(H1,F1)



s1 = 'maps';
s2 = '.png';
F2 = strcat(a,s1,THRES,s2);
H2 = figure;
subplot(121)
imagesc(ACT), axis square
title('ON STIMULATION')
subplot(122)
imagesc(SURROUND), axis square
title('OFF STIMULATION')
saveas(H2,F2)
% I = mat2gray(ACT);
% figure,imshow(I)
% J = mat2gray(SURROUND); %surround negative
% figure, imshow(J)

sss1 = '_ON_OFF.txt';
TXT1 = strcat(a,sss1);

fileID = fopen(TXT1,'w');
formatSpec = 'MightexVector1.0';
formatSpec1 = 'Grid';
formatSpec2 = 'Bin';
activate = 1;
fprintf(fileID, formatSpec);
fprintf(fileID,'\n');
fprintf(fileID, formatSpec1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');

%%%%%% SURROUND
%%%%% STIM 1
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(10,:), s);fprintf(fileID,'\n');


%%%%%%repeat ACT
%%%%% STIM 1
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(10,:), s);fprintf(fileID,'\n');

fclose(fileID);


%%%%%%%%%%%% TEMPLATE ONLY ON-EXCITATION

sss2 = '_ON.txt';
TXT2 = strcat(a,sss2);


fileID = fopen(TXT2,'w');
formatSpec = 'MightexVector1.0';
formatSpec1 = 'Grid';
formatSpec2 = 'Bin';
activate = 1;
fprintf(fileID, formatSpec);
fprintf(fileID,'\n');
fprintf(fileID, formatSpec1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');

%%%%%%repeat ACT
%%%%% STIM 1
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(10,:), s);fprintf(fileID,'\n');

%%%%% STIM 2
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', ACT(10,:), s);fprintf(fileID,'\n');



fclose(fileID);

%%%%%%%%%%%% TEMPLATE ONLY OFF-EXCITATION

sss3 = '_OFF.txt';
TXT3 = strcat(a,sss3);


fileID = fopen(TXT3,'w');
formatSpec = 'MightexVector1.0';
formatSpec1 = 'Grid';
formatSpec2 = 'Bin';
activate = 1;
fprintf(fileID, formatSpec);
fprintf(fileID,'\n');
fprintf(fileID, formatSpec1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 1);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');
fprintf(fileID,'%d', 10);
fprintf(fileID,'\n');

%%%%%%repeat ACT
%%%%% STIM 1
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(10,:), s);fprintf(fileID,'\n');

%%%%% STIM 2
fprintf(fileID, formatSpec2);
s = ';';
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(1,:), s); fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(2,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(3,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(4,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(5,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(6,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(7,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(8,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(9,:), s);fprintf(fileID,'\n');
fprintf(fileID,' %d %d %d %d %d %d %d %d %d %d%s', SURROUND(10,:), s);fprintf(fileID,'\n');



fclose(fileID);

