import unittest
from  ..app.models import NewsSource

class TestSource(unittest.TestCase):
    
    def setUp(self):
        
        self.new_source = NewsSource('1234','Disney','World','Yes')
        
    def test_initialised(self):
        
        self.new_source
        self.assertTrue(isinstance(self.new_source, NewsSource))
