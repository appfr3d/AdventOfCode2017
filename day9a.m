function sum = day9a()
% Read puzzle input form a file
fileID = fopen('day9Input.txt');
string = fgetl(fileID);
fclose(fileID);

% Initialize variables
sum = 0;
groups = 0;
isInGarbage = false;
skipNext = false;

for i = 1:length(string)
    if ~skipNext
        if isInGarbage
            if string(i) == '!'
                skipNext = true; % skip the next character
            elseif string(i) == '>'
                isInGarbage = false;
            end
        else
            % Only add points when opening groups
            if string(i) == '{'
                groups = groups + 1;
                sum = sum + groups;
            elseif string(i) == '}'
                groups = groups - 1;
            elseif string(i) == '<'
                isInGarbage = true;
            end
        end
    else
        skipNext = false;
    end
end
end