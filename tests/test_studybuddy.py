import os
import sys
import tempfile
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import studybuddy


class StudyBuddyTests(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)
        studybuddy.DATA_FILE = self.path

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_and_list(self):
        studybuddy.add_task("Write report", "2026-10-20")
        tasks = studybuddy.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Write report")

    def test_ids_increase(self):
        a = studybuddy.add_task("A", "2026-10-20")
        b = studybuddy.add_task("B", "2026-10-21")
        self.assertEqual(b["id"], a["id"] + 1)

    def test_mark_done(self):
        t = studybuddy.add_task("A", "2026-10-20")
        self.assertTrue(studybuddy.mark_done(t["id"]))
        self.assertTrue(studybuddy.list_tasks()[0]["done"])

    def test_delete(self):
        t = studybuddy.add_task("A", "2026-10-20")
        self.assertTrue(studybuddy.delete_task(t["id"]))
        self.assertEqual(studybuddy.list_tasks(), [])
        self.assertFalse(studybuddy.delete_task(999))

    def test_due_soon(self):
        soon = (date.today() + timedelta(days=1)).isoformat()
        later = (date.today() + timedelta(days=30)).isoformat()
        studybuddy.add_task("Soon", soon)
        studybuddy.add_task("Later", later)
        result = studybuddy.due_soon(3)
        self.assertEqual([t["title"] for t in result], ["Soon"])

    def test_export_csv(self):
        studybuddy.add_task("A", "2026-10-20")
        out = self.path + ".csv"
        try:
            self.assertEqual(studybuddy.export_csv(out), 1)
            self.assertTrue(os.path.exists(out))
        finally:
            if os.path.exists(out):
                os.remove(out)


if __name__ == "__main__":
    unittest.main()
