from .test_setup import TestSetup


class TestViews(TestSetup):
    
    def test_user_cannot_registerwithnodata(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)
