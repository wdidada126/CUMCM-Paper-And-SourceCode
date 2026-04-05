
clear;
clc;
fprintf('Testing Floyd algorithm...\n');

a = [
    0, 5, inf, 10;
    inf, 0, 3, inf;
    inf, inf, 0, 1;
    inf, inf, inf, 0
];

[D, R] = floyd(a);

fprintf('Distance matrix:\n');
disp(D);
fprintf('Path matrix:\n');
disp(R);
fprintf('Test completed successfully!\n');
