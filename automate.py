import subprocess
import time
import os
import resource
import psutil
import platform
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns

def complieProgram(c_program,program_name):
    subprocess.run(["gcc", c_program, "-o", program_name])

def isProgram_exists(program):
    if not os.path.exists(program):
        print(f"Error: Program '{program}' not found.")
        return None, f"Program {program} not found "
    return True," "

def isTestcase_exists(testcase):
    if not os.path.exists(testcase):
        print(f"Error: Input file '{testcase}' not found.")
        return None, f"Input {testcase} file not found"
    return True," "

def run_c_program_with_input(program, input_file):

    if platform.system() == "Windows":
        before_memory = psutil.virtual_memory().used
    else:
        before_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()  # Record the start time
    process = subprocess.Popen([program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    with open(input_file, 'r') as f:
        input_data = f.read()
    stdout, stderr = process.communicate(input=input_data)
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time in seconds
    # Get system's virtual memory usage before and after running the program using 'resource' library
    if platform.system() == "Windows":
         after_memory = psutil.virtual_memory().used
    else:
        after_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # Ensure that before_memory is less than after_memory
    memory_usage = max(after_memory - before_memory, 0)

    # Convert memory usage to kilobytes (KB)
    memory_usage_kb = memory_usage / (1024**2)

    return stdout, stderr, execution_time, memory_usage_kb

def plot_bar(df : pd.DataFrame):
    __,ax = plt.subplots()

    ax.set_title('Algorithm Runtimes')
    ax.set_xlabel('Test Size')
    ax.set_ylabel('Runtime (seconds)')

    df.plot.bar(ax=ax)

    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    plt.xticks(rotation=0)
    plt.savefig('avg_execution_time_plot_bar.png')
    plt.show()

def plot_line(df : pd.DataFrame):
    
    __,ax = plt.subplots()

    ax.set_title('Algorithm Runtimes')
    ax.set_xlabel('Test Size')
    ax.set_ylabel('Runtime (seconds)')

    df.plot(ax=ax)

    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    plt.xticks(rotation=0)
    plt.savefig('avg_execution_time_plot_line.png')
    plt.show()

def main():
    # Provide a list of input file paths
    c_program = ["bubbleSort.c","insertionSort.c","selectionSort.c","mergeSort.c","quickSort.c"]
    test_input_files = ["testcase/10.txt","testcase/100.txt","testcase/1000.txt","testcase/10000.txt"]
    if platform.system() == "Windows":
        program_names = ["bubbleSort.exe","insertionSort.exe","selectionSort.exe","mergeSort.exe","quickSort.exe"]
    else:
        program_names = ["./bubbleSort","./insertionSort","./selectionSort","./mergeSort","./quickSort"]  # Change this to the correct executable names
    num_try = 5
    output_file = "output.txt"
    results = []  # Store the results in a list
    time_result = []
    memory_result = []
    avg_execution_times = [[] for _ in program_names]
    for i,c in enumerate(c_program):
        res,c_error = isProgram_exists(c)
        if res == None:
            print(c_error)
            return 0
    for i,program_name in enumerate(program_names):
        res,c_error = isProgram_exists(program_name)
        if res == None:
            for i,program_name in enumerate(program_names):
                complieProgram(c_program[i],program_name)
            time.sleep(5)
            print("All C programs are compiled. Please re-run the program")
            return 0
    for i,testcase in enumerate(test_input_files):
        res,c_error = isTestcase_exists(test_input_files[i])
        if res == None:
            print(c_error)
            return 0

    with open(output_file,'w') as f:
        f.write('')

    for i in range(len(program_names)):
        empty1 = []
        empty2 = []
        for j in range(len(test_input_files)):
            empty1.append(0)  # Initialize with 0
            empty2.append(0)  # Initialize with 0
        time_result.append(empty1)
        memory_result.append(empty2)

    for i in range(len(program_names)):
        for j in range(len(test_input_files)):
            for try_round in range(num_try):
                c_output, c_error, execution_time, memory_usage = run_c_program_with_input(program_names[i], test_input_files[j])
                results.append((program_names[i], test_input_files[j], try_round, c_output, c_error, execution_time, memory_usage))
                time_result[i][j] += execution_time
                memory_result[i][j] += memory_usage
    
    for i in range(len(program_names)):
        for j in range(len(test_input_files)):
            time_result[i][j] /= 5
            memory_result[i][j] /= 5
            avg_execution_times[i].append(time_result[i][j])

    for i, result in enumerate(results):
        program_name, test_input_file, try_round, c_output, c_error, execution_time, memory_usage = result
        if try_round == 0:
            output_text = f'[ {program_name:<24} : {test_input_file:20} ]'
            with open(output_file,'a') as f:
                f.write(output_text+'\n')
            print(output_text)
        output_text = f"Round : {try_round+1} | Execution time: {execution_time:.6f} seconds | Memory usage: {memory_usage:.2f} MB"
        print(output_text)
        with open(output_file,'a') as f:
          f.write(output_text+'\n')
        # if c_error:
            # print(f"Error: {c_error}")
        # else:
            # print(f"Output: {c_output}")
            # print(f"Success!")
        if try_round+1 == num_try:
            print(f"")
    print(f'')
    with open(output_file,'a') as f:
        f.write(f'------- RESULT --------\n')
    print(f'------- RESULT --------')
    for i, time_result_row in enumerate(time_result):
        for j, avg_time in enumerate(time_result_row):
            output_text = f'Sort : {program_names[i]:<20} Case : {test_input_files[j]:<20} Avg. Time : {avg_time:.6f} s  Avg. Memory : {memory_result[i][j]:.6f} MB'
            with open(output_file,'a') as f:
                f.write(output_text+"\n")
            print(output_text)

    with open('output_with_label.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(time_result)

    col_label =  [name.replace("testcase/", "").replace(".txt", "") for name in test_input_files]
    row_label =  [name.replace(".exe", "") for name in program_names]

    df = pd.read_csv('output_with_label.csv', names = col_label, header = None)
    df.insert(loc = 0, column='Test Size', value=row_label)
    df = df.set_index('Test Size').T
    df.index.name='Test Size'
    df.to_csv("output_with_label.csv") 

    #plot : edit in plot function 
    plot_line(df)
    plot_bar(df)

if __name__ == "__main__":
    main()
