
% compute synaptic conductance
clc
clear
close all


a = input('enter file number for EPSC >>   ' , 's');
b = strcat(a,'.abf');
[x] = abfload(b);
x = x(:,:);
[nx ny] = size(x);
E = x(:,1:3:ny)*10^-12;
E_curr_inj = x(:,2:3:ny);
E_stim = x(:,3:3:ny)*-100;

sampling_frequency = 20000; % 20KHz
sampling_interval = 1/sampling_frequency; % step
L = length(x); % size of time series
tout = (0:1:L-1)*sampling_interval;

% focus on timespan
si = sampling_frequency;

time_start = 5.1;
time_end = 5.7;
E_focus = E(time_start*sampling_frequency:time_end*sampling_frequency,:); % changed from x to R_traces_norm
E_curr_inj = E(4.5*sampling_frequency:5.1*sampling_frequency,:);
E_stim_focus = E_stim(time_start*sampling_frequency:time_end*sampling_frequency,:);
T = tout(time_start*sampling_frequency:time_end*sampling_frequency);

a = input('enter file number for IPSC >>   ' , 's');
b = strcat(a,'.abf');
[x] = abfload(b);
x = x(:,:);
[nx ny] = size(x);
I = x(:,1:3:ny)*10^-12;
delay = -0.0;
time_start = 5.1+delay;
time_end = 5.7+delay;

I_stim = x(:,3:3:ny)-100; %offset simply for visibility
I_focus = I(time_start*sampling_frequency:time_end*sampling_frequency,:); % changed from x to R_traces_norm
I_stim_focus = I_stim(time_start*sampling_frequency:time_end*sampling_frequency,:);
I_curr_inj = I(4.5*sampling_frequency:5.1*sampling_frequency,:);


figure,plot(T,E_focus, 'r', T, E_stim_focus*10^-12, 'k', T, I_focus,'b')

%%%% for conductance analysis

I_current = mean(I_focus(:,1:end)');
I_curr_inj_T = mean(I_curr_inj');
E_current = mean(E_focus(:,1:end)');
E_curr_inj_T = mean(E_curr_inj');

T = T;
hold on

DE_curr = E_current - E_curr_inj_T; DE_curr = smooth(DE_curr,50);
DI_curr = I_current - I_curr_inj_T; DI_curr = smooth(DI_curr,50);

VrevE =  0.01;
VrevI = -0.08;

VholdEPSC = -0.075;
VholdIPSC = -0.02;

for i = 1:length(E_current)
    gtot(i) = (DI_curr(i)-DE_curr(i))/(VholdIPSC-VholdEPSC);
end

gtot = smooth(gtot, 20);


shift = DE_curr - gtot*VholdEPSC; shift = smooth(shift,20); % use points for EPSC to determine y = ax + b (b-shift);   
shift2 = DI_curr - gtot*VholdIPSC; shift2 = smooth(shift2,20); % use points for EPSC to determine y = ax + b (b-shift);   
Shift = (shift+shift2)/2;
Vrev = -Shift./gtot;


Ge =  gtot.*((Vrev-VrevI)/(VrevE-VrevI));
Gi =  gtot.*((Vrev-VrevE)/(VrevI-VrevE));
    
% figure,plot(T,Ge,T,Gi,'r', T, Ge+Gi,'k')

Gi = smooth(Gi,20);
Ge = smooth(Ge,20);
figure,plot(T,Ge,'r',T,Gi,'b', T, Ge+Gi,'k')

hold on
plot(T,E_stim_focus*10^-12,T,I_stim_focus*10^-12)
legend('E', 'I','total','stim')

%save Gi Gi
%save Ge Ge


