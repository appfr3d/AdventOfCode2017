function sumCorrect = day4a()
% Read input file and iitialize variables
fileID = fopen('day4Input.txt');
sumCorrect = 0;
passfrases = [];
counter = 1;
while ~feof(fileID)
    line = fgetl(fileID);
    frase = strsplit(line, ' ');
    passfrases(counter).words = frase;
    counter = counter + 1;
end

% Loop through the database
for i = 1:length(passfrases)
    valid = 1;
    for n = 1:length(passfrases(i).words)-1
       for k = n+1:length(passfrases(i).words)
            if i~=k && strcmp(passfrases(i).words{n}, passfrases(i).words{k})
                % Current frase is invalid
                valid = 0;
                break;
            end
       end
       if valid == 0, break; end
    end
    % Sum is only increased if no equal words in the phrase is found
    sumCorrect = sumCorrect + valid;
end
end