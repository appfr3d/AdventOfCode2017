function sum = day9b()
% Read puzzle input form a file
fileID = fopen('day9Input.txt');
string = fgetl(fileID);
fclose(fileID);

% Initialize variables
sum = 0;
isInGarbage = false;
skipNext = false;

for i = 1:length(string)
    if ~skipNext
        if isInGarbage
            if string(i) == '!'
                skipNext = true; % skip the next character
            elseif string(i) == '>'
                isInGarbage = false;
            else
                sum = sum + 1;
            end
        elseif string(i) == '<'
            isInGarbage = true;
        end
    else
        skipNext = false;
    end
end
end