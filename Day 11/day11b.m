function maxSteps = day11b()
% Read input
fileID = fopen('day11Input.txt');
line = fgetl(fileID);
fclose(fileID);

% Get directions, and initialize variables
directions = strsplit(line, ',');
n = 0;
ne = 0;
nw = 0;
s = 0;
se = 0;
sw = 0;
maxSteps = 0;

for dir = directions
    % Update our variable count
    if strcmp(dir, 'n'), n = n+1;
    elseif strcmp(dir, 'ne'), ne = ne+1;
    elseif strcmp(dir, 'nw'), nw = nw+1;
    elseif strcmp(dir, 's'), s = s+1;
    elseif strcmp(dir, 'se'), se = se+1;
    elseif strcmp(dir, 'sw'), sw = sw+1;
    end
    
    % Cancle out whats possible to cancel out
    dir1 = n-s;
    dir2 = ne-sw;
    dir3 = nw-se;

    % Sort and find diff
    dirs = sort([dir1, dir2, dir3]);
    diff = dirs(2)-dirs(1);
    
    % Update maxSteps if needed
    steps = dirs(3) + diff + dirs(1);
    maxSteps = max(maxSteps, steps);
    
end

end