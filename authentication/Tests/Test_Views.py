from .Test_setup import TestSetup

class TestViews(TestSetup):
    
    def user_can_not_registerwithnodata(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)
        