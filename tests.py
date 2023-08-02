import unittest
from appower.worker import Energy
class TestEnergy(unittest.TestCase):

    def test_get_energy_file_404(self):
        rapl = Energy()
        rapl.program_name = 'notfound404'
        self.assertRaises(FileNotFoundError, rapl.get_rapl_energy())
        
    def test_get_energy(self):
        rapl = Energy()
        rapl_energy = rapl.get_rapl_energy()
        self.assertIsInstance(rapl_energy, str)

