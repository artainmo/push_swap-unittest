import subprocess
import sys
import os
import random
from termcolor import colored

checker_program_path = "../push_swap/checker"
push_swap_program_path = "../push_swap/push_swap"




c_exec = "./" + checker_program_path + " "
p_exec = "./" + push_swap_program_path + " "

def random_int_list(lenght):
    random_list = []
    for i in range(lenght):
        rand = random.randint(-30000, 30000)
        while rand in random_list:
            rand = random.randint(-30000, 30000)
        random_list.append(rand)
    random_list = " ".join(str(x) for x in random_list)
    return random_list

#name - expected output - command
checker_tests = [["Non-numerical input", "Error", c_exec + "a b c"],      
                 ["Duplicate numerical", "Error", c_exec + "1 2 1"],
                 ["Higher max int", "Error", c_exec + "1 2 2147483649"],
                 ["Lower min int", "Error", c_exec + "-2147483649 1 2"],
                 ["Empty", "", c_exec],
                 ["Non-existent command", "Error",  "echo 'wq' | " + c_exec + "1 2"],
                 ["Non-existent command spaces", "Error", "echo 'sa ' | " + c_exec + "1 2"],
                 ["Existent command KO", "KO\n", "echo 'sa\npb\nrrr' | " + c_exec + "0 9 1 8 2 7 3 6 4 5"],
                 ["Existent command KO", "KO\n", "echo 'sb\npa\nrr' | " + c_exec + "0 9 1 8 2 7 3 6 4 5"],
                 ["Operations no segfault", "KO\n", "echo 'pa\npa\npb\nsb\nrb\nrrb\npb\nra\nrb' | " + c_exec + "0 9 1 8 2 7"],
                 ["Instantly OK", "OK\n", "echo '' | " +  c_exec + "0 1 2"],
                 ["Multiple commands OK", "OK\n", "echo 'pb\nra\npb\nra\nsa\nra\npa\npa' | " +  c_exec + "0 9 1 8 2"],
                 ["Long multiple commands OK", "OK\n", "echo 'pb\nsa\nra\nsa\nrr\nrr\npb\nsa\nra\nsa\npb\nrrr\nsa\nsa\npb\nsa\nrr\npb\npa\npa\nrr\nsa\npb\nrrb\nrrb\npa\npa\nsb\npa\npa\nrra\nrra' |  " + c_exec + "0 9 1 8 2 7 5 3 -12"]]

r5list1 = random_int_list(5)
r5list2 = random_int_list(5)
r5list3 = random_int_list(5)
r100list1 = random_int_list(100)
r100list2 = random_int_list(100)
r100list3 = random_int_list(100)
r500list1 = random_int_list(500)
r500list2 = random_int_list(500)
r500list3 = random_int_list(500)

push_swap_tests = [["Sorted list", "", p_exec + "42"],
                   ["Sorted list", "", p_exec + "-15 0 1 2 3"],
                   ["Sorted list", "", p_exec + "0 1 2 3 4 5 6 7 8"],
                   ["Simple test lines", [3, 0], p_exec + "2 1 0 | wc -l"],
                   ["Simple test ok/ko", "OK\n", p_exec + "2 1 0 | " + c_exec + "2 1 0"],
                   ["Simple test 2 lines", [12, 0], p_exec + "1 5 2 4 3 | wc -l"],
                   ["Simple test 2 ok/ko", "OK\n", p_exec + "1 5 2 4 3 | " + c_exec + "1 5 2 4 3"],
                   ["Simple random 1 lines", [12, 0], p_exec + r5list1 + " | wc -l"],
                   ["Simple random 1 ok/ko", "OK\n", p_exec + r5list1 + " | " + c_exec + r5list1],
                   ["Simple random 2 lines", [12, 0], p_exec + r5list2 + " | wc -l"],
                   ["Simple random 2 ok/ko", "OK\n", p_exec + r5list2 + " | " + c_exec + r5list2],
                   ["Simple random 3 lines", [12, 0], p_exec + r5list3 + " | wc -l"],
                   ["Simple random 3 ok/ko", "OK\n", p_exec + r5list3 + " | " + c_exec + r5list3],
                   ["Medium random 1 lines", [700, 1500], p_exec + r100list1 + " | wc -l"],
                   ["Medium random 1 ok/ko", "OK\n", p_exec + r100list1 + " | " + c_exec + r100list1],
                   ["Medium random 2 lines", [700, 1500], p_exec + r100list2 + " | wc -l"],
                   ["Medium random 2 ok/ko", "OK\n", p_exec + r100list2 + " | " + c_exec + r100list2],
                   ["Medium random 3 lines", [700, 1500], p_exec + r100list3 + " | wc -l"],
                   ["Medium random 3 ok/ko", "OK\n", p_exec + r100list3 + " | " + c_exec + r100list3],
                   ["Advanced random 1 lines", [5500, 11500], p_exec + r500list1 + " | wc -l"],
                   ["Advanced random 1 ok/ko", "OK\n", p_exec + r500list1 + " | " + c_exec + r500list1],
                   ["Advanced random 2 lines", [5500, 11500], p_exec + r500list2 + " | wc -l"],
                   ["Advanced random 2 ok/ko", "OK\n", p_exec + r500list2 + " | " + c_exec + r500list2],
                   ["Advanced random 3 lines", [5500, 11500], p_exec + r500list3 + " | wc -l"],
                   ["Advanced random 3 ok/ko", "OK\n", p_exec + r500list3 + " | " + c_exec + r500list3]]

