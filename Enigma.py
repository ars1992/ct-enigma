class Enigma:
    def __int__(self,
                patch_key: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                rotor_selection: list = [0, 1, 2],
                reflector_selection: int = 0,
                r1_pos: int = 0,
                r2_pos: int = 0,
                r3_pos: int = 0):

        self.position = 0
        self.patch_key = patch_key
        self.al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                  'AJDKSIRUXBLHWTMCQGZNPYFVOE',
                  'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                  'ESOVPZJAYQUIRHXLNFTGKDCMWB',
                  'VZBRGITYUPSDNHLXAWMJQOFECK']

        reflectors = ["EJMZALYXVBWFCRQUONTSPIKHGD",
                      "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                      "FVPJIAOYEDRZXWGCTKUQSBNMHL"]

        self.r1 = rotors[rotor_selection[0]]
        self.r2 = rotors[rotor_selection[1]]
        self.r3 = rotors[rotor_selection[2]]
        self.re = reflectors[reflector_selection]
        self.r1_pos = r1_pos
        self.r2_pos = r2_pos
        self.r3_pos = r3_pos
        self.c_offset = int('A'.encode("ascii")[0])

