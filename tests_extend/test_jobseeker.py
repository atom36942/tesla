import unittest
from script_extend.worker_resume_parser import download_url_sign
from script_extend.worker_resume_parser import response_schema_build
from script_extend.worker_resume_parser import retry_delay_sec


class TestJobseekerWorker(unittest.TestCase):
    def test_schema_skips_base_columns_and_types_the_rest(self):
        schema = response_schema_build(column_type={"id": "bigint", "name": "text", "skills": "array", "experience": "numeric", "graduation_year": "integer", "projects": "jsonb"})
        self.assertEqual(set(schema["properties"]), {"name", "skills", "experience", "graduation_year", "projects"})
        self.assertEqual(schema["properties"]["skills"]["type"], "ARRAY")
        self.assertEqual(schema["properties"]["experience"]["type"], "NUMBER")
        self.assertEqual(schema["properties"]["graduation_year"]["type"], "INTEGER")

    def test_retry_delay_caps_at_last(self):
        self.assertEqual([retry_delay_sec(retry_count=n) for n in (-1, 0, 3, 9)], [60, 60, 86400, 86400])

    def test_url_left_alone_without_keys_or_when_signed(self):
        storage = {"azure_account_name": None, "azure_account_key": None, "aws_access_key_id": None, "aws_secret_access_key": None}
        self.assertEqual(download_url_sign(url="https://x.blob.core.windows.net/c/a.pdf", candidate_id=1, storage=storage), "https://x.blob.core.windows.net/c/a.pdf")
        self.assertEqual(download_url_sign(url="https://x/a.pdf?sig=1", candidate_id=1, storage={**storage, "azure_account_name": "a", "azure_account_key": "k"}), "https://x/a.pdf?sig=1")
