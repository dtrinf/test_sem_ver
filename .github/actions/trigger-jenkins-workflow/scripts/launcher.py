#!/usr/bin/env python3
import argparse
import json
import logging
import sys
import requests

from sardevops_jenkins_library.functions import (
    scan_repository,
    trigger_jenkins_job,
    check_job_status,
    approve_job_build,
    wait_for_job_completion,
    download_artifacts
)

def main(args):

    scan = args.scan
    deploy = args.deploy

    
    jenkins_scan_repository(args) if scan else None

    jenkins_run_pipeline(args) if deploy else None


def jenkins_scan_repository(args):
    jenkins_url = args.jenkins_url
    jenkins_user = args.jenkins_user
    jenkins_api_token = args.jenkins_api_token
    jenkins_job_name = args.jenkins_job_name

    parameters = args.parameters
    print(parameters)

    if jenkins_url is not None:
        scan_repository(jenkins_job_name, jenkins_url = jenkins_url, username=jenkins_user, api_token=jenkins_api_token)
    else:
        scan_repository(jenkins_job_name, username=jenkins_user, api_token=jenkins_api_token)

def jenkins_run_pipeline(args):
    pass


if __name__ == "__main__":

    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--jenkins_url", help="[Optional] Jenkins URL", type=str
    )
    parser.add_argument(
        "--jenkins_user", help="Jenkins User", type=str, required=True
    )
    parser.add_argument(
        "--jenkins_api_token", help="Jenkins API Token", type=str, required=True
    )
    parser.add_argument(
        "--jenkins_job_name", help="Jenkins Job Name", type=str, required=True
    )
    parser.add_argument(
        "--parameters", help="Jenkins Job Parameters", type=json.loads, default={}, required=False
    )
    parser.add_argument(
        "--wait_for_completion", help="[Optional] Wait for job completion", action="store_true", required=False
    )
    parser.add_argument(
        # Only required if --deploy is specified
        "--tag", help="Git Tag to deploy", type=str, required='--deploy' in sys.argv # or '--scan' in sys.argv
    )
    parser.add_argument(
        "--scan", help="[Optional] Scan Repository before triggering job", action="store_true", required=False
    )
    parser.add_argument(
        "--deploy", help="Deploy to environment", action="store_true", required=False
    )


    args = parser.parse_args()

    main(args)



