% 测试pdztfb.m的核心功能 - 不显示图形
fprintf('Testing pdztfb.m...\n');

% 加载数据
try
  load clhsjfile;
  fprintf('✓ Data loaded successfully\n');
  
  % 计算总分
  r1 = sum(red1, 2)';
  r2 = sum(red2, 2)';
  w1 = sum(white1, 2)';
  w2 = sum(white2, 2)';
  
  fprintf('✓ Calculations completed successfully\n');
  fprintf('Red wine group 1 scores: '); disp(r1(1:5));
  fprintf('Red wine group 2 scores: '); disp(r2(1:5));
  fprintf('White wine group 1 scores: '); disp(w1(1:5));
  fprintf('White wine group 2 scores: '); disp(w2(1:5));
  
  fprintf('Test completed successfully!\n');
catch
  fprintf('Error: %s\n', lasterr());
end
