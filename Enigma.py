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

        
