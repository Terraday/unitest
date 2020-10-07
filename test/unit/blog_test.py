from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test','Peter',[])
        
        self.assertEqual('Peter',b.author)
        self.assertEqual([],b.posts)

    def test_repr(self):
        b = Blog('Test','Peter',[1,2])
        b2 = Blog('My Day','Josue',[1])
        
        self.assertEqual(b.__repr__(),'Test por Peter (2 posts)')
        self.assertEqual(b2.__repr__(),'My Day por Josue (1 post)')

    def test_tarea(self):
        pass