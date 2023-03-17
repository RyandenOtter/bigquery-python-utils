from typing import Union
from google.cloud import bigquery

def get_job(
        client: bigquery.Client,
        job_id: str
        ) -> Union[bigquery.LoadJob , bigquery.CopyJob , bigquery.ExtractJob , bigquery.QueryJob , bigquery.UnknownJob]:
    
    job = client.get_job(job_id)

    return job


def output_query_job(job: bigquery.QueryJob):
    
    print("Query Plan:")
    for count, entry in enumerate(job.query_plan):
        print(f"    Entry #{count}")
        print("    Records read:    ", entry.records_read)
        print("    Records written: ", entry.records_written)

        

    print("job_id", job.job_id)
    print("Timeline: ", job.timeline)
    print("Cache Hit: ", job.cache_hit)
    print("Reservation Usage: ", job.reservation_usage)

if __name__ == "__main__":
    client = bigquery.Client()
    job_id = 'bquxjob_12f89b56_1841f776575'
    job = get_job(
            client=client,
            job_id=job_id)

    if isinstance(job, bigquery.QueryJob):
        output_query_job(job)
    
