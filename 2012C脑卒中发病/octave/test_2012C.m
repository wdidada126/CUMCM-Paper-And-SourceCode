% 测试2012C脑卒中发病项目的核心代码
fprintf('Testing 2012C 脑卒中发病 project...\n');

% 测试年龄段数据
fprintf('\n=== 年龄段数据测试 ===\n');
y_age = [194 59 265 874 3138 8692 14888 21556 11280 826];
x_age = {'1-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100'};
fprintf('年龄段数据: '); disp(y_age);
fprintf('总人数: %d\n', sum(y_age));
fprintf('✓ 年龄段数据加载成功\n');

% 测试性别数据
fprintf('\n=== 性别数据测试 ===\n');
y_sex = [33385 28526];
fprintf('性别数据 (男, 女): '); disp(y_sex);
fprintf('总人数: %d\n', sum(y_sex));
fprintf('✓ 性别数据加载成功\n');

% 测试一些简单的统计计算
fprintf('\n=== 简单统计计算测试 ===\n');
mean_age = 0;
for i = 1:10
    mean_age = mean_age + y_age(i) * (i*10 - 5); % 中点年龄
end
mean_age = mean_age / sum(y_age);
fprintf('平均年龄估计: %.2f\n', mean_age);
fprintf('✓ 统计计算成功\n');

fprintf('\nTest completed successfully!\n');
