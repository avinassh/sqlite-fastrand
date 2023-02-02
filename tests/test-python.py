import unittest
import sqlite3
import sqlite_fastrand

class TestSqlitefastrandPython(unittest.TestCase):
  def test_path(self):
    db = sqlite3.connect(':memory:')
    db.enable_load_extension(True)

    self.assertEqual(type(sqlite_fastrand.loadable_path()), str)
    
    sqlite_fastrand.load(db)
    version, = db.execute('select fastrand_version()').fetchone()
    self.assertEqual(version[0], "v")

if __name__ == '__main__':
    unittest.main()