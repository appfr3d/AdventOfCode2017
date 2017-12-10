function dividesum = day2b(m)

dividesum = 0;

[r, c] = size(m);


% Loop thorugh the matrix
for row = 1:r
    
    % Reset the sum
    sum = 0;
    
    for col = 1:c
        % For each element in column, check if the numbers after are
        % divisible or not, all numbers before are already checked
        for next = col+1:c
            
            % If division has a rest of zero, we are done with this row
            if mod(m(row, col), m(row, next)) == 0
                sum = m(row, col) / m(row, next);
            elseif mod(m(row, next), m(row, col)) == 0
                sum = m(row, next) / m(row, col);
            end
        end
    end
    
    % Update out dividesum
    dividesum = dividesum + sum;
end

end