import os
from random import *

class Practice:
    def menu():

        problem_count = 0
        completed_problem_count = 0
        attempted_problem_count = problem_count + completed_problem_count

        def clear_screen():
            os.system('clear')
        
        os.mkdir('tmp')

        selecting = True
        while (selecting):

            print(f'\nProblems completed -> {completed_problem_count}')
            print(f'\nProblems attempted -> {attempted_problem_count}')

            editor = "vim"

            choice = input("\n[1- Start, q- quit]")

            # Choice one description
            if (choice == "1"):
                clear_screen()
                working = True
                currProb = Problem()
                while (working):
                    print("[1- New Problem, 2- Solution, 3- Start, q- quit]\n")
                    print(f"{currProb.problem_name}")
                    print(f"\n{currProb.prompt}")

                    problem_option = input()
                    if (problem_option == '1'):
                        currProb = Problem()
                        clear_screen()

                    elif (problem_option == '2'):
                        os.system(f"find Grokking/All -name \"{currProb.problem_name}\" | xargs {editor}")

                    elif (problem_option == '3'):
                        problem_count += 1
                        os.system(f"echo '{currProb.prompt}' > tmp/quiz{problem_count}.cpp")
                        os.system(f"{editor} tmp/quiz{problem_count}.cpp")
                        complete = False
                        clear_screen()
                        print("[1- New Problem, 2- Solution, 3- Continue, 4- Correct, 5- Incorrect, q- Quit]\n")
                        print(f"{currProb.problem_name}")
                        print(f"\n{currProb.prompt}")

                        while (True):
                           
                            working_option = input()
                            if (working_option == '1'):
                                currProb = Problem()
                                clear_screen()
                                break

                                # check if complete == false
                                path = f'tmp/quiz{problem_count}'
                                if (complete == false and os.path.exists(path)):
                                    os.remove(f'tmp/quiz{problem_count}')
                                    

                            elif (working_option == '2'):
                                os.system(f"find Grokking/All -name \"{currProb.problem_name}\" | xargs {editor}")

                            elif (working_option == '3'):
                                os.system(f"{editor} tmp/quiz{problem_count}.cpp")


                            elif (working_option == '4'):
                                completed_problem_count += 1
                                currProb = Problem()
                                complete = True
                                clear_screen()
                                break

                            elif (working_option == '5'):
                                attempted_problem_count += 1
                                currProb = Problem()
                                complete = True
                                clear_screen()
                                break

                            elif (working_option == 'q'):
                                working = False
                                break

                    elif (problem_option == 'q'):
                        break

                    clear_screen()

            # To leave app
            elif (choice == "q"):
                os.system('rm -r tmp');
                clear_screen()
                break

            # Bad user input
            else:
                print("Wrong input")

            clear_screen()

    def _range_of_problems():
        pass

    def _non_stop():
        pass

    
class Problem:
    def __init__(self, random=True):
        if (random):
            problem_name = Problem._get_random_problem()
            self.problem_name = problem_name
            with open(f"Grokking/All/{problem_name}") as file:
                text = file.read()
                file.close()
                prompt = text[text.find("/*")+2:text.find("*/")]
                self.prompt = "/*" + prompt + "*/"

        else:
            self.problem_path = Problem._get_certain_problem()


    def get_prompt(self):
        return self.prompt

    def _get_random_problem():
        problems = os.listdir('Grokking/All')
        random_selection = problems[randint(0, len(problems)-1)]
        return random_selection

    def _get_certain_problem(topic, name):
        pass 


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(" __       __            __                                              __")
    print("/  |  _  /  |          /  |                                            /  |")
    print("$$ | / \\ $$ |  ______  $$ |  _______   ______   _____  ____    ______  $$ |")
    print("$$ |/$  \\$$ | /      \\ $$ | /       | /      \\ /     \\/    \\  /      \\ $$ |")
    print("$$ /$$$  $$ |/$$$$$$  |$$ |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |$$ |")
    print("$$ $$/$$ $$ |$$    $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$    $$ |$$/")
    print("$$$$/  $$$$ |$$$$$$$$/ $$ |$$ \\_____ $$ \\__$$ |$$ | $$ | $$ |$$$$$$$$/  __ ")
    print("$$$/    $$$ |$$       |$$ |$$       |$$    $$/ $$ | $$ | $$ |$$       |/  |")
    print("$$/      $$/  $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/ $$/ ")
    print("===========================================================================")


    Practice.menu()

if __name__ == "__main__":
    main()
