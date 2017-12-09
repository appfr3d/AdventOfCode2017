function day7b()

funcs = readFunctions();

% Use task a) to find the name og the starting function
startFuncName = day7a();
getWeight(startFuncName, funcs);

end

function func = findFuncWithName(name, funcs)
for i = funcs
    if strcmp(name, i.name)
        func = i;
        return;
    end
end
end

function [weight, done] = getWeight(funcName, funcs)
done = false;
func = findFuncWithName(funcName, funcs);
weight = func.weight;
childWeights = zeros(1, length(func.children));
for c = 1:length(func.children)
    % Gå gjennom alle og finn "the child"
    [cW, done] = getWeight(func.children(c), funcs);
    if done
        return;
    end
    childWeights(c) = cW;
    weight = weight + childWeights(c);
end

if childWeights >= 2
    for n = 2:length(childWeights)-1
        if childWeights(1) ~= childWeights(n)
            disp('HER ER EN FEIL');
            checkError(func, childWeights);
            done = true;
            continue;
        end
    end
    
end
end

% found =
function checkError(parentFunc, childWeights)
n = 1;
for c = parentFunc.children
    fprintf('child: %s, weight: %i\n',c, childWeights(n));
    n = n + 1;
end
end

% func trenger:
% weight        (int)
% children      (list with funcs)


% instead of rewriting the a) task, read the file again
function funcs = readFunctions()
file = fopen('day7Input.txt');

a = 1;


if file
    while ~feof(file)
        line = fgetl(file);        
        [name, rest] = strtok(line);
        
        funcs(a).name = name;
        
        if contains(rest, '->')
            % Has subFunctions, aka is a parent
            rawChildren = extractAfter(rest, '-> ');
            childs = strsplit(rawChildren,', ');
            
            % Add all subfunctions to the children-list
            for child = 1:length(childs)
                funcs(a).children(child) = childs(child);
            end
            
        else
            % has no sumFunctions, aka is a child
            funcs(a).children = [];
        end
        
        % add the current weight
        funcs(a).weight = str2double(extractBetween(rest, '(', ')'));

        a = a + 1;
        
    end
    fclose(file);
end

end