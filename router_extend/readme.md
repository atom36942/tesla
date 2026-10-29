# router_extend
API routes: one `<feature>.py` with `router = APIRouter()`. A route with params reads them with `app_state.func_request_param_read`, calls a `func_*` and returns `{"status": 1, "message": result}`; no business logic. Every route needs a `config_api` entry (id 200+) in `config_extend.py`. See AGENTS.md (Routes, config_api).