leak_tests = [["LEAK: Sorted list", "leaks", "valgrind --leak-check=full --show-leak-kinds=all " + p_exec + "42"],
             ["LEAK: Duplicate numerical", "leaks", "valgrind --leak-check=full --show-leak-kinds=all " + c_exec + "1 2 1"],
             ["LEAK: Non-existent command", "leaks", "valgrind --leak-check=full --show-leak-kinds=all " +  "echo 'wq' | " + c_exec + "1 2"],
             ["LEAK: Simple random 3 ok/ko", "leaks", "valgrind --leak-check=full --show-leak-kinds=all " + p_exec + r5list3 + " | " + c_exec + r5list3]]


def verify(output, test_name, expected_result, cmd):
    print(test_name.ljust(100), end="")
    err_color = "red"
    if isinstance(expected_result, list):
        if int(output) <= expected_result[0] and int(output) != 0:
            correct = True
        elif int(output) <= expected_result[1] and int(output) != 0:
            correct = False
            err_color = "yellow"
        else:
            correct = False
    elif expected_result == "leaks":
        if output.find("All heap blocks were freed -- no leaks are possible") != -1:
            correct = True
        else:
            correct = False
    elif expected_result == "Error":
        if output.strip("\n") == "Error":
            correct = True
        else:
            correct = False
    elif output == expected_result:
        correct = True
    else:
        correct = False
    if correct == True:
        print(colored("<>", "green"))
    else:
        print(colored("<>", err_color))
        with open("errors.txt", "a+") as fd:
            if isinstance(expected_result, list):
                if int(output) == 0:
                    fd.write("NOTE: if already ordered not really wrong else error occured during program execution\n")
            fd.write("TEST: " + test_name + " " + cmd  + "\n")
            fd.write("YOU: " + output + "\n")
            fd.write("EXPECTED: " + str(expected_result) + "\n============================================================\n\n")

def test(test_name, test_expected_result, cmd):
    try:
        output = subprocess.Popen(cmd, shell=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = output.communicate(timeout=60)
    except:
        print(test_name)
        print("timout: infinite loop?")
        print("Command:\n" + cmd)
        exit()
    if test_expected_result == "Error" or test_expected_result == "leaks":
        output = output[1]
    else:
        output = output[0]
    verify(output, test_name, test_expected_result, cmd)

if __name__=="__main__":
    try:
        os.remove("errors.txt")
    except:
        pass
    os.system("clear")
    print(colored("CHECKER TESTS", "yellow"))
    for t in checker_tests:
        test(t[0], t[1], t[2])
    print(colored("\nPUSH_SWAP TESTS", "yellow"))
    for t in push_swap_tests:
        test(t[0], t[1], t[2])
    if len(sys.argv) > 1 and sys.argv[1] == "leaks":
        print(colored("\nLEAK TEST", "yellow"))
        print("Make sure to have valgrind installed")
        for t in leak_tests:
            test(t[0], t[1], t[2])   

