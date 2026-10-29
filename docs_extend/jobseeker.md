# Jobseeker

- Table `jobseeker` (`config_extend.py`): one row per candidate, with the resume (`resume_url` or `resume_content`) and the profile fields filled from it.
- Worker: `venv/bin/python -m script_extend.worker_resume_parser` polls rows with `worker_status` Pending, reads each resume (S3 or Azure link, or the stored text), and fills the profile, `ai_rating` (1–10, strict) and `ai_remark` with Gemini (or OpenAI).
- `worker_status`: Pending, Processing, Completed, Failed (retried after 1 min, 5 min, 1 h, 1 day), Dead (retries used up).
