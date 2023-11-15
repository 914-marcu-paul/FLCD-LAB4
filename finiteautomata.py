class FiniteAutomata:

    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    @staticmethod
    def get_line(line):
        # we use this method to only read characters past the equality sign in the input file
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        # we check if the starting state is in the total states
        if q0 not in Q:
            return False
        # we check if all possible final states are in the total states
        for f in F:
            if f not in Q:
                return False
        # we check if for every transition, the state is in the total states, the symbol is in the alphabet,
        # and the destination state is in the total states
        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for destination in S[key]:
                if destination not in Q:
                    return False
        return True

    @staticmethod
    def read_from_file(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.get_line(file.readline())
            E = FiniteAutomata.get_line(file.readline())
            # here we limit the line read to only the first letter
            q0 = FiniteAutomata.get_line(file.readline())[0]
            F = FiniteAutomata.get_line(file.readline())

            file.readline()

            # we read all the lines after the S character, representing all the transitions in the finite automata
            S = {}
            for line in file:
                pair = line.strip().split('->')
                state = pair[0].strip().replace('(', '').replace(')', '').split(',')[0]
                symbol = pair[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = pair[1].strip()
                # if the state + symbol combo already exists, we add an extra destination onto the existing ones
                if (state, symbol) in S.keys():
                    S[(state, symbol)].append(destination)
                # if the state + symbol combo doesn't exist, we instantiate the destination list
                else:
                    S[(state, symbol)] = [destination]

            # we check the validity of the data read from the file
            if not FiniteAutomata.validate(Q, E, q0, F, S):
                raise Exception("incorrect input file.")

            return FiniteAutomata(Q, E, q0, F, S)

    # we check if the finite automaton is deterministic (more than 1 possible destination from a given state and input)
    def is_dfa(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def is_accepted(self, seq):
        if self.is_dfa():
            state = self.q0
            visited = []
            for symbol in seq:
                if (state, symbol) not in self.S.keys():
                    return False
                # we go through the final automata until we can't anymore with the given symbol
                while (state, symbol) in self.S.keys() and (state, symbol) not in visited:
                    visited.append((state, symbol))
                    print("visited: " + str(visited))
                    state = self.S[(state, symbol)][0]
                    print("new state: " + state)
            return state in self.F
        return False

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n E = { " + ', '.join(self.E) + " }\n q0 = { " + self.q0 + \
               " }\n F = { " + ', '.join(self.F) + " }\n S = { " + str(self.S) + " } "
