#!/usr/bin/env pypy

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-05-05"

class Turing:
    __debug = False

    def directSolution(self, inTape):
        """
        This method is the result of the analysis of the behabehaviours of the turin maching with
        All the possible inputs. I used a black box tech to obtain this.
        The structure of the tapes are:
            #times#number_1#number_2#...#number_n#
        And the machine perform two phases:
            - 1. Add "times" times the #number_1#number_2#...#number_n# at the end of the tape
                 The "times" part is a countes, at the end this part is full of zeroes
            - 2. Reduce the tape adding the last number with the previous one until have only one number
        
        The solutin is the num of the numbers multiplied by "times" :)
           
        """
        tapeParts = inTape.split('#', 2)
        tapeParts.pop(0)
        repeat = int(tapeParts[0], 2)

        value = 0
        for part in tapeParts[1][:-1].split('#'):
            value += int(part, 2)

        return "#%s#" % (bin(value * repeat)[2:].zfill(len(tapeParts[0])))

    def resolve(self, inTape):
        """
        This is the method who implements the Turing machine step by step.
        I added some traces in order to show the tape for each cicle, and be able to analyze it as a black box
        """
        tape = list(inTape)
        head = 0
        state = 'start'
        lastStr = ''

        # Read the tape until be at the "end" status
        while state != 'end':
            # Check witch is the corrent movement, and move the tape, if the tape is at the end,
            # add a new _ character
            if head >= len(tape):
                currentChar = '_'
                tape.append(currentChar)
            else:
                currentChar = tape[head]

            action = self.__machine[state][currentChar]

            if state == action[2] and tape[head] == action[0]:
                # Well, we are simply moving the head to find a different char, move the head
                if action[1] == 'R':
                    while head < len(tape) and tape[head] == action[0]:
                        head += 1
                elif action[1] == 'L':
                    while tape[head] == action[0]:
                        head -= 1
            else:
                tape[head] = action[0]
                state = action[2]

                # Move the head acording to the current action
                if action[1] == 'R':
                    head += 1
                elif action[1] == 'L':
                    head -= 1

            tapeStr = ''.join(tape).rstrip('_')
            if lastStr != tapeStr:
                parts = tapeStr.split('#')
                print parts
                try:
                    print "Last: %d # %d # %d" % (int(parts[len(parts) - 4], 2), int(parts[len(parts) - 3], 2), int(parts[len(parts) - 2], 2))
                except:
                    pass
            lastStr = tapeStr

            if self.__debug:
                print action
                print tape

        return ''.join(tape).rstrip('_')

    def __init__(self, inMachine = ''):
        """
        The constructor creates the machine from the string given on the problem
        I do this, in order to don't waste hours creatin the structure by hand, is easy and more secure :)
        The structure of the machine is:
            machine[current_state][char_read_from_the_tape] => (char_to_write_on_the_table, way_to_move_the_tape, final_status_after_execute)
        If the machine is not specified, don't create the machone, the machine is used only for analysis propousals
        """
        if inMachine != '':
            self.__machine = {}
            for line in inMachine.split('\n'):
                parts = line.strip().split(',')
                charsToRead = parts[1].split(':')
                if parts[0] in self.__machine:
                    self.__machine[parts[0]][charsToRead[0]] = (charsToRead[1], parts[2], parts[3])
                else:
                    self.__machine[parts[0]] = {charsToRead[0]: (charsToRead[1], parts[2], parts[3])}

            if self.__debug:
                print self.__machine

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    machine = Turing()
    for line in lines:
        print "%s" % (machine.directSolution(line))

    # Remove this exit in order to use the full turing machine, this part is only for
    # analysis propousals
    exit()

    # I pass the machine as a string in order to be parsed by the system
    machine = Turing("""start,#:%,R,state0
        state0,0:0,R,state0
        state0,1:1,R,state0
        state0,#:#,S,state1
        state1,#:#,L,state1
        state1,$:$,L,state1
        state1,1:0,R,state2
        state1,0:1,L,state1
        state2,1:1,R,state2
        state2,0:0,R,state2
        state2,#:#,L,state3
        state2,$:$,L,state3
        state3,0:0,L,state3
        state3,1:1,R,state4
        state3,%:%,R,state5
        state4,0:0,R,state4
        state4,1:1,R,state4
        state5,1:1,R,state5
        state5,0:0,R,state5
        state5,#:#,S,state6
        state5,$:$,S,state6
        state4,#:#,S,state7
        state4,$:$,S,state7
        state7,#:$,R,state8
        state7,$:$,R,state9
        state8,1:1,R,state8
        state8,0:0,R,state8
        state8,#:#,R,state8
        state8,_:_,L,state10
        state10,#:$,L,state11
        state11,1:1,L,state11
        state11,0:0,L,state11
        state11,#:#,L,state11
        state11,$:$,R,state9
        state9,1:_,R,state12
        state9,0:_,R,state13
        state9,#:_,R,state14
        state9,$:$,S,state15
        state12,1:1,R,state12
        state12,0:0,R,state12
        state12,#:#,R,state12
        state12,$:$,R,state12
        state12,_:1,L,state16
        state16,1:1,L,state16
        state16,0:0,L,state16
        state16,#:#,L,state16
        state16,$:$,L,state16
        state16,_:1,R,state9
        state13,1:1,R,state13
        state13,0:0,R,state13
        state13,#:#,R,state13
        state13,$:$,R,state13
        state13,_:0,L,state17
        state17,1:1,L,state17
        state17,0:0,L,state17
        state17,#:#,L,state17
        state17,$:$,L,state17
        state17,_:0,R,state9
        state14,1:1,R,state14
        state14,0:0,R,state14
        state14,#:#,R,state14
        state14,$:$,R,state14
        state14,_:#,L,state18
        state18,1:1,L,state18
        state18,0:0,L,state18
        state18,#:#,L,state18
        state18,$:$,L,state18
        state18,_:#,R,state9
        state15,1:1,R,state15
        state15,0:0,R,state15
        state15,#:#,R,state15
        state15,$:$,R,state15
        state15,_:#,L,state19
        state19,1:1,L,state19
        state19,0:0,L,state19
        state19,#:#,L,state19
        state19,$:$,L,state20
        state20,1:1,L,state20
        state20,0:0,L,state20
        state20,#:#,L,state20
        state20,$:$,S,state1
        state6,1:1,R,state6
        state6,0:0,R,state6
        state6,#:#,R,state6
        state6,$:#,R,state6
        state6,_:_,L,state21
        state21,#:#,L,state22
        state22,1:1,L,state22
        state22,0:0,L,state22
        state22,#:#,L,state23
        state22,%:#,S,end
        state23,1:1,R,state23
        state23,0:0,R,state23
        state23,#:#,R,state23
        state23,_:_,L,state24
        state24,#:#,L,state25
        state25,0:0,L,state25
        state25,1:1,R,state26
        state25,#:#,R,state27
        state26,0:0,R,state26
        state26,1:1,R,state26
        state27,1:1,R,state27
        state27,0:0,R,state27
        state27,#:_,L,state28
        state26,#:#,L,state29
        state29,1:0,L,state30
        state29,0:1,L,state29
        state30,1:1,L,state30
        state30,0:0,L,state30
        state30,#:#,L,state31
        state31,1:0,L,state31
        state31,0:1,R,state32
        state32,1:1,R,state32
        state32,0:0,R,state32
        state32,#:#,R,state32
        state32,_:_,L,state21
        state28,1:_,L,state28
        state28,0:_,L,state28
        state28,#:#,S,state21""")

    for line in lines:
        print "%s" % (machine.resolve(line))
