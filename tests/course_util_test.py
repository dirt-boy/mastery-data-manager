import json
import js2py
js2py.translate_file('course_util.js', 'course_utiljs.py')
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
sample_e = [{
        "teachers": [{
            "courseId": 1,
            "userId": 1,
            "profile": {
                "name": {
                    "fullName": "Ee Ff"
                }
            }
        },
        {
            "courseId": 1,
            "userId": 2,
            "profile": {
                "name": {
                    "fullName": "Gg Hh"
                }
            }
        }],
        "students": [{
            "courseId": 1,
            "userId": 5,
            "profile": {
                "name": {
                    "fullName": "Aa Bb"
                }
            }
        },
        {
            "courseId": 1,
            "userId": 6,
            "profile": {
                "name": {
                    "fullName": "Cc Dd"
                }
            }
        }]
    },
    {
        "teachers": [{
            "courseId": 2,
            "userId": 3,
            "profile": {
                "name": {
                    "fullName": "Aa Cc"
                }
            }
        },
        {
            "courseId": 2,
            "userId": 4,
            "profile": {
                "name": {
                    "fullName": "Bb Dd"
                }
            }
        }],
        "students": [{
            "courseId": 2,
            "userId": 7,
            "profile": {
                "name": {
                    "fullName": "Cc Ee"
                }
            }
        },
        {
            "courseId": 2,
            "userId": 8,
            "profile": {
                "name": {
                    "fullName": "Ee Gg"
                }
            }
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
        self.assertEqual(str(course_utiljs.getRoster(sample_e)), str({
            "students": {
                "5": "Aa Bb",
                "6": "Cc Dd",
                "7": "Cc Ee",
                "8": "Ee Gg"
            },
            "teachers": {
                "1": "Ee Ff",
                "2": "Gg Hh",
                "3": "Aa Cc",
                "4": "Bb Dd"
            }
        }))
        self.assertEqual(str(course_utiljs.getRoster(sample_x)), str({'students': {}, 'teachers': {}}))

if __name__ == '__main__':
    unittest.main()
