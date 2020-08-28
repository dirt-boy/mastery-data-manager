import json
import js2py
js2py.translate_file('course_util.js', 'tests/course_utiljs.py')
from course_utiljs import course_utiljs
import unittest

sample_a = [{
        "courses": [{
            "id": 1,
            "name": "a"
        },
        {
            "id": 2,
            "name": "aa"
        }]
    },
    {
        "courses": [{
            "id": 3,
            "name": "aaa"
        }]
    }]

sample_b = [{
        "courses": [{
            "id": 1,
            "name": "a"
        },
        {
            "id": 2,
            "name": "aa"
        }]
    },
    {
        "notcourses": [{
            "id": 3,
            "name": "aaa"
        }]
    }]
sample_c = [{
        "courseWork": [{
            "id": 1,
            "title": "b"
        },
        {
            "id": 2,
            "title": "bb"
        }]
    },
    {
        "courseWork": [{
            "id": 3,
            "title": "bbb"
        }]
    }]
sample_d = [{
        "courseWork": [{
            "id": 1,
            "title": "b"
        },
        {
            "id": 2,
            "title": "bb"
        }]
    },
    {
        "notcourseWork": [{
            "id": 3,
            "title": "bbb"
        }]
    }]

sample_x = []

class TestClassroomMethods(unittest.TestCase):

    def test_courselist(self):
        self.assertEqual(str(course_utiljs.getCourseList(sample_a, 'courses')), str({
            "1": "a",
            "2": "aa",
            "3": "aaa"
        }))
        self.assertEqual(str(course_utiljs.getCourseList(sample_b, 'courses')), str({
            "1": "a",
            "2": "aa"
        }))
        self.assertEqual(str(course_utiljs.getCourseList(sample_x, 'courses')), str({}))

    def test_courseWorklist(self):
        self.assertEqual(str(course_utiljs.getCourseList(sample_c, 'courseWork')), str({
            "1": "b",
            "2": "bb",
            "3": "bbb"
        }))
        self.assertEqual(str(course_utiljs.getCourseList(sample_d, 'courseWork')), str({
            "1": "b",
            "2": "bb"
        }))
        self.assertEqual(str(course_utiljs.getCourseList(sample_x, 'courseWork')), str({}))

    def test_roster(self):
        self.assertEqual(str(course_utiljs.getRoster(sample_x)), str({}))

if __name__ == '__main__':
    unittest.main()
