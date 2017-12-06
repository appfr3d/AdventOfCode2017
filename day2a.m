function checksum = day2a(m)

checksum = 0;

[r, c] = size(m);

% Loop thorugh the matrix
for row = 1:r
    
    % Reset max, min values
    mest = m(row,1);
    minst = m(row,1);
    for col = 1:c
        
        % Update our max, min values if needed
        if m(row,col) > mest
            mest = m(row,col);
        end
        
        if m(row,col) < minst
            minst = m(row,col);
        end
    end
    
    % Calculate diff and add to the sum
    diff = mest - minst;
    checksum = checksum + diff;
end

end