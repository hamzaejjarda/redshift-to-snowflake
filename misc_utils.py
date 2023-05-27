import os


def initialize_env():
    os.environ['DATA_ETL_REDSHIFT_USER_METRICS'] = ''
    os.environ['DATA_ETL_REDSHIFT_HOST_METRICS'] = ''
    os.environ['DATA_ETL_REDSHIFT_USER_PW_METRICS'] = ''
    os.environ['DATA_ETL_REDSHIFT_PORT'] = '5439'
    os.environ['DATA_ETL_AWS_ACCESS_KEY_ID'] = ''
    os.environ['DATA_ETL_AWS_SECRET_KEY_ID'] = ''
    os.environ['DATA_ETL_SNOWFLAKE_USER'] = ''
    os.environ['DATA_ETL_SNOWFLAKE_PW'] = ''
    os.environ['DATA_ETL_SNOWFLAKE_ACCOUNT'] = ''