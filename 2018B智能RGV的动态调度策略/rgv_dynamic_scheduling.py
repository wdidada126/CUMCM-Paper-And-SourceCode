import numpy as np
import matplotlib.pyplot as plt

def rgv_dynamic_scheduling():
    """
    智能RGV的动态调度策略问题
    基于MATLAB代码的Python实现
    """
    print("Problem: RGV Dynamic Scheduling Strategy")
    print("=" * 60)
    
    # 问题1：RGV调度优化
    print("\nProblem 1: RGV Scheduling Optimization")
    print("-" * 40)
    
    # 定义参数
    num_cnc = 8  # CNC数量
    num_moves = 100  # RGV移动次数
    
    # 时间参数
    exchang_time_odd = 28  # 奇数CNC上料时间
    exchang_time_even = 31  # 偶数CNC上料时间
    clear_time = 25  # 清洗时间
    time_for_one_step = 560  # 加工时间
    mov_1_step_t = 20  # 移动1步时间
    mov_2_step_t = 33  # 移动2步时间
    mov_3_step_t = 46  # 移动3步时间
    
    # 目标值
    fitn = 330  # 目标完成数量
    
    # 模拟RGV移动序列
    def fitness(RGV_position, N):
        """
        计算适应度函数
        RGV_position: RGV移动序列
        N: 移动次数
        """
        curent_time = 0
        CNC_finish_time = np.zeros(num_cnc)
        finished_num = 0
        load_time = np.zeros(N)
        unload_time = np.zeros(N)
        CNC_doing = np.zeros(num_cnc, dtype=int)
        
        for i in range(N):
            load_time[i] = curent_time
            
            cnc_idx = RGV_position[i] - 1  # 转换为0-based索引
            
            if cnc_idx % 2 == 0:
                curent_time += exchang_time_even
            else:
                curent_time += exchang_time_odd
            
            if CNC_doing[cnc_idx] > 0:
                unload_time[CNC_doing[cnc_idx] - 1] = load_time[i]
                finished_num += 1
                curent_time += clear_time
            
            CNC_finish_time[cnc_idx] = curent_time + time_for_one_step
            CNC_doing[cnc_idx] = i + 1
            
            if i < N - 1:
                next_cnc_idx = RGV_position[i + 1] - 1
                if curent_time < CNC_finish_time[next_cnc_idx]:
                    curent_time = CNC_finish_time[next_cnc_idx]
                
                # 计算移动时间
                current_row = cnc_idx // 2
                next_row = next_cnc_idx // 2
                row_diff = abs(next_row - current_row)
                
                if row_diff > 2:
                    curent_time += mov_3_step_t
                elif row_diff > 1:
                    curent_time += mov_2_step_t
                elif row_diff > 0:
                    curent_time += mov_1_step_t
            
            if curent_time > 28800:  # 超过8小时
                return finished_num - fitn, i
        
        return finished_num - fitn, N
    
    # 生成随机调度序列
    def generate_random_schedule(N):
        """
        生成随机调度序列
        """
        schedule = np.random.randint(1, num_cnc + 1, N)
        return schedule
    
    # 测试多个调度序列
    num_tests = 10
    best_fitness = -float('inf')
    best_schedule = None
    
    for test in range(num_tests):
        schedule = generate_random_schedule(num_moves)
        fitness_value, moves_used = fitness(schedule, num_moves)
        
        if fitness_value > best_fitness:
            best_fitness = fitness_value
            best_schedule = schedule
    
    print(f"Best fitness value: {best_fitness}")
    print(f"Finished products: {best_fitness + fitn}")
    
    # 问题2：不同参数下的性能分析
    print("\nProblem 2: Performance Analysis with Different Parameters")
    print("-" * 40)
    
    # 定义不同的参数组合
    parameter_sets = [
        {
            'exchang_time_odd': 28,
            'exchang_time_even': 31,
            'clear_time': 25,
            'time_for_one_step': 560,
            'mov_1_step_t': 20,
            'mov_2_step_t': 33,
            'mov_3_step_t': 46,
            'fitn': 330,
            'name': 'Parameter Set 1'
        },
        {
            'exchang_time_odd': 30,
            'exchang_time_even': 35,
            'clear_time': 30,
            'time_for_one_step': 580,
            'mov_1_step_t': 23,
            'mov_2_step_t': 41,
            'mov_3_step_t': 59,
            'fitn': 310,
            'name': 'Parameter Set 2'
        },
        {
            'exchang_time_odd': 27,
            'exchang_time_even': 32,
            'clear_time': 25,
            'time_for_one_step': 545,
            'mov_1_step_t': 18,
            'mov_2_step_t': 32,
            'mov_3_step_t': 46,
            'fitn': 340,
            'name': 'Parameter Set 3'
        }
    ]
    
    results = []
    
    for params in parameter_sets:
        # 使用参数更新全局变量
        exchang_time_odd = params['exchang_time_odd']
        exchang_time_even = params['exchang_time_even']
        clear_time = params['clear_time']
        time_for_one_step = params['time_for_one_step']
        mov_1_step_t = params['mov_1_step_t']
        mov_2_step_t = params['mov_2_step_t']
        mov_3_step_t = params['mov_3_step_t']
        fitn = params['fitn']
        
        # 测试多个调度序列
        best_fitness_param = -float('inf')
        for test in range(num_tests):
            schedule = generate_random_schedule(num_moves)
            fitness_value, moves_used = fitness(schedule, num_moves)
            
            if fitness_value > best_fitness_param:
                best_fitness_param = fitness_value
        
        results.append({
            'name': params['name'],
            'fitness': best_fitness_param,
            'finished': best_fitness_param + fitn
        })
        
        print(f"{params['name']}: Fitness = {best_fitness_param}, Finished = {best_fitness_param + fitn}")
    
    # 绘制结果比较图
    plt.figure(figsize=(10, 6))
    names = [r['name'] for r in results]
    finished = [r['finished'] for r in results]
    
    plt.bar(names, finished, color='b', alpha=0.7)
    plt.xlabel('Parameter Set')
    plt.ylabel('Finished Products')
    plt.title('RGV Performance with Different Parameters')
    plt.grid(True)
    plt.savefig('rgv_performance_comparison.png')
    plt.close()
    
    print("Performance comparison plot saved as 'rgv_performance_comparison.png'")
    
    # 问题3：调度序列可视化
    print("\nProblem 3: Schedule Visualization")
    print("-" * 40)
    
    # 使用最佳参数集
    params = parameter_sets[0]
    exchang_time_odd = params['exchang_time_odd']
    exchang_time_even = params['exchang_time_even']
    clear_time = params['clear_time']
    time_for_one_step = params['time_for_one_step']
    mov_1_step_t = params['mov_1_step_t']
    mov_2_step_t = params['mov_2_step_t']
    mov_3_step_t = params['mov_3_step_t']
    fitn = params['fitn']
    
    # 生成调度序列并计算时间
    schedule = best_schedule[:50]  # 只显示前50个移动
    
    curent_time = 0
    CNC_finish_time = np.zeros(num_cnc)
    CNC_doing = np.zeros(num_cnc, dtype=int)
    times = []
    cncs = []
    
    for i in range(len(schedule)):
        cnc_idx = schedule[i] - 1
        
        if cnc_idx % 2 == 0:
            curent_time += exchang_time_even
        else:
            curent_time += exchang_time_odd
        
        if CNC_doing[cnc_idx] > 0:
            curent_time += clear_time
        
        CNC_finish_time[cnc_idx] = curent_time + time_for_one_step
        CNC_doing[cnc_idx] = i + 1
        
        times.append(curent_time)
        cncs.append(cnc_idx + 1)
        
        if i < len(schedule) - 1:
            next_cnc_idx = schedule[i + 1] - 1
            if curent_time < CNC_finish_time[next_cnc_idx]:
                curent_time = CNC_finish_time[next_cnc_idx]
            
            current_row = cnc_idx // 2
            next_row = next_cnc_idx // 2
            row_diff = abs(next_row - current_row)
            
            if row_diff > 2:
                curent_time += mov_3_step_t
            elif row_diff > 1:
                curent_time += mov_2_step_t
            elif row_diff > 0:
                curent_time += mov_1_step_t
    
    # 绘制调度序列
    plt.figure(figsize=(12, 6))
    plt.plot(times, cncs, 'ro-', linewidth=2, markersize=8)
    plt.xlabel('Time (s)')
    plt.ylabel('CNC Number')
    plt.title('RGV Scheduling Sequence')
    plt.grid(True)
    plt.savefig('rgv_schedule_sequence.png')
    plt.close()
    
    print("Schedule sequence plot saved as 'rgv_schedule_sequence.png'")
    
    return {
        'best_fitness': best_fitness,
        'best_finished': best_fitness + fitn,
        'parameter_results': results
    }

if __name__ == "__main__":
    result = rgv_dynamic_scheduling()
    print("\n" + "=" * 60)
    print("RGV dynamic scheduling analysis completed!")
    print("=" * 60)