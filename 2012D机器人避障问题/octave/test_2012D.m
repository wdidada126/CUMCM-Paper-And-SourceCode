% 测试2012D机器人避障问题项目的核心代码
fprintf('Testing 2012D 机器人避障问题 project...\n');

% 测试FLOYD1函数
fprintf('\n=== 测试FLOYD1函数 ===\n');
% 创建一个简单的测试图
w = [
    0, 5, inf, 10;
    inf, 0, 3, inf;
    inf, inf, 0, 1;
    inf, inf, inf, 0
];
s = 1;
t = 4;
fprintf('输入邻接矩阵:\n');
disp(w);
try
    [L, R] = FLOYD1(w, s, t);
    fprintf('✓ FLOYD1函数调用成功\n');
    fprintf('路径长度: '); disp(L);
    fprintf('路径节点: '); disp(R);
catch
    fprintf('✗ FLOYD1函数调用失败: %s\n', lasterr());
end

% 测试huchang函数
fprintf('\n=== 测试huchang函数 ===\n');
A = [0, 0];
B = [2, 2];
C = [1, 1];
r = 1;
fprintf('测试参数: A=[%d,%d], B=[%d,%d], C=[%d,%d], r=%d\n', A(1), A(2), B(1), B(2), C(1), C(2), r);
try
    z = huchang(A, B, C, r);
    fprintf('✓ huchang函数调用成功\n');
    fprintf('弧长: %.4f\n', z);
catch
    fprintf('✗ huchang函数调用失败: %s\n', lasterr());
end

fprintf('\nTest completed!\n');
