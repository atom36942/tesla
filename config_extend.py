# base
from config import config_column_int_mapping as base_config_column_int_mapping
from config import config_postgres as base_config_postgres
from config import config_api as base_config_api

# atom
config_column_int_mapping = {
**base_config_column_int_mapping,
"jobseeker": {
"worker_status": {None: "Pending", 1: "Processing", 2: "Completed", 3: "Failed", 4: "Dead"},
},
}

config_postgres = {
**base_config_postgres,
"table": {
**base_config_postgres["table"],
"jobseeker":[
{"name":"id","datatype":"bigint","identity":"always","is_primary": True},
{"name":"created_at","datatype":"timestamptz","default":"now()","index":"btree(created_at)"},
{"name":"created_by_id","datatype":"bigint"},
{"name":"updated_at","datatype":"timestamptz"},
{"name":"updated_by_id","datatype":"bigint"},
{"name":"verified_at","datatype":"timestamptz"},
{"name":"verified_by_id","datatype":"bigint"},
{"name":"deactivated_at","datatype":"timestamptz"},
{"name":"deactivated_by_id","datatype":"bigint"},
{"name":"deleted_at","datatype":"timestamptz"},
{"name":"deleted_by_id","datatype":"bigint"},
{"name":"profile","datatype":"text","index":"btree(profile)|gin_trgm(profile)"},
{"name":"name","datatype":"text"},
{"name":"email","datatype":"text"},
{"name":"college","datatype":"text[]"},
{"name":"resume_url","datatype":"text"},
{"name":"resume_content","datatype":"text"},
{"name":"video_url","datatype":"text"},
{"name":"skills","datatype":"text[]"},
{"name":"experience","datatype":"numeric(4,1)"},
{"name":"company_current","datatype":"text"},
{"name":"company_past","datatype":"text[]"},
{"name":"ctc_current","datatype":"integer"},
{"name":"ctc_expected","datatype":"integer"},
{"name":"currency","datatype":"text"},
{"name":"notice_period_days","datatype":"integer"},
{"name":"location_current","datatype":"text"},
{"name":"location_preferred","datatype":"text[]"},
{"name":"qualification_highest","datatype":"text"},
{"name":"source","datatype":"text"},
{"name":"linkedin_url","datatype":"text"},
{"name":"github_url","datatype":"text"},
{"name":"portfolio_url","datatype":"text"},
{"name":"languages","datatype":"text[]"},
{"name":"gender","datatype":"text"},
{"name":"worker_status","datatype":"smallint","in":(1,2,3,4),"index":"btree(worker_status,worker_next_retry_at,created_at)"},
{"name":"worker_retry_count","datatype":"integer","default":0},
{"name":"worker_next_retry_at","datatype":"timestamptz","default":"now()"},
{"name":"worker_processed_at","datatype":"timestamptz"},
{"name":"worker_last_error","datatype":"text"},
{"name":"ai_remark","datatype":"text"},
{"name":"ai_rating","datatype":"numeric(3,1)"},
{"name":"remark","datatype":"text"},
{"name":"rating","datatype":"numeric(3,1)"},
{"name":"status","datatype":"smallint","default":1},
{"name":"mobile","datatype":"text"},
{"name":"work_authorization","datatype":"text"},
{"name":"graduation_year","datatype":"integer"},
{"name":"certifications","datatype":"jsonb"},
{"name":"summary","datatype":"text"},
{"name":"projects","datatype":"jsonb",},
{"name":"industry","datatype":"text"}
],
},
}

config_api = {
**base_config_api,
}

# misc
