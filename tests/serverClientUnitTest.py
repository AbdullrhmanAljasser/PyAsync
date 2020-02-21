import unittest
from main.sServer import sServer
from main.sClient import sClient
from main.Library import Library
from runBG import runBG


class TestingServerClient(unittest.TestCase):

    # #Testing Client Server connection
    # def test_singleConnection(self):
    #     #runBG()
    #     msg = "test"
    #     ##The server is ran before the unittest is ran
    #     #sSocket = sServer()
    #     cSocket = sClient()
    #     self.assertIsNotNone(cSocket.send(msg))
    #     cSocket.close()

    # def test_MultipleConnection(self):
    #     #runBG()
    #     msg = "test"
    #     ##The server is ran before the unittest is ran
    #     #sSocket = sServer()
    #     cSocket = sClient()
    #     cSocket2= sClient()
    #     self.assertIsNotNone(cSocket.send(msg))
    #     self.assertIsNotNone(cSocket2.send(msg))
    #     cSocket.close()
    #     cSocket2.close()

    # def test_clientCommunication(self):
    #     #runBG()
    #     msg = "Hi"
    #     ##Server is supposed to be ran outside
    #     cSocket = sClient()
    #     s = cSocket.send(msg)
    #     self.assertEqual(s[0], str(-1))
    #     cSocket.close()

    # def test_adminCreateStaff(self):
    #     runBG()
    #     admin = sClient()
    #     admin.send('admin')
    #     admin.send('crstaff,S1002')
    #     self.assertTrue(Library().staffExists("S1002"))
    #     admin.send('exit')

    # def test_staffCreatePatreon(self):
    #     runBG()
    #     staff = sClient()
    #     staff.send('staff,s1000')
    #     staff.send('crpatreon,p1001,jack')
    #     self.assertTrue(Library().patreonExists("p1001"))
    #     staff.send('exit')

    # def test_bookInsertion(self):
    #     runBG()
    #     s = sClient()
    #     s.send('staff,s1000')
    #     s.send('addbook,b1001,Hunger Games')
    #     self.assertTrue(Library().bookExists('b1001'))
    #     s.send('exit')

    def test_bookBorrow(self):
        runBG()
        s = sClient()
        s.send('patreon,p1000')
        s.send("borrow,b1000")
        self.assertTrue(Library().getPatreon('p1000').bExists('b1000'))


if __name__== '__main__':
    unittest.main()