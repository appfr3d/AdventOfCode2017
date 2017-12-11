function steps = day11a()
% Read input
fileID = fopen('day11Input.txt');
line = fgetl(fileID);
fclose(fileID);

% Get number of each direction
directions = strsplit(line, ',');
n = sum(strcmp(directions,'n'));
ne = sum(strcmp(directions,'ne'));
nw = sum(strcmp(directions,'nw'));
s = sum(strcmp(directions,'s'));
se = sum(strcmp(directions,'se'));
sw = sum(strcmp(directions,'sw'));

% Cancle out whats possible to cancel out
dir1 = n-s;
dir2 = ne-sw;
dir3 = nw-se;

% Sort
dirs = sort([dir1, dir2, dir3]);
diff = dirs(2)-dirs(1);

% Add the two largest
steps = dirs(3) + diff + dirs(1);
end
