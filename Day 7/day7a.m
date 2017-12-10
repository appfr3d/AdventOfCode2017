function startFunction = day7a() 
[parents, children] = readFunctions();

for p = parents
    isChild = false;

    for c = 1:length(children)
        % if the parent is in the list of children
        if strcmp(p, children{c})
            isChild = true;
        end
    end % children
    
    if ~isChild
        % could not find a child with its name
        % threrfore it is the starting function
        startFunction = p;
        return;
    end
    
end % parents
end % function

function [parents, children] = readFunctions()
file = fopen('day7Input.txt');
parents = {};
children = {};
p = 1;
c = 1;

if file
    while ~feof(file)
        line = fgetl(file);        
        [name, rest] = strtok(line);
        
        if contains(rest, '->')
            % Has subFunctions, aka is a parent
            parents{p} = name;
            p = p + 1;
            
            rawChildren = extractAfter(rest, '-> ');
            childs = strsplit(rawChildren,', ');
            
            % Add all subfunctions to the children-list
            for child = 1:length(childs)
                children{c} = childs(child);
                c = c + 1;
            end
            
        else
            % has no sumFunctions, aka is a child
            children{c} = name;
            c = c + 1;
        end
    end
    fclose(file);
end
end