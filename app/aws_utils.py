import boto3
import logging

import boto3

def get_codebuild_logs(project_name, build_id, log_group_name, region="us-east-1"):
    """Fetch CodeBuild logs from CloudWatch."""
    logs_client = boto3.client("logs", region_name=region)
    codebuild_client = boto3.client("codebuild", region_name=region)

    try:
        # Get build logs
        log_events = logs_client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=f"codebuild/{project_name}/{build_id}"
        )
        logs = "\n".join(event["message"] for event in log_events["events"])
        return logs
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return None

