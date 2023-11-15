from finiteautomata import FiniteAutomata

if __name__ == "__main__":
    done = False
    finite_automata = FiniteAutomata.read_from_file("fa.in")
    while not done:
        print("1. display finite automaton.")
        print("2. display finite automaton states.")
        print("3. display finite automaton alphabet.")
        print("4. display finite automaton transitions.")
        print("5. display finite automaton final states.")
        print("6. check for deterministic finite automaton.")
        print("7. check for accepted sequence.")
        command = input(">>")
        if command == "1":
            print(str(finite_automata))
        elif command == "2":
            print(finite_automata.Q)
        elif command == "3":
            print(finite_automata.E)
        elif command == "4":
            print(finite_automata.S)
        elif command == "5":
            print(finite_automata.F)
        elif command == "6":
            print(finite_automata.is_dfa())
        elif command == "7":
            sequence = input(">>")
            print(finite_automata.is_accepted(sequence))
        else:
            done = True
