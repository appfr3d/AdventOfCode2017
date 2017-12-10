function ret = day3a(number)
%{
how many numbers are in the loop:
1
8
16
22

x1 = 1  % matlab starts matrixes at 1
xn+1 =  (4*(2n-3)) + 4

66666666666
65555555556
65444444456
65433333456
65432223456
65432123456
65432223456
65433333456
65444444456
65555555556
66666666666

1*1, 2*8, 3*8 osv
%}


%{
the cost of a position in the loop:
10 9 8 7 6 5 6 7 8 9 10
 9 8 7 6 5 4 5 6 7 8 9
 8 7 6 5 4 3 4 5 6 7 8
 7 6 5 4 3 2 3 4 5 6 7
 6 5 4 3 2 1 2 3 4 5 6
 5 4 3 2 1 0 1 2 3 4 5
 6 5 4 3 2 1 2 3 4 5 6
 7 6 5 4 3 2 3 4 5 6 7
 8 7 6 5 4 3 4 5 6 7 8
 9 8 7 6 5 4 5 6 7 8 9
10 9 8 7 6 5 6 7 8 9 10

n=5 gir
56789109876

%}

loopN = 1;
lastMax = 1;
loopMax = 1;

% Start by finding wich loop the number is in
while (number > loopMax)
    
    
    % xn+1 = 4(2n-3)+4
    lastMax = loopMax;                  % 9
    % loopMax = 4*(2*loopN - 1) + 4;
    loopMax = loopMax + 4*2*loopN;      % 9 + 16 = 25
    
    % update for next loop
    loopN = loopN + 1;                  % 3
end

% Update loopN afte we jump uot of the loop
loopN = loopN - 1;

% we now know what loop our number is in
disp('er i loop nummer: ')
disp(loopN);


% the numbers in our "loop"/square
loopNumbers = lastMax+1:loopMax;

% set the last number in the front of the list, so it starts in the bottom
% left corner of the square
loopNumbers = [loopMax, loopNumbers(1,1:end-1)];


len = loopN*2;
val = len; % Start value (the corners)
values = zeros(1, loopN*2*4);
for i = 0:loopN
    
    values(1+i) = val;
    if i >= 1
        values((4*len)+1-i) = val;
    end
    
    values(len+1+i) = val;
    values(len+1-i) = val;
    
    values((2*len)+1+i) = val;
    values((2*len)+1-i) = val;
    
    values((3*len)+1+i) = val;
    values((3*len)+1-i) = val;
    
    val = val-1;
end

fprintf('%6.0i ',loopNumbers);
fprintf('\nså:\n');
fprintf('%6.0i ',values);
fprintf('\n');

[~, index] = find(loopNumbers==number);
ret = values(index);

end