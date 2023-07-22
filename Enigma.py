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


    def encrypt_char(self, c: str) -> str:
        step0 = self.patch_key[int(c.encode("ascii")[0]) - self.c_offset]
        step1 = self.r1[(int(step0.encode("ascii")[0]) - self.c_offset + (self.position // len(self.al) ** 2) + self.r1_pos % len(self.al))]
        step2 = self.r2[(int(step1.encode("ascii")[0]) - self.c_offset + (self.position // len(self.al)) + self.r2_pos) % len(self.al)]
        step3 = self.r3[(int(step2.encode("ascii")[0]) - self.c_offset + self.position + self.r3_pos) % len(self.al)]
        step4 = self.re[int(step3.encode("ascii")[0]) - self.c_offset]
        step5 = self.r3[(int(step4.encode("ascii")[0]) - self.c_offset + self.position + self.r3_pos) % len(self.al)]
        step6 = self.r2[(int(step5.encode("ascii")[0]) - self.c_offset + (self.position // len(self.al)) + self.r2_pos) % len(self.al)]
        step7 = self.r1[(int(step6.encode("ascii")[0]) - self.c_offset + (self.position // len(self.al) ** 2) + self.r1_pos) % len(self.al)]
        step8 = self.patch_key[int(step7.encode("ascii")[0]) - self.c_offset]
        self.position += 1