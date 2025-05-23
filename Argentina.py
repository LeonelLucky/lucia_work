import unittest


inadimplentes = ["João", "Maria", "Carlos"]

def verificar_elegibilidade(nome, idade, renda_mensal, escolaridade_superior):
    motivos = []

    if idade < 18:
        motivos.append("Idade inferior a 18 anos.")
    if renda_mensal < 2000:
        motivos.append("Renda mensal inferior a R$ 2.000.")
    if nome in inadimplentes:
        motivos.append("Nome está na lista de inadimplentes.")
    if not escolaridade_superior:
        motivos.append("Escolaridade não é superior.")

    if motivos:
        return (False, motivos)
    return (True, ["Elegível para o empréstimo."])


class TestElegibilidadeEmprestimo(unittest.TestCase):
    def test_1_elegivel(self):
        status, motivos = verificar_elegibilidade("Ana", 25, 3000, True)
        self.assertTrue(status)
        self.assertIn("Elegível para o empréstimo.", motivos)

    def test_2_idade(self):
        status, motivos = verificar_elegibilidade("Bruno", 17, 3000, True)
        self.assertFalse(status)
        self.assertIn("Idade inferior a 18 anos.", motivos)

    def test_3_renda(self):
        status, motivos = verificar_elegibilidade("Carla", 25, 1500, True)
        self.assertFalse(status)
        self.assertIn("Renda mensal inferior a R$ 2.000.", motivos)

    def test_4_inadimplente(self):
        status, motivos = verificar_elegibilidade("João", 30, 3000, True)
        self.assertFalse(status)
        self.assertIn("Nome está na lista de inadimplentes.", motivos)

    def test_5_escolaridade(self):
        status, motivos = verificar_elegibilidade("Letícia", 22, 3000, False)
        self.assertFalse(status)
        self.assertIn("Escolaridade não é superior.", motivos)

    def test_6_multiplos_motivos(self):
        status, motivos = verificar_elegibilidade("Pedro", 16, 1500, False)
        self.assertFalse(status)
        self.assertIn("Idade inferior a 18 anos.", motivos)
        self.assertIn("Renda mensal inferior a R$ 2.000.", motivos)
        self.assertIn("Escolaridade não é superior.", motivos)

    def test_7_todas_falsas(self):
        status, motivos = verificar_elegibilidade("Maria", 17, 1000, False)
        self.assertFalse(status)
        self.assertEqual(len(motivos), 4)

if __name__ == "__main__":
    unittest.main()
