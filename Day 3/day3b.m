function value = day3b()
% My puzzle input
input = 368078;

% Assumes that the matrix is is not bigger than 19x19
M = zeros(19,19);

% Start row and col, the middle of our matrix
r = 10; 
c = 10;
M(r,c) = 1; % initial value is 1;

n = 2;  % Which loop we are in

% Used to go around previous squares
turns = {[-1,0], [0,-1], [1,0], [0,1]};

% The value for the next position
val = 0;   
while val < input
    % Next loop starts here,
    % Start the loop, one position to the right from previous loop-end
    c = c + 1;
    for times = 1:4
        for i = 1:2*(n-1)
            % Dont update the position the first time
            if i ~= 1 || times ~= 1
                update = turns{times};
                r = r + update(1);
                c = c + update(2);
                
            end
            % Loop through neighburs and sum up
            val = 0;
            for vert = -1:1
                for horz = -1:1
                    val = val + M(r+vert, c+horz);
                end
            end
            
            % Give the position a value
            M(r,c) = val;
            if val > input
                % The first value larger than our input is found!
                value = val;
                return;
            end
        end
    end
    % Update loop count
    n = n + 1;
end
end
