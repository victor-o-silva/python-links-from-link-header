import unittest
import links_from_header


class ExtractTestCase(unittest.TestCase):
    def test_github_header(self):
        header = ('<https://api.github.com/user/repos?page=1>; rel="first", ' +
                  '<https://api.github.com/user/repos?page=9>; rel="prev", ' +
                  '<https://api.github.com/user/repos?page=11>; rel="next", ' +
                  '<https://api.github.com/user/repos?page=50>; rel="last"')
        self.assertEqual(
            links_from_header.extract(header),
            {
                'first': 'https://api.github.com/user/repos?page=1',
                'prev': 'https://api.github.com/user/repos?page=9',
                'next': 'https://api.github.com/user/repos?page=11',
                'last': 'https://api.github.com/user/repos?page=50',
            }
        )


if __name__ == '__main__':
    unittest.main()
