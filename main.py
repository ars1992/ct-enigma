from Enigma import Enigma




enigma = Enigma(r1_pos=16,
                r2_pos=8,
                r3_pos=23,
                patch_key="YELCPBHJUSVR" + "QTXWZNGDFAKMIO",
                rotor_selection=[2, 4, 0],
                reflector_selection=2)

enigma2 = Enigma(r1_pos=16,
                r2_pos=8,
                r3_pos=23,
                patch_key="YELCPBHJUSVR" + "QTXWZNGDFAKMIO",
                rotor_selection=[2, 4, 0],
                reflector_selection=2)

plaintext = "HALLO"
encrypt_text = enigma.encrypt(plaintext)
print(encrypt_text)
print(enigma2.decrypt(encrypt_text))
